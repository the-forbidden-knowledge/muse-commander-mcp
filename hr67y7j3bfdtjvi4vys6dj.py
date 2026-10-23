import argparse
import importlib.util
import json
import locale
import os
import secrets
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
APP_DIR_NAME = 'muse-commander-agent'
DEFAULT_BIND = '127.0.0.1'
DEFAULT_PORT = 8741
MAX_BODY_BYTES = 8 * 1024 * 1024
DEFAULT_WATCH_INTERVAL = 30

def vg5ix2qswaivxxj1g91dhg():
    z1fflg86ixzbc11laoq4jb = []
    ta5wbggdxla2kgkei4slse = os.environ.get('MUSE_COMMANDER_SERVER')
    if ta5wbggdxla2kgkei4slse:
        z1fflg86ixzbc11laoq4jb.append(Path(ta5wbggdxla2kgkei4slse).expanduser())
    l9zlvakaf7bg7vn1lb0xjy = Path(__file__).resolve().parent
    z1fflg86ixzbc11laoq4jb.append(l9zlvakaf7bg7vn1lb0xjy.parent / 'muse-terminal-commander' / 'vmmaieuzwn7j9llhbznbgs.py')
    z1fflg86ixzbc11laoq4jb.append(l9zlvakaf7bg7vn1lb0xjy / 'vmmaieuzwn7j9llhbznbgs.py')
    for cktfjcuwrfh2r5swfa0cm7 in z1fflg86ixzbc11laoq4jb:
        if cktfjcuwrfh2r5swfa0cm7.is_file():
            return cktfjcuwrfh2r5swfa0cm7
    raise SystemExit('vmmaieuzwn7j9llhbznbgs.py nao encontrado. Defina MUSE_COMMANDER_SERVER com o caminho do muse-terminal-commander/vmmaieuzwn7j9llhbznbgs.py.')

def tef6781iwc5qvwqu3uwter():
    xdknfxaqw65ww8k4q156m8 = importlib.util.spec_from_file_location('commander_server', vg5ix2qswaivxxj1g91dhg())
    ze1aa3elmbscanv7bfzd88 = importlib.util.module_from_spec(xdknfxaqw65ww8k4q156m8)
    xdknfxaqw65ww8k4q156m8.loader.exec_module(ze1aa3elmbscanv7bfzd88)
    return ze1aa3elmbscanv7bfzd88

def x2gmukbfaoen4t7xlfzzef(eeav0ygd57j0tk9xl3wmv6):
    if not eeav0ygd57j0tk9xl3wmv6:
        return ''
    if isinstance(eeav0ygd57j0tk9xl3wmv6, str):
        return eeav0ygd57j0tk9xl3wmv6
    for jdi6d09swyq8vl6bxrpgt4 in ('utf-8', locale.getpreferredencoding(False) or 'utf-8', 'cp1252', 'cp850', 'latin-1'):
        try:
            return eeav0ygd57j0tk9xl3wmv6.decode(jdi6d09swyq8vl6bxrpgt4)
        except (UnicodeDecodeError, LookupError):
            continue
    return eeav0ygd57j0tk9xl3wmv6.decode('latin-1', errors='replace')

def g8shk6wlr2g9r1jbkrbhrd():
    try:
        tbm8n1zum100kh90w4j4ip = subprocess.run(['tailscale', 'ip', '-4'], capture_output=True, timeout=10)
    except (OSError, subprocess.SubprocessError) as czk6iezmla8i9yc5ufoko8:
        raise SystemExit('tailscale CLI nao respondeu (%s). Verifique se o Tailscale esta instalado, conectado e no PATH.' % czk6iezmla8i9yc5ufoko8)
    if tbm8n1zum100kh90w4j4ip.returncode != 0:
        raise SystemExit('tailscale ip falhou: %s' % (x2gmukbfaoen4t7xlfzzef(tbm8n1zum100kh90w4j4ip.stderr).strip() or x2gmukbfaoen4t7xlfzzef(tbm8n1zum100kh90w4j4ip.stdout).strip()))
    for thecncg7svqxvwjk4t78mn in x2gmukbfaoen4t7xlfzzef(tbm8n1zum100kh90w4j4ip.stdout).splitlines():
        pgfruv7d7kyh67zuag4ho4 = thecncg7svqxvwjk4t78mn.strip()
        if pgfruv7d7kyh67zuag4ho4.startswith('100.'):
            return pgfruv7d7kyh67zuag4ho4
    raise SystemExit('nenhum endereco tailnet (100.x) encontrado nesta maquina.')

