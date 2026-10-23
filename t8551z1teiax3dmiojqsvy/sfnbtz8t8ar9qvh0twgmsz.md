# Auditoria do código

Auditoria interna do commander executada com checklists próprias de auditoria de aplicações e de sistemas: configuração, autenticação, gestão de sessão/token, tratamento de erros, validação de entrada, integridade de logs e limites. Achados, correções aplicadas e riscos aceitos ficam registrados aqui — é o documento de maturidade do repositório.

## Achados e correções aplicadas

1. **Log de auditoria sem evidência de adulteração.** Antes: linhas JSONL soltas — quem editasse o arquivo não deixava sinal. Correção: cadeia de hashes na escrita (cada entrada carrega o hash da anterior, em append atômico com lock) e a tool `verify_audit`, que recomputa a cadeia e aponta onde ela quebra. Linhas antigas sem hash são contadas como legado, sem invalidar o restante.
2. **Erro 500 vazava detalhe interno.** Antes: a resposta de erro interno incluía o texto da exceção. Correção: o cliente recebe "erro interno (detalhe no log de auditoria)"; o detalhe vai só para o log — e todo erro 500 passou a ser auditado (antes não era).
3. **Respostas sem proteção de cache.** Correção: toda resposta HTTP sai com `Cache-Control: no-store`.
4. **Corpo gigante corrompia a conexão.** Antes: corpo acima do teto era rejeitado sem fechar a conexão, e os bytes restantes envenenavam a próxima requisição keep-alive. Correção: rejeição por `Content-Length` com fechamento limpo da conexão.

## Verificado como conforme

- Comparação do token em tempo constante (`compare_digest`), sem vazamento de timing.
- Corpo de requisição limitado a 8 MB, rejeitado pelo cabeçalho antes da leitura.
- Token guardado com permissão 0600; bind padrão em `127.0.0.1`, nunca em `0.0.0.0`.
- Limites das tools são máximos de verdade com aplicação em um único ponto (leitura capada na fonte em 1 MB, saídas capadas em 64 KB por bytes, timeout travado em 600 s, buscas capadas em 200 resultados).
- Toda chamada de tool gera registro de auditoria, inclusive falhas.

## Riscos aceitos (waivers registrados)

- **Permissões totais por padrão.** Decisão do dono do produto, documentada no README: quem instala aceita o mesmo nível de confiança de um terminal aberto; restrições são opt-in.
- **Remoção sempre permanente.** Regra do produto: nada vai para a Lixeira, sem modo reversível.

## Verificação

57 testes automatizados cobrem, entre outros: validade da cadeia de auditoria (incluindo rotação com âncora), detecção de linha forjada no log, cabeçalho `no-store`, rejeição de corpo acima do teto, atraso progressivo em falhas de autenticação, validação de tipos de argumento, baseline e diff de estado, tetos de leitura/busca/timeout e o comportamento de todas as 25 tools.

## Rodada 2 — monitoramento e validação

5. **Sem baseline de estado.** Antes: nenhuma referência do que é "normal" na máquina. Correção: tools `capture_baseline`/`check_baseline` — fotografia com SHA-256 das árvores pedidas + processos + identificação da máquina, e diff posterior. Teste de auditoria periódico e roteirizável = monitoramento contínuo.
6. **Tipos de argumento não validados.** Antes: tipo errado virava crash dentro do handler. Correção: validação de entrada contra o `inputSchema` de cada tool, antes do handler, no protocolo MCP e na rota HTTP — tipo errado vira erro de tool limpo.
7. **Log de auditoria sem gestão de tamanho.** Correção: rotação automática ao atingir o teto (10 MB por padrão; config só baixa), com âncora do último hash gravada à parte para a cadeia continuar verificável entre arquivos.
8. **Força bruta no token sem fricção.** Correção: atraso progressivo por origem após 3 falhas consecutivas de autenticação (0,5 s dobrando até 5 s), em vez de bloqueio rígido que derrubaria o uso legítimo.
