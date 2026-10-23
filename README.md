# Servidor MCP que entrega o computador ao Muse

Servidor Model Context Protocol em Python puro, sem dependências: 25 tools para arquivos, processos, terminal, limpeza de temporários, busca full-text, verificação de auditoria, baseline de sistema e reconhecimento de logs, faladas por stdio (JSON-RPC 2.0, protocolo 2025-06-18). Qualquer cliente MCP — incluindo o Muse — conecta por subprocesso e passa a gerenciar a máquina local com escopo de paths, política de comandos e auditoria ligados por padrão.

## As 25 tools

| Tool | O que faz |
|---|---|
| `read_file` | Lê um arquivo de texto dentro do escopo |
| `write_file` | Cria ou sobrescreve arquivo; cria diretórios pais |
| `edit_file` | Substitui um trecho exato; exige `replace_all` se o trecho for ambíguo |
| `list_directory` | Lista diretório com tipo, tamanho e data de modificação |
| `create_directory` | Cria diretório (com pais) |
| `move_file` | Move ou renomeia arquivo/diretório |
| `delete_path` | Apaga permanentemente (sem Lixeira) um arquivo ou diretório, inclusive não vazio (recursivo); a raiz do sistema é recusada |
| `search_files` | Busca por padrão glob sob uma raiz do escopo |
| `get_file_info` | Tamanho, permissões e datas de um caminho |
| `execute_command` | Roda um comando de shell com timeout e saída truncada |
| `list_processes` | Lista processos (pid, ppid, nome, estado, linha de comando) |
| `kill_process` | Envia um sinal a um processo; recusar o próprio servidor |
| `clean_temp` | Comando padrão de limpeza, sempre permanente: dry_run inventaria; dry_run=false apaga os arquivos dos temporários do sistema (nunca as pastas) |
| `index_files` | Indexa arquivos de texto num índice SQLite FTS5: qualquer pasta, todas as subpastas, determinístico |
| `search_index` | Busca full-text no índice FTS5 (sintaxe MATCH): caminho + snippet, por relevância |
| `verify_audit` | Verifica a cadeia de integridade do log de auditoria: detecta linhas adulteradas, removidas ou inseridas |
| `capture_baseline` | Fotografa a referência: hash SHA-256 das árvores pedidas, processos em execução, identificação da máquina |
| `check_baseline` | Compara o estado atual com a baseline: arquivos alterados/removidos/novos e processos novos/encerrados |
| `sniff_log` | Reconhece o formato de um log .txt sem ler o conteúdo: delimitador, cabeçalho, timestamp, total de linhas |
| `screenshot` | Captura a tela em PNG (só Windows; com compressão opcional) |
| `ui_elements` | Árvore de acessibilidade da tela (só Windows) |
| `click` | Clique de mouse numa coordenada (só Windows) |
| `type_text` | Digitação de texto (só Windows) |
| `press_key` | Teclas especiais (só Windows) |
| `find_template` | Localiza um elemento na tela por template (só Windows) |

## Limites reais, aplicados num único ponto

Os limites são máximos de verdade — configuração e pedido só podem baixá-los, nunca subi-los:

- leitura de arquivo capada **na fonte** (1 MB, sem carregar o arquivo inteiro na RAM);
- saídas de comando capadas em **bytes** (64 KB por stream);
- timeout travado em 600 s (padrão 120 s), com valor inválido caindo para o padrão;
- buscas capadas em 200 resultados.

Toda a aplicação passa por um único conjunto de helpers no código (`_clamp_int`, `_read_capped`, `_truncate_utf8`, `_cap_results`): nenhuma tool implementa o próprio corte. Na migração para C++/Elixir, o contrato é o mesmo, com leitura por chunks (mmap) e indexação concorrente para máxima performance em escala.

## Baseline e monitoramento contínuo

`capture_baseline` fotografa a referência — hash SHA-256 de cada arquivo das árvores pedidas (o padrão é o próprio código do servidor), nomes dos processos em execução e a identificação da máquina — e `check_baseline` devolve o diff: arquivos alterados, removidos e novos; processos novos e encerrados. É o teste de auditoria transformado em rotina: rodar `check_baseline` periodicamente é o monitoramento contínuo, e cada desvio inesperado vira investigação. O log de auditoria também roda sozinho ao atingir 10 MB (config pode baixar), e a cadeia de hashes continua válida entre arquivos pela âncora gravada na rotação.

## Arquivos grandes e logs: leitura parte a parte

O processo que protege a conversa: `read_file` nunca abre o arquivo inteiro. Cada chamada faz **uma única leitura de no máximo 1 MB + 1 byte, direto do disco**, a partir do `offset` pedido — o +1 byte existe só para dizer que há mais. O tamanho do arquivo não muda o custo: 3 GB ou 28 GB custam o mesmo (provado em demonstração: 0,09 s nas duas leituras).

- `offset` e `limit` são em bytes; o teto de 1 MB por chamada é real e a configuração só pode baixá-lo.
- O retorno sempre traz: `content` (no máximo 1 MB), `bytes` (o tamanho **real** do arquivo — você sabe exatamente o que não viu), `offset`, `next_offset` (onde a leitura continua, ou `null` no fim) e `truncated`.
- Um .txt de 28 GB é lido assim: reconhecer o formato, buscar o que interessa (`search_index`), e ler as fatias que importam. **Cada fatia entra na conversa; o arquivo, nunca.**