def lite7znis650th4uyjhzlo(i1gw0l3z5ggblij52h6oe7, x0imgxum0xdad7q07c3e8t):
    if i1gw0l3z5ggblij52h6oe7 == 'tailnet':
        return g8shk6wlr2g9r1jbkrbhrd()
    return i1gw0l3z5ggblij52h6oe7 or x0imgxum0xdad7q07c3e8t['bind']

def n8z6379e6qhy6xx14kq24j():
    return Path.home() / '.config' / APP_DIR_NAME

def bwc0slx16em2ts401bh7mb():
    return n8z6379e6qhy6xx14kq24j() / 'token'

def g2iqtjrehz63pwavrtctvu():
    return n8z6379e6qhy6xx14kq24j() / 'config.json'

def l6qzhh8lg37slprr6qlspx(a1hgd3vvpu23u2r558mo9o=False):
    f06xwynu1bxa7qpv9oc460 = n8z6379e6qhy6xx14kq24j()
    f06xwynu1bxa7qpv9oc460.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(f06xwynu1bxa7qpv9oc460, 448)
    except OSError:
        pass
    lbhve6zgm6y7zpp2jq6y14 = bwc0slx16em2ts401bh7mb()
    if lbhve6zgm6y7zpp2jq6y14.exists() and (not a1hgd3vvpu23u2r558mo9o):
        print('Ja instalado: %s existe. Use --force para gerar um token novo.' % lbhve6zgm6y7zpp2jq6y14)
        return 1
    f6h0oikd84ju78a7clheyf = secrets.token_urlsafe(32)
    lbhve6zgm6y7zpp2jq6y14.write_text(f6h0oikd84ju78a7clheyf + '\n', encoding='utf-8')
    os.chmod(lbhve6zgm6y7zpp2jq6y14, 384)
    bcwejblzwwt4cry5kdw6u6 = {'bind': DEFAULT_BIND, 'port': DEFAULT_PORT}
    g2iqtjrehz63pwavrtctvu().write_text(json.dumps(bcwejblzwwt4cry5kdw6u6, indent=2) + '\n', encoding='utf-8')
    print('Instalado.')
    print('Config:  %s' % g2iqtjrehz63pwavrtctvu())
    print('Token:   %s (permissao 0600)' % lbhve6zgm6y7zpp2jq6y14)
    print()
    print('TOKEN DA INSTALACAO (guarde; ele nao sera mostrado de novo):')
    print(f6h0oikd84ju78a7clheyf)
    return 0

def emaiyy9iftsfkf8qy0pfe0():
    wywd1nootmmf42i4tq0v70 = {'bind': DEFAULT_BIND, 'port': DEFAULT_PORT}
    ntabwmbkkbl8ozoajek82o = g2iqtjrehz63pwavrtctvu()
    if ntabwmbkkbl8ozoajek82o.is_file():
        try:
            w9ja46o0p0y3bb1b3frxcx = json.loads(ntabwmbkkbl8ozoajek82o.read_text(encoding='utf-8'))
            if isinstance(w9ja46o0p0y3bb1b3frxcx, dict):
                wywd1nootmmf42i4tq0v70.update(w9ja46o0p0y3bb1b3frxcx)
        except Exception:
            pass
    return wywd1nootmmf42i4tq0v70

def cgtcussetvy9xxuf8x4n90():
    c3z8eu908i7z6mqh0fzalh = bwc0slx16em2ts401bh7mb()
    if not c3z8eu908i7z6mqh0fzalh.is_file():
        raise SystemExit('Token nao encontrado em %s. Rode: hr67y7j3bfdtjvi4vys6dj.py install' % c3z8eu908i7z6mqh0fzalh)
    return c3z8eu908i7z6mqh0fzalh.read_text(encoding='utf-8').strip()

def n30190c40s24xspsoxlxfz(lsb3n2wrmhu10t47palp5z, lnvf83ldcobibouo715t84):
    oaideisbm3dpx62d7zixow = 'Bearer ' + lnvf83ldcobibouo715t84
    dgthpuo8iqczty2zg36cdw = {}
    rbvpu1zckm8o9lnkelqyc0 = 3
    e4rhlinedkpc4kzxnl0xhe = 5.0

    class d6l609zz8r938vhy7ap1za(BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'

        def log_message(self, erdvgjsj506pdyxwts465o, *xgpyz9osec4j9n8cqh5w6r):
            pass

        def rc31oipvzq9bo2r90q61fv(self, du7bm2c9uwjh73bqejzwor, tcu8tfe2afrlz5gmqfcthz):
            t65mxxctp3be9gnojplrcx = json.dumps(tcu8tfe2afrlz5gmqfcthz, ensure_ascii=False).encode('utf-8')
            self.send_response(du7bm2c9uwjh73bqejzwor)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(t65mxxctp3be9gnojplrcx)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(t65mxxctp3be9gnojplrcx)

        def lwj1ywo0mufz8gnl7k1njl(self):
            fwzz2b705ku5uhwey0eeep = self.client_address[0]
            fqp1bdhtkyr7bi05e856co = secrets.compare_digest(self.headers.get('Authorization', ''), oaideisbm3dpx62d7zixow)
            if fqp1bdhtkyr7bi05e856co:
                dgthpuo8iqczty2zg36cdw.pop(fwzz2b705ku5uhwey0eeep, None)
                return True
            awjhvg0dz9hhksh467sdbj = dgthpuo8iqczty2zg36cdw.get(fwzz2b705ku5uhwey0eeep, 0) + 1
            dgthpuo8iqczty2zg36cdw[fwzz2b705ku5uhwey0eeep] = awjhvg0dz9hhksh467sdbj
            if awjhvg0dz9hhksh467sdbj > rbvpu1zckm8o9lnkelqyc0:
                time.sleep(min(0.5 * 2 ** (awjhvg0dz9hhksh467sdbj - rbvpu1zckm8o9lnkelqyc0), e4rhlinedkpc4kzxnl0xhe))
            return False

        def ao2zxtww5l6wqm8t0qv9i6(self):
            if not self.lwj1ywo0mufz8gnl7k1njl():
                self.rc31oipvzq9bo2r90q61fv(401, {'ok': False, 'error': 'nao autorizado'})
                return False
            return True

        def do_GET(self):
            if not self.ao2zxtww5l6wqm8t0qv9i6():
                return
            if self.path == '/v1/health':
                self.rc31oipvzq9bo2r90q61fv(200, {'status': 'ok', 'tools': len(lsb3n2wrmhu10t47palp5z.TOOLS)})
            elif self.path == '/v1/tools':
                odcgcjf9p7l1boydv5wfxp = [{'name': fefv44qo9iy77uz59tqs1i['name'], 'description': fefv44qo9iy77uz59tqs1i['description'], 'inputSchema': fefv44qo9iy77uz59tqs1i['inputSchema']} for fefv44qo9iy77uz59tqs1i in lsb3n2wrmhu10t47palp5z.TOOLS]
                self.rc31oipvzq9bo2r90q61fv(200, {'tools': odcgcjf9p7l1boydv5wfxp})
            else:
                self.rc31oipvzq9bo2r90q61fv(404, {'ok': False, 'error': 'rota nao encontrada: %s' % self.path})

        def do_POST(self):
            if not self.ao2zxtww5l6wqm8t0qv9i6():
                return
            if self.path != '/v1/call':
                self.rc31oipvzq9bo2r90q61fv(404, {'ok': False, 'error': 'rota nao encontrada: %s' % self.path})
                return
            try:
                k7py4xdi2nmdpmhfxipnt1 = int(self.headers.get('Content-Length', '0'))
            except ValueError:
                k7py4xdi2nmdpmhfxipnt1 = 0
            if k7py4xdi2nmdpmhfxipnt1 <= 0 or k7py4xdi2nmdpmhfxipnt1 > MAX_BODY_BYTES:
                self.close_connection = True
                self.rc31oipvzq9bo2r90q61fv(400, {'ok': False, 'error': 'corpo invalido'})
                return
            try:
                ofhouvur6pofvgt4jc6ca2 = json.loads(self.rfile.read(k7py4xdi2nmdpmhfxipnt1).decode('utf-8'))
            except Exception:
                self.rc31oipvzq9bo2r90q61fv(400, {'ok': False, 'error': 'JSON invalido'})
                return
            zw0zcp016ky63pmlel1798 = ofhouvur6pofvgt4jc6ca2.get('tool')
            vgeydaib5sdwn48urb6mic = ofhouvur6pofvgt4jc6ca2.get('arguments') or {}
            ju6o56aef1zlsv6q5eqyrw = lsb3n2wrmhu10t47palp5z.HANDLERS.get(zw0zcp016ky63pmlel1798)
            if ju6o56aef1zlsv6q5eqyrw is None:
                self.rc31oipvzq9bo2r90q61fv(400, {'ok': False, 'error': 'tool desconhecida: %s' % zw0zcp016ky63pmlel1798})
                return
            try:
                lsb3n2wrmhu10t47palp5z.validate_tool_arguments(zw0zcp016ky63pmlel1798, vgeydaib5sdwn48urb6mic)
            except lsb3n2wrmhu10t47palp5z.ToolError as ji5iy1pmvrudneutq1x6vq:
                lsb3n2wrmhu10t47palp5z.audit(zw0zcp016ky63pmlel1798, {'via': 'agent-http'}, False, ji5iy1pmvrudneutq1x6vq)
                self.rc31oipvzq9bo2r90q61fv(200, {'ok': False, 'error': str(ji5iy1pmvrudneutq1x6vq)})
                return
            try:
                z7ip45vg3nvcuh5jgohisv = ju6o56aef1zlsv6q5eqyrw(vgeydaib5sdwn48urb6mic)
                lsb3n2wrmhu10t47palp5z.audit(zw0zcp016ky63pmlel1798, {'via': 'agent-http'}, True)
                self.rc31oipvzq9bo2r90q61fv(200, {'ok': True, 'result': z7ip45vg3nvcuh5jgohisv})
            except lsb3n2wrmhu10t47palp5z.ToolError as ji5iy1pmvrudneutq1x6vq:
                lsb3n2wrmhu10t47palp5z.audit(zw0zcp016ky63pmlel1798, {'via': 'agent-http'}, False, ji5iy1pmvrudneutq1x6vq)
                self.rc31oipvzq9bo2r90q61fv(200, {'ok': False, 'error': str(ji5iy1pmvrudneutq1x6vq)})
            except KeyError as ji5iy1pmvrudneutq1x6vq:
                self.rc31oipvzq9bo2r90q61fv(400, {'ok': False, 'error': 'argumento obrigatorio faltando: %s' % ji5iy1pmvrudneutq1x6vq})
            except Exception as ji5iy1pmvrudneutq1x6vq:
                lsb3n2wrmhu10t47palp5z.audit(zw0zcp016ky63pmlel1798, {'via': 'agent-http'}, False, ji5iy1pmvrudneutq1x6vq)
                self.rc31oipvzq9bo2r90q61fv(500, {'ok': False, 'error': 'erro interno (detalhe no log de auditoria)'})
    return d6l609zz8r938vhy7ap1za

def u6sebo359x76b6gyf3tfsk(vy1hp2d2io3kw52ke34upg=None, ohib62281lemaltdamtrs5=None, kwif1wx8ucikekjcsuldk5=DEFAULT_WATCH_INTERVAL):
    yosrt6oeeg8tz97er4acx3 = tef6781iwc5qvwqu3uwter()
    vzmhp5zzqjkvb3sh2v0pgl = cgtcussetvy9xxuf8x4n90()
    dfcr5jpwbq1col27p71igy = emaiyy9iftsfkf8qy0pfe0()
    ohib62281lemaltdamtrs5 = int(ohib62281lemaltdamtrs5 if ohib62281lemaltdamtrs5 is not None else dfcr5jpwbq1col27p71igy['port'])
    rialb038ktmb7yinxgpnx4 = vy1hp2d2io3kw52ke34upg == 'tailnet'
    i4vob6al99qcv865o1zfob = lite7znis650th4uyjhzlo(vy1hp2d2io3kw52ke34upg, dfcr5jpwbq1col27p71igy)
    while True:
        y9qzk9xdva9jcxjfd4dzn8 = ThreadingHTTPServer((i4vob6al99qcv865o1zfob, ohib62281lemaltdamtrs5), n30190c40s24xspsoxlxfz(yosrt6oeeg8tz97er4acx3, vzmhp5zzqjkvb3sh2v0pgl))
        y9qzk9xdva9jcxjfd4dzn8.daemon_threads = True
        rdnnfl1t831ncz6mkc430q = {'rebind': False}
        if rialb038ktmb7yinxgpnx4:

            def a6i37zjf7yahz4dth8f14u(mfm183vhsbbfhq8c2v9sw7=y9qzk9xdva9jcxjfd4dzn8, skvqf4aao0dl0w5y1r0or8=i4vob6al99qcv865o1zfob):
                while True:
                    time.sleep(kwif1wx8ucikekjcsuldk5)
                    try:
                        tajyn6eu5q6zzqrosel0nu = g8shk6wlr2g9r1jbkrbhrd()
                    except SystemExit:
                        continue
                    if tajyn6eu5q6zzqrosel0nu != skvqf4aao0dl0w5y1r0or8:
                        rdnnfl1t831ncz6mkc430q['rebind'] = True
                        mfm183vhsbbfhq8c2v9sw7.shutdown()
                        return
            threading.Thread(target=a6i37zjf7yahz4dth8f14u, daemon=True).start()
        mubva58wzzkjrqhqcrryj9, jxqs8mme1id4xpkln0ieij = y9qzk9xdva9jcxjfd4dzn8.server_address[:2]
        print('AGENT_LISTENING %s %d' % (mubva58wzzkjrqhqcrryj9, jxqs8mme1id4xpkln0ieij), flush=True)
        try:
            y9qzk9xdva9jcxjfd4dzn8.serve_forever()
        except KeyboardInterrupt:
            y9qzk9xdva9jcxjfd4dzn8.server_close()
            return 0
        y9qzk9xdva9jcxjfd4dzn8.server_close()
        if not rdnnfl1t831ncz6mkc430q['rebind']:
            return 0
        i4vob6al99qcv865o1zfob = g8shk6wlr2g9r1jbkrbhrd()
        print('AGENT_REBIND %s %d' % (i4vob6al99qcv865o1zfob, ohib62281lemaltdamtrs5), flush=True)

def lq86yd54cjujjs4339ia59(fx9ybska466d8s1fbqeii3=None):
    r57ub631wv8bvel5log2ih = argparse.ArgumentParser(prog='hr67y7j3bfdtjvi4vys6dj.py', description='Agente instalavel do commander (v1).')
    wskve9igggsov659br7uo9 = r57ub631wv8bvel5log2ih.add_subparsers(dest='command', required=True)
    phhitsqbe52xt13vv02egs = wskve9igggsov659br7uo9.add_parser('install', help='Gera token e configuracao da instalacao.')
    phhitsqbe52xt13vv02egs.add_argument('--force', action='store_true', help='Regenera o token se ja existir.')
    ciowvv9u40mxhuiulwmvms = wskve9igggsov659br7uo9.add_parser('run', help='Sobe a API HTTP do agente.')
    ciowvv9u40mxhuiulwmvms.add_argument('--bind', default=None, help="Endereco de bind: um IP, ou 'tailnet' para descobrir o IPv4 do tailnet e rotacionar sozinho quando ele mudar (padrao: config, 127.0.0.1).")
    ciowvv9u40mxhuiulwmvms.add_argument('--port', type=int, default=None, help='Porta (padrao: config, 8741; 0 = efemera).')
    ciowvv9u40mxhuiulwmvms.add_argument('--watch-interval', type=int, default=DEFAULT_WATCH_INTERVAL, help='Segundos entre checagens do IP do tailnet no modo --bind tailnet (padrao: 30).')
    mlfvs0iwxyburrb9lvw1wn = r57ub631wv8bvel5log2ih.parse_args(fx9ybska466d8s1fbqeii3)
    if mlfvs0iwxyburrb9lvw1wn.command == 'install':
        return l6qzhh8lg37slprr6qlspx(a1hgd3vvpu23u2r558mo9o=mlfvs0iwxyburrb9lvw1wn.force)
    return u6sebo359x76b6gyf3tfsk(vy1hp2d2io3kw52ke34upg=mlfvs0iwxyburrb9lvw1wn.bind, ohib62281lemaltdamtrs5=mlfvs0iwxyburrb9lvw1wn.port, kwif1wx8ucikekjcsuldk5=mlfvs0iwxyburrb9lvw1wn.watch_interval)
if __name__ == '__main__':
    sys.exit(lq86yd54cjujjs4339ia59())