### sniff_log: reconhecer antes de ler

Para a análise de logs — cada fonte tem seu próprio padrão, e reconhecer o padrão é o que permite automatizar e gastar menos. O `sniff_log` lê só o início do arquivo e devolve o perfil do formato: delimitador, cabeçalho e campos, formato de timestamp (ISO 8601, Apache, epoch), **total de linhas** (contado por streaming, sem entrar na RAM) e amostra das primeiras linhas. Com o perfil na mão, a extração é automática e os tokens vão só para os trechos que importam.

### Limites reais do Muse (medidos)

Verificado nesta sessão, no modelo Muse Spark: a janela de contexto é de **350 mil tokens** por conversa; a compactação dispara aos **272 mil tokens** e retém os últimos 40 mil — a memória de trabalho útil é de ~270 mil tokens antes de o material mais antigo ser resumido. Regra prática: ~3 a 4 caracteres por token em português e código, então uma fatia de 1 MB ocupa de um quarto a um terço da janela. Por isso os tetos existem: eles garantem que operar arquivos gigantes nunca esvazie o contexto — e por isso o processo certo é sempre reconhecer, buscar e ler em fatias, guardando só os achados.

### Como os arquivos do computador chegam ao Muse

Pelo canal do commander, **o arquivo fica no disco da máquina**. O que viaja pelo tailnet são só os pedaços pedidos: fatias do `read_file`, perfis do `sniff_log`, diffs do `check_baseline`, resumos do `verify_audit` e trechos do `search_index`. O arquivo em si nunca "vai para a nuvem". Os anexos enviados no chat são outro canal, com limites próprios do aplicativo — não se misturam com este.

## Permissões totais por padrão — e o risco é claro

Por padrão, este servidor tem acesso total à máquina: lê, escreve, move e apaga qualquer arquivo (inclusive diretórios não vazios, recursivamente) e executa qualquer comando, com os privilégios do usuário que o lançou. É a mesma confiança depositada num terminal aberto. Quem não aceita esse risco não deve rodar o servidor sem restringi-lo antes.

As restrições existem, mas são opt-in, via `config.json`:

- **Escopo de paths.** `allowed_directories` limita onde as tools de arquivo operam (padrão: `/`, a raiz inteira). Todo caminho é resolvido (realpath) antes da checagem; symlink que escapa de um escopo restrito é rejeitado.
- **Caminhos bloqueados.** `blocked_paths` veta subárvores mesmo dentro do escopo.
- **Política de comandos.** `blocked_command_patterns` barra comandos por regex (padrão: lista vazia, nada é barrado).

Dois guardas duros não são configuráveis: o servidor não encerra a si mesmo via `kill_process`, e não apaga a raiz do sistema de arquivos.

**Auditoria fica sempre ligada.** Toda chamada de tool grava uma linha JSONL com timestamp, tool, resumo dos argumentos e resultado. Conteúdos de arquivo não vão para o log — só metadados.

## Como rodar

```bash
python3 vmmaieuzwn7j9llhbznbgs.py
```

O servidor lê JSON-RPC por stdin e responde por stdout (uma mensagem por linha). Exemplo de handshake:

```
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"demo","version":"0"}}}
{"jsonrpc":"2.0","method":"notifications/initialized"}
{"jsonrpc":"2.0","id":2,"method":"tools/list"}
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"list_directory","arguments":{"path":"~"}}}
```

## Como configurar

Copie o exemplo e ajuste:

```bash
mkdir -p ~/.config/muse-terminal-commander
cp d9s6nk714nxs89p1ebe18x.json ~/.config/muse-terminal-commander/config.json
```

Para apontar para outro arquivo de configuração: `MUSE_COMMANDER_CONFIG=/caminho/config.json python3 vmmaieuzwn7j9llhbznbgs.py`.

## Como testar

```bash
python3 dvfru5d7epa1dcq4iov6hs/s9axlvnq3wa5r17ts3i3rt.py
python3 dvfru5d7epa1dcq4iov6hs/l27goehokaj0s0ywrugjae.py
python3 dvfru5d7epa1dcq4iov6hs/phn6u3340asht9e94ti896.py
```

57 testes ponta a ponta: handshake, catálogo de tools, roundtrip de escrita/leitura/edição, rejeição de fuga de escopo restrito, remoção recursiva de diretório, bloqueio de comando perigoso quando configurado, permissões totais por padrão, inventário e limpeza de temporários (dry-run e deleção), limites reais (cap na fonte, config não sobe o teto, timeout travado, truncamento em bytes, teto de 200 resultados), indexação e busca FTS5 (indexação, reindexação determinística, teto de resultados, consulta inválida), cadeia de integridade do log de auditoria (validade, detecção de linha forjada e rotação com âncora), validação de tipos de argumento, baseline e diff (captura, conferência limpa, detecção de alteração e adição), leitura parte a parte (offset/limit, teto que não cede, offset além do fim) e reconhecimento de formato de log (CSV com timestamp, texto livre), execução real, listagem e encerramento de processo, escrita do log de auditoria, compressão de screenshot, validação de PNG e decodificação de saída em camadas (UTF-8, locale, cp1252, cp850, latin-1). Sem dependências externas — só biblioteca padrão.

## Licença

MIT.
