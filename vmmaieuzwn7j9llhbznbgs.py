import base64
import hashlib
import json
import locale
import os
import platform
import re
import shutil
import signal
import struct
import subprocess
import sys
import threading
import zlib
from datetime import datetime, timezone
from pathlib import Path
SERVER_NAME = 'muse-terminal-commander'
SERVER_VERSION = '0.1.0'
PROTOCOL_VERSION = '2025-06-18'
MAX_READ_BYTES = 1048576
MAX_OUTPUT_BYTES = 65536
DEFAULT_COMMAND_TIMEOUT = 120
MAX_COMMAND_TIMEOUT = 600
MAX_SEARCH_RESULTS = 200
MAX_AUDIT_LOG_BYTES = 10485760

class qxik4i1ab3x3aozq5e8hyt(Exception):
    pass

def qeryeatm67mrkq1vend81c():
    agd5tdiq1wkiimlh089udz = os.environ.get('MUSE_COMMANDER_CONFIG')
    if agd5tdiq1wkiimlh089udz:
        return Path(agd5tdiq1wkiimlh089udz).expanduser()
    return Path.home() / '.config' / SERVER_NAME / 'config.json'

def ipb8ci0xyj9gp7zmvyadbo():
    return os.path.abspath(os.sep)

def ccu987fkkysx5o15pmtwfk():
    oz4ex7z5ehqqxncdbd44dr = {'allowed_directories': [ipb8ci0xyj9gp7zmvyadbo()], 'blocked_paths': [], 'blocked_command_patterns': [], 'command_timeout_seconds': DEFAULT_COMMAND_TIMEOUT, 'max_read_bytes': MAX_READ_BYTES, 'audit_log': str(Path.home() / '.local' / 'share' / SERVER_NAME / 'audit.log')}
    dsm5k9km53aj4z247pujud = qeryeatm67mrkq1vend81c()
    if dsm5k9km53aj4z247pujud.is_file():
        try:
            yokpzetgksx0v9pz2h1daw = json.loads(dsm5k9km53aj4z247pujud.read_text(encoding='utf-8'))
            if isinstance(yokpzetgksx0v9pz2h1daw, dict):
                oz4ex7z5ehqqxncdbd44dr.update(yokpzetgksx0v9pz2h1daw)
        except Exception:
            pass
    return oz4ex7z5ehqqxncdbd44dr
CONFIG = ccu987fkkysx5o15pmtwfk()

def rph6t2b4c5a50sh3xwae3e(w1qf5oblmaw2vfh0tfbs3q):
    bp844183wpblxtwse5pzru = []
    for fjmpnjcjdjkzc6eabiixd6 in w1qf5oblmaw2vfh0tfbs3q or []:
        try:
            bp844183wpblxtwse5pzru.append(Path(os.path.expanduser(fjmpnjcjdjkzc6eabiixd6)).resolve())
        except Exception:
            continue
    return bp844183wpblxtwse5pzru

def b43pwr9dw5rarft7wgk814(mo0o1xxu567hpx01ofuscr):
    wqlq7qrt895fn4kvuggmtd = Path(os.path.expanduser(mo0o1xxu567hpx01ofuscr)).resolve()
    b3yz1ydakq3l6v5yfcgx00 = False
    for vtna1na2vwi1h6cb6t2pgw in rph6t2b4c5a50sh3xwae3e(CONFIG['allowed_directories']):
        try:
            wqlq7qrt895fn4kvuggmtd.relative_to(vtna1na2vwi1h6cb6t2pgw)
            b3yz1ydakq3l6v5yfcgx00 = True
            break
        except ValueError:
            continue
    if not b3yz1ydakq3l6v5yfcgx00:
        raise qxik4i1ab3x3aozq5e8hyt('caminho fora do escopo permitido: %s' % wqlq7qrt895fn4kvuggmtd)
    for z7ugujkgfbzdf324av5pm5 in rph6t2b4c5a50sh3xwae3e(CONFIG.get('blocked_paths', [])):
        try:
            wqlq7qrt895fn4kvuggmtd.relative_to(z7ugujkgfbzdf324av5pm5)
            raise qxik4i1ab3x3aozq5e8hyt('caminho bloqueado pela configuracao: %s' % wqlq7qrt895fn4kvuggmtd)
        except ValueError:
            continue
    return wqlq7qrt895fn4kvuggmtd

def luzso6wcodee5z4cdau6ld(pi7hhom0vgelmit586ebqr, jew2kgji45p336vd53gy43, dzytl9zhmodgp0z7twekw1, bdk4vml2068pghpgb0dnv7=1):
    try:
        k7ngkhklmcq6nph4fqytyp = int(pi7hhom0vgelmit586ebqr)
    except (TypeError, ValueError):
        return jew2kgji45p336vd53gy43
    if k7ngkhklmcq6nph4fqytyp < bdk4vml2068pghpgb0dnv7:
        return jew2kgji45p336vd53gy43
    return min(k7ngkhklmcq6nph4fqytyp, dzytl9zhmodgp0z7twekw1)

def cr2qu1uhln4t1n5dwt8vdm():
    return luzso6wcodee5z4cdau6ld(CONFIG.get('max_read_bytes', MAX_READ_BYTES), MAX_READ_BYTES, MAX_READ_BYTES)

def am2lity5ynwqh4swnl8y6j(voazajhcidfyekth31dn6f):
    px8tv25acljvtccu3i4vdz = luzso6wcodee5z4cdau6ld(CONFIG.get('command_timeout_seconds', DEFAULT_COMMAND_TIMEOUT), DEFAULT_COMMAND_TIMEOUT, MAX_COMMAND_TIMEOUT)
    return luzso6wcodee5z4cdau6ld(voazajhcidfyekth31dn6f if voazajhcidfyekth31dn6f is not None else px8tv25acljvtccu3i4vdz, px8tv25acljvtccu3i4vdz, MAX_COMMAND_TIMEOUT)

def lqj8x429i9m0d4t48mub7p(jml5jawelpnol1dgy2uuav, yhqwygeprd96sr0v8b907y, hbhet1ta86vx46ffj7vdhq=0):
    with open(jml5jawelpnol1dgy2uuav, 'rb') as kdnby02otv5l4go486v2wp:
        if hbhet1ta86vx46ffj7vdhq:
            kdnby02otv5l4go486v2wp.seek(hbhet1ta86vx46ffj7vdhq)
        ee7adut3xl1p6p2iktlukc = kdnby02otv5l4go486v2wp.read(yhqwygeprd96sr0v8b907y + 1)
    return (ee7adut3xl1p6p2iktlukc[:yhqwygeprd96sr0v8b907y], len(ee7adut3xl1p6p2iktlukc) > yhqwygeprd96sr0v8b907y)

def tst0zn7l94nw1xzfprnhl7(if1hrkat27v49lcz4v81z9, ekvd7g0fqg52czguvlxc8h):
    vd2z41cekowsuhziqnq5a0 = if1hrkat27v49lcz4v81z9.encode('utf-8', errors='replace')
    if len(vd2z41cekowsuhziqnq5a0) <= ekvd7g0fqg52czguvlxc8h:
        return (if1hrkat27v49lcz4v81z9, False)
    return (vd2z41cekowsuhziqnq5a0[:ekvd7g0fqg52czguvlxc8h].decode('utf-8', errors='ignore'), True)

def dhqoy4u44wcqwe6la8nzn2(cf4gcurwlr7zhb7r4qm44l):
    if not cf4gcurwlr7zhb7r4qm44l:
        return ''
    if isinstance(cf4gcurwlr7zhb7r4qm44l, str):
        return cf4gcurwlr7zhb7r4qm44l
    for m0c1k276auwf3w6lhb58m3 in ('utf-8', locale.getpreferredencoding(False) or 'utf-8', 'cp1252', 'cp850', 'latin-1'):
        try:
            return cf4gcurwlr7zhb7r4qm44l.decode(m0c1k276auwf3w6lhb58m3)
        except (UnicodeDecodeError, LookupError):
            continue
    return cf4gcurwlr7zhb7r4qm44l.decode('latin-1', errors='replace')

def w7t27t98j1w1o444e25cpf(oyokhh66dcgkvd5h4d5dq6, nsziwkh7v1yt2nr5hxienv, pufjzw6rwsf61uv5jq3jbx=MAX_SEARCH_RESULTS):
    return luzso6wcodee5z4cdau6ld(oyokhh66dcgkvd5h4d5dq6 if oyokhh66dcgkvd5h4d5dq6 is not None else nsziwkh7v1yt2nr5hxienv, nsziwkh7v1yt2nr5hxienv, pufjzw6rwsf61uv5jq3jbx)

def e4ub0mew07jvsx8lh9hp2z():
    return luzso6wcodee5z4cdau6ld(CONFIG.get('audit_log_max_bytes', MAX_AUDIT_LOG_BYTES), MAX_AUDIT_LOG_BYTES, MAX_AUDIT_LOG_BYTES, 1024)

def k9bp7xl1f6uwf0568vj7f9():
    return Path(os.path.expanduser(CONFIG['audit_log']))
_AUDIT_LOCK = threading.Lock()
_AUDIT_LAST_HASH = None

def hu2gj0v0wzs529srig3rht(jm8704mr4p47wwpr9667p6):
    try:
        with jm8704mr4p47wwpr9667p6.open('rb') as be5mateg4wg5y4896envls:
            be5mateg4wg5y4896envls.seek(0, os.SEEK_END)
            ev6vb7findzy8wk59pwhpw = be5mateg4wg5y4896envls.tell()
            if ev6vb7findzy8wk59pwhpw == 0:
                return ''
            k5x8ftx1pni56rpl5398gl = min(ev6vb7findzy8wk59pwhpw, 8192)
            be5mateg4wg5y4896envls.seek(ev6vb7findzy8wk59pwhpw - k5x8ftx1pni56rpl5398gl)
            for guktwuuygp4mknkhebz181 in reversed(be5mateg4wg5y4896envls.read().splitlines()):
                guktwuuygp4mknkhebz181 = guktwuuygp4mknkhebz181.strip()
                if not guktwuuygp4mknkhebz181:
                    continue
                try:
                    s7pu4jcc13nwpdnvl3pbpy = json.loads(guktwuuygp4mknkhebz181.decode('utf-8')).get('hash')
                except Exception:
                    continue
                return s7pu4jcc13nwpdnvl3pbpy or ''
    except Exception:
        pass
    return ''

def nmixv3w3l02delmlzv9dhd(vum6412sew89jvvv42szyu, n102woehk8c3bng8exbj6l, mdttk1l2qh9nwp02r8lf7r, peh0ska138pex1967q43h7=None):
    global _AUDIT_LAST_HASH
    dsgsazf3v8sycwkpm15buc = {'ts': datetime.now(timezone.utc).isoformat(), 'tool': vum6412sew89jvvv42szyu, 'summary': n102woehk8c3bng8exbj6l, 'ok': mdttk1l2qh9nwp02r8lf7r}
    if peh0ska138pex1967q43h7:
        dsgsazf3v8sycwkpm15buc['error'] = str(peh0ska138pex1967q43h7)[:300]
    d0mj0xervfemara8bb966j = json.dumps(dsgsazf3v8sycwkpm15buc, ensure_ascii=False, sort_keys=True)
    with _AUDIT_LOCK:
        try:
            wcpjlzp8kjorx5hnu4aoxf = k9bp7xl1f6uwf0568vj7f9()
            wcpjlzp8kjorx5hnu4aoxf.parent.mkdir(parents=True, exist_ok=True)
            if _AUDIT_LAST_HASH is None:
                _AUDIT_LAST_HASH = hu2gj0v0wzs529srig3rht(wcpjlzp8kjorx5hnu4aoxf)
            if wcpjlzp8kjorx5hnu4aoxf.exists() and wcpjlzp8kjorx5hnu4aoxf.stat().st_size >= e4ub0mew07jvsx8lh9hp2z():
                xd1htu9eae1ahvxs9ysc8g(wcpjlzp8kjorx5hnu4aoxf)
            p8shzgugkj57v20urjsc5r = _AUDIT_LAST_HASH
            gzujjjtual302vfgr08zw0 = hashlib.sha256((p8shzgugkj57v20urjsc5r + '|' + d0mj0xervfemara8bb966j).encode('utf-8')).hexdigest()
            bh1fhvb4ihe2qn9gk79ngx = dict(dsgsazf3v8sycwkpm15buc, prev_hash=p8shzgugkj57v20urjsc5r, hash=gzujjjtual302vfgr08zw0)
            with wcpjlzp8kjorx5hnu4aoxf.open('a', encoding='utf-8') as u5xrxm5z08kzsej1o5bnha:
                u5xrxm5z08kzsej1o5bnha.write(json.dumps(bh1fhvb4ihe2qn9gk79ngx, ensure_ascii=False) + '\n')
            _AUDIT_LAST_HASH = gzujjjtual302vfgr08zw0
        except Exception:
            pass

def xd1htu9eae1ahvxs9ysc8g(xw2rz11tlml84wyp0gtqny):
    global _AUDIT_LAST_HASH
    try:
        kokwdjk5on60xdyvg1rplc = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')
        q7gc2inzxevlsb5233eosh = xw2rz11tlml84wyp0gtqny.with_name('%s.%s.bak' % (xw2rz11tlml84wyp0gtqny.name, kokwdjk5on60xdyvg1rplc))
        os.replace(xw2rz11tlml84wyp0gtqny, q7gc2inzxevlsb5233eosh)
        zqiq1sloubw1v4nqhr3ft4 = _AUDIT_LAST_HASH if _AUDIT_LAST_HASH else hu2gj0v0wzs529srig3rht(q7gc2inzxevlsb5233eosh)
        xw2rz11tlml84wyp0gtqny.with_suffix('.anchor').write_text(json.dumps({'rotated_at': kokwdjk5on60xdyvg1rplc, 'file': q7gc2inzxevlsb5233eosh.name, 'hash': zqiq1sloubw1v4nqhr3ft4}), encoding='utf-8')
        _AUDIT_LAST_HASH = zqiq1sloubw1v4nqhr3ft4
    except Exception:
        pass

def sousn8nglijzqf4oy81c7t():
    try:
        return json.loads(k9bp7xl1f6uwf0568vj7f9().with_suffix('.anchor').read_text(encoding='utf-8')).get('hash', '')
    except Exception:
        return ''

def v03qkdw13q1iedw6mc50ae():
    nug3liun55e0grkb9iopoc = k9bp7xl1f6uwf0568vj7f9()
    try:
        miyoplfwfchgr3fl5gnrxy = [kwnrnc11bzquqlpa76pax6 for kwnrnc11bzquqlpa76pax6 in nug3liun55e0grkb9iopoc.read_text(encoding='utf-8').splitlines() if kwnrnc11bzquqlpa76pax6.strip()]
    except FileNotFoundError:
        return {'entries': 0, 'legacy': 0, 'valid': True, 'broken_at': None}
    k04z8v0w4hcyudxm5kj0u7 = z1nbzclaltbzu06504yael = 0
    h3oxnl8hylym1c86fcymso = sousn8nglijzqf4oy81c7t()
    for sqxuczwro567l8avyt076t, ifzu50ip8egsu702mjvuf8 in enumerate(miyoplfwfchgr3fl5gnrxy):
        try:
            g4l3p9nnped0fqhwiy2v8f = json.loads(ifzu50ip8egsu702mjvuf8)
        except Exception:
            return {'entries': k04z8v0w4hcyudxm5kj0u7, 'legacy': z1nbzclaltbzu06504yael, 'valid': False, 'broken_at': sqxuczwro567l8avyt076t}
        if 'hash' not in g4l3p9nnped0fqhwiy2v8f:
            z1nbzclaltbzu06504yael += 1
            continue
        k04z8v0w4hcyudxm5kj0u7 += 1
        qzon7b14r04uyrepw5o9c6 = {zyil609tc6l3gwzmcpjyh5: bshi4vax063suq8lem3vy2 for zyil609tc6l3gwzmcpjyh5, bshi4vax063suq8lem3vy2 in g4l3p9nnped0fqhwiy2v8f.items() if zyil609tc6l3gwzmcpjyh5 not in ('prev_hash', 'hash')}
        xji909jx5utb1qwfto5l8c = json.dumps(qzon7b14r04uyrepw5o9c6, ensure_ascii=False, sort_keys=True)
        ouz4cxta8i2zbztqm5p4qi = hashlib.sha256(((g4l3p9nnped0fqhwiy2v8f.get('prev_hash') or '') + '|' + xji909jx5utb1qwfto5l8c).encode('utf-8')).hexdigest()
        if g4l3p9nnped0fqhwiy2v8f.get('prev_hash') != h3oxnl8hylym1c86fcymso or g4l3p9nnped0fqhwiy2v8f['hash'] != ouz4cxta8i2zbztqm5p4qi:
            return {'entries': k04z8v0w4hcyudxm5kj0u7, 'legacy': z1nbzclaltbzu06504yael, 'valid': False, 'broken_at': sqxuczwro567l8avyt076t}
        h3oxnl8hylym1c86fcymso = g4l3p9nnped0fqhwiy2v8f['hash']
    return {'entries': k04z8v0w4hcyudxm5kj0u7, 'legacy': z1nbzclaltbzu06504yael, 'valid': True, 'broken_at': None}

def f20fqy37s9juxubprzj97g(ph8fksfpkyh69cixb6y8ip):
    return v03qkdw13q1iedw6mc50ae()

def z0gvqh4wltfh0shi0wxzug(wzvakusf6sf9xn2ztzyv4n, ska82kzmzxud66c14doc5p):
    if not isinstance(ska82kzmzxud66c14doc5p, dict):
        raise qxik4i1ab3x3aozq5e8hyt('argumentos devem ser um objeto')
    yxf1izfh2jczbw7q6cvicl = wzvakusf6sf9xn2ztzyv4n or {}
    for zr09wwenlnxtf46rotz85w in yxf1izfh2jczbw7q6cvicl.get('required') or []:
        if zr09wwenlnxtf46rotz85w not in ska82kzmzxud66c14doc5p:
            raise qxik4i1ab3x3aozq5e8hyt('argumento obrigatorio faltando: %s' % zr09wwenlnxtf46rotz85w)
    t02wibc03ddhbgpazbtmms = yxf1izfh2jczbw7q6cvicl.get('properties') or {}
    for zr09wwenlnxtf46rotz85w, r0bu6bqzby0wd7u1wz68cy in ska82kzmzxud66c14doc5p.items():
        lw0770d8wb4yf9ai5wybn7 = t02wibc03ddhbgpazbtmms.get(zr09wwenlnxtf46rotz85w)
        if lw0770d8wb4yf9ai5wybn7 is None:
            continue
        pbgvxg3seda7vjmx4flazi = lw0770d8wb4yf9ai5wybn7.get('type')
        o43odwz3l2l4qy7ykalnl1 = pbgvxg3seda7vjmx4flazi == 'string' and isinstance(r0bu6bqzby0wd7u1wz68cy, str) or (pbgvxg3seda7vjmx4flazi == 'integer' and isinstance(r0bu6bqzby0wd7u1wz68cy, int) and (not isinstance(r0bu6bqzby0wd7u1wz68cy, bool))) or (pbgvxg3seda7vjmx4flazi == 'number' and isinstance(r0bu6bqzby0wd7u1wz68cy, (int, float)) and (not isinstance(r0bu6bqzby0wd7u1wz68cy, bool))) or (pbgvxg3seda7vjmx4flazi == 'boolean' and isinstance(r0bu6bqzby0wd7u1wz68cy, bool)) or (pbgvxg3seda7vjmx4flazi == 'array' and isinstance(r0bu6bqzby0wd7u1wz68cy, list)) or (pbgvxg3seda7vjmx4flazi == 'object' and isinstance(r0bu6bqzby0wd7u1wz68cy, dict))
        if pbgvxg3seda7vjmx4flazi and (not o43odwz3l2l4qy7ykalnl1):
            raise qxik4i1ab3x3aozq5e8hyt("argumento '%s' deve ser do tipo %s" % (zr09wwenlnxtf46rotz85w, pbgvxg3seda7vjmx4flazi))

def d6c75kdary4s7xrjt1urts(ds5vme8ak4qzhpipm36nju, khh12pn0nguibkqsigo98p):
    for jxjx0ee2fsrt3jsxgy4bm9 in TOOLS:
        if jxjx0ee2fsrt3jsxgy4bm9['name'] == ds5vme8ak4qzhpipm36nju:
            z0gvqh4wltfh0shi0wxzug(jxjx0ee2fsrt3jsxgy4bm9['inputSchema'], khh12pn0nguibkqsigo98p)
            return

def u80goaskoj8e27atqr675j(mgw8uxts6rc9a0s3hp8wd7=None):
    if mgw8uxts6rc9a0s3hp8wd7:
        return Path(os.path.expanduser(mgw8uxts6rc9a0s3hp8wd7))
    if CONFIG.get('baseline_path'):
        return Path(os.path.expanduser(CONFIG['baseline_path']))
    return qeryeatm67mrkq1vend81c().parent / 'baseline.json'

def t2wripfgch6rm5jwkpftpc(gfym7b3om8eonwg00qeqcc):
    xbkkd22iek300gjdf0ltlc = hashlib.sha256()
    with open(gfym7b3om8eonwg00qeqcc, 'rb') as t5dk3fvn9o91rt4gl2xxk6:
        for mbir3loygy6w60crro89f8 in iter(lambda: t5dk3fvn9o91rt4gl2xxk6.read(1048576), b''):
            xbkkd22iek300gjdf0ltlc.update(mbir3loygy6w60crro89f8)
    return xbkkd22iek300gjdf0ltlc.hexdigest()

def meu3akrj789y6q5shdzp0c(p53psn54waip33tut0hxow):
    os613dnpj8l7tel4dlcww1 = {}
    if p53psn54waip33tut0hxow.is_file():
        v4k2iot7hy3rp10uqpudec = [p53psn54waip33tut0hxow]
    else:
        v4k2iot7hy3rp10uqpudec = sorted((s6dddcbkbj4543an8yxqrj for s6dddcbkbj4543an8yxqrj in p53psn54waip33tut0hxow.rglob('*') if s6dddcbkbj4543an8yxqrj.is_file()))
    for t9oqb48qxin570cl9nhtgg in v4k2iot7hy3rp10uqpudec:
        try:
            os613dnpj8l7tel4dlcww1[str(t9oqb48qxin570cl9nhtgg)] = {'sha256': t2wripfgch6rm5jwkpftpc(t9oqb48qxin570cl9nhtgg), 'size': t9oqb48qxin570cl9nhtgg.stat().st_size}
        except Exception:
            continue
    return os613dnpj8l7tel4dlcww1

def o60pr57idppyajlhs03331():
    yw3j8317jlrk84zi2skzan = set()
    try:
        if os.name == 'nt':
            sh283r48owlayxoqslcktm = subprocess.run(['tasklist', '/FO', 'CSV', '/NH'], capture_output=True, timeout=30)
            for rxbxqx2nbvlcxun3vwsxmp in dhqoy4u44wcqwe6la8nzn2(sh283r48owlayxoqslcktm.stdout).splitlines():
                cejlw75p3yvqa4uc1xq5op = rxbxqx2nbvlcxun3vwsxmp.split('","')
                if cejlw75p3yvqa4uc1xq5op:
                    yw3j8317jlrk84zi2skzan.add(cejlw75p3yvqa4uc1xq5op[0].strip('"').strip().lower())
        else:
            sh283r48owlayxoqslcktm = subprocess.run(['ps', '-eo', 'comm='], capture_output=True, timeout=30)
            for rxbxqx2nbvlcxun3vwsxmp in dhqoy4u44wcqwe6la8nzn2(sh283r48owlayxoqslcktm.stdout).splitlines():
                rxbxqx2nbvlcxun3vwsxmp = rxbxqx2nbvlcxun3vwsxmp.strip()
                if rxbxqx2nbvlcxun3vwsxmp:
                    yw3j8317jlrk84zi2skzan.add(rxbxqx2nbvlcxun3vwsxmp.lower())
    except Exception:
        pass
    return sorted((cvh36vbdpwf4jxeug2rqxd for cvh36vbdpwf4jxeug2rqxd in yw3j8317jlrk84zi2skzan if cvh36vbdpwf4jxeug2rqxd))

def uhuclyznb5kgv29kk8xi9p(vylan2h88e79jo0ncv5az9):
    ys6j2yp1var97mt9jwjkqg = vylan2h88e79jo0ncv5az9.get('paths') or [str(Path(__file__).resolve().parent)]
    x23ulenbo3fy4or2ko9u5r = [b43pwr9dw5rarft7wgk814(str(ynhm57iltlugw7tpbr7x65)) for ynhm57iltlugw7tpbr7x65 in ys6j2yp1var97mt9jwjkqg]
    nal19w5tjstcaqyci6nw4c = {}
    for u5gfpky2xi3nqi4s0x5l90 in x23ulenbo3fy4or2ko9u5r:
        nal19w5tjstcaqyci6nw4c.update(meu3akrj789y6q5shdzp0c(u5gfpky2xi3nqi4s0x5l90))
    dflum2mtg4zmyoq1bfpvrm = {'name': vylan2h88e79jo0ncv5az9.get('name', 'default'), 'created': datetime.now(timezone.utc).isoformat(), 'host': platform.node(), 'system': '%s %s' % (platform.system(), platform.release()), 'roots': [str(thdyosk2mxzzld584rn8g4) for thdyosk2mxzzld584rn8g4 in x23ulenbo3fy4or2ko9u5r], 'files': nal19w5tjstcaqyci6nw4c, 'processes': o60pr57idppyajlhs03331()}
    ygldwdva56k399p45pweb2 = u80goaskoj8e27atqr675j(vylan2h88e79jo0ncv5az9.get('baseline_path'))
    ygldwdva56k399p45pweb2.parent.mkdir(parents=True, exist_ok=True)
    ygldwdva56k399p45pweb2.write_text(json.dumps(dflum2mtg4zmyoq1bfpvrm, ensure_ascii=False, indent=1), encoding='utf-8')
    return {'path': str(ygldwdva56k399p45pweb2), 'name': dflum2mtg4zmyoq1bfpvrm['name'], 'files': len(nal19w5tjstcaqyci6nw4c), 'processes': len(dflum2mtg4zmyoq1bfpvrm['processes']), 'created': dflum2mtg4zmyoq1bfpvrm['created']}

def jse02550lk0v9ge2rtif95(pxut2als0rl8opzx3l09ln):
    zlpqnkgaky1akgn1ci35ww = u80goaskoj8e27atqr675j(pxut2als0rl8opzx3l09ln.get('baseline_path'))
    try:
        xunhh6byyzllqrxedl4cjv = json.loads(zlpqnkgaky1akgn1ci35ww.read_text(encoding='utf-8'))
    except FileNotFoundError:
        raise qxik4i1ab3x3aozq5e8hyt('baseline nao encontrada: rode capture_baseline primeiro')
    d14xp1r1mou0uuyy89cenm = {}
    for x6iqmsffg5qnggsd0y1rsl in xunhh6byyzllqrxedl4cjv.get('roots', []):
        iohjaq01rq3l9a29eqbk2f = Path(x6iqmsffg5qnggsd0y1rsl)
        if iohjaq01rq3l9a29eqbk2f.exists():
            d14xp1r1mou0uuyy89cenm.update(meu3akrj789y6q5shdzp0c(iohjaq01rq3l9a29eqbk2f))
    ts6yftb91vunga5k4itgez = xunhh6byyzllqrxedl4cjv.get('files', {})
    j3eklqmkk2ux20r6e07jp7 = sorted((lu655bkmmw6frtmwrzdiwu for lu655bkmmw6frtmwrzdiwu in ts6yftb91vunga5k4itgez if lu655bkmmw6frtmwrzdiwu in d14xp1r1mou0uuyy89cenm and d14xp1r1mou0uuyy89cenm[lu655bkmmw6frtmwrzdiwu]['sha256'] != ts6yftb91vunga5k4itgez[lu655bkmmw6frtmwrzdiwu]['sha256']))
    jh3966vonpv7vgdybr2lvg = sorted((ovgba40yoye407alfhb8vj for ovgba40yoye407alfhb8vj in ts6yftb91vunga5k4itgez if ovgba40yoye407alfhb8vj not in d14xp1r1mou0uuyy89cenm))
    q47n4xoza1rriepuu1kvt8 = sorted((mcq4e9z4zhs32rlqfpg4wt for mcq4e9z4zhs32rlqfpg4wt in d14xp1r1mou0uuyy89cenm if mcq4e9z4zhs32rlqfpg4wt not in ts6yftb91vunga5k4itgez))
    vmzl15vy1axn23t9hvig6v = set(o60pr57idppyajlhs03331())
    lq3p8anjdc6uv2zus1yo8e = set(xunhh6byyzllqrxedl4cjv.get('processes', []))
    return {'valid': not (j3eklqmkk2ux20r6e07jp7 or jh3966vonpv7vgdybr2lvg or q47n4xoza1rriepuu1kvt8), 'baseline_created': xunhh6byyzllqrxedl4cjv.get('created'), 'files_changed': j3eklqmkk2ux20r6e07jp7, 'files_missing': jh3966vonpv7vgdybr2lvg, 'files_added': q47n4xoza1rriepuu1kvt8, 'processes_new': sorted(vmzl15vy1axn23t9hvig6v - lq3p8anjdc6uv2zus1yo8e), 'processes_gone': sorted(lq3p8anjdc6uv2zus1yo8e - vmzl15vy1axn23t9hvig6v)}

def jwhqegqhu9qycdeuqh8x4x(yc749vgpj3gqmt7q0eoi12, n192fbkdw0irdjfuz5htny):
    if yc749vgpj3gqmt7q0eoi12 == 'write_file':
        return {'path': n192fbkdw0irdjfuz5htny.get('path'), 'content_bytes': len(n192fbkdw0irdjfuz5htny.get('content', ''))}
    if yc749vgpj3gqmt7q0eoi12 == 'edit_file':
        return {'path': n192fbkdw0irdjfuz5htny.get('path'), 'old_text_chars': len(n192fbkdw0irdjfuz5htny.get('old_text', ''))}
    return dict(n192fbkdw0irdjfuz5htny)

def kgukosv3qx4hz9dh1ihube(xf3ac490hn5pl3tvmimh7k):
    pzbfj4gllgilcvvq43y826 = b43pwr9dw5rarft7wgk814(xf3ac490hn5pl3tvmimh7k['path'])
    if not pzbfj4gllgilcvvq43y826.is_file():
        raise qxik4i1ab3x3aozq5e8hyt('arquivo nao encontrado: %s' % pzbfj4gllgilcvvq43y826)
    dcib9lsr9abju3zxknif46 = pzbfj4gllgilcvvq43y826.stat().st_size
    hdcwcrcc3nur3f9yxlxfyh = cr2qu1uhln4t1n5dwt8vdm()
    ifkrv6r4ost3rv7te265jw = luzso6wcodee5z4cdau6ld(xf3ac490hn5pl3tvmimh7k.get('limit', hdcwcrcc3nur3f9yxlxfyh), hdcwcrcc3nur3f9yxlxfyh, MAX_READ_BYTES)
    hgreuqzl979axoh1q2gn6a = xf3ac490hn5pl3tvmimh7k.get('offset', 0)
    if not isinstance(hgreuqzl979axoh1q2gn6a, int) or isinstance(hgreuqzl979axoh1q2gn6a, bool) or hgreuqzl979axoh1q2gn6a < 0:
        raise qxik4i1ab3x3aozq5e8hyt('offset deve ser um inteiro >= 0')
    if hgreuqzl979axoh1q2gn6a > dcib9lsr9abju3zxknif46:
        hgreuqzl979axoh1q2gn6a = dcib9lsr9abju3zxknif46
    u8z3vc1f09atrkmrkdupuv, pxdpi0vxjuzzx7ffy3wj2k = lqj8x429i9m0d4t48mub7p(pzbfj4gllgilcvvq43y826, ifkrv6r4ost3rv7te265jw, hgreuqzl979axoh1q2gn6a)
    return {'path': str(pzbfj4gllgilcvvq43y826), 'content': u8z3vc1f09atrkmrkdupuv.decode('utf-8', errors='replace'), 'bytes': dcib9lsr9abju3zxknif46, 'offset': hgreuqzl979axoh1q2gn6a, 'next_offset': hgreuqzl979axoh1q2gn6a + len(u8z3vc1f09atrkmrkdupuv) if pxdpi0vxjuzzx7ffy3wj2k else None, 'truncated': pxdpi0vxjuzzx7ffy3wj2k}
_LOG_TS_PATTERNS = [('iso8601', re.compile('\\d{4}-\\d{2}-\\d{2}[T ]\\d{2}:\\d{2}:\\d{2}')), ('apache', re.compile('\\d{2}/[A-Za-z]{3}/\\d{4}:\\d{2}:\\d{2}:\\d{2}')), ('epoch_ms', re.compile('\\b1[0-9]{12}\\b')), ('epoch_s', re.compile('\\b1[0-9]{9}\\b')), ('hora', re.compile('\\b\\d{2}:\\d{2}:\\d{2}\\b'))]

def w73crvscom12eq7emuodf2(p94en7o7sft056h04vvce4):
    ma0qpbb8xnjoe8z4cmxucj = 0
    s9jhgicbkcun2113emmai5 = b''
    szr7a57ei2c038cxahuva6 = False
    with open(p94en7o7sft056h04vvce4, 'rb') as w84bas9opo9w9i843xnaw0:
        for pu2f5k51h5itd4dreo0n5t in iter(lambda: w84bas9opo9w9i843xnaw0.read(1048576), b''):
            szr7a57ei2c038cxahuva6 = True
            ma0qpbb8xnjoe8z4cmxucj += pu2f5k51h5itd4dreo0n5t.count(b'\n')
            s9jhgicbkcun2113emmai5 = pu2f5k51h5itd4dreo0n5t[-1:]
    if szr7a57ei2c038cxahuva6 and s9jhgicbkcun2113emmai5 != b'\n':
        ma0qpbb8xnjoe8z4cmxucj += 1
    return ma0qpbb8xnjoe8z4cmxucj
_IDENT_RE = re.compile('^[A-Za-z_][A-Za-z0-9_]*(\\s[A-Za-z_][A-Za-z0-9_ ]*)?$')

def ocf8chj5ypd0f3n70abug8(dq6yq0l6nd60yhdhxtkqws):
    return bool(dq6yq0l6nd60yhdhxtkqws) and all((_IDENT_RE.match(c22o62ut16odjsg9k0fb2a.strip().strip('"')) for c22o62ut16odjsg9k0fb2a in dq6yq0l6nd60yhdhxtkqws))

def reci56s279cy4e66jxzj80(se3bjtvtq50604w9pndxzy):
    jd1kyl9kiupik5ofji000i = b43pwr9dw5rarft7wgk814(se3bjtvtq50604w9pndxzy['path'])
    if not jd1kyl9kiupik5ofji000i.is_file():
        raise qxik4i1ab3x3aozq5e8hyt('arquivo nao encontrado: %s' % jd1kyl9kiupik5ofji000i)
    ivk31eanihhigh5g2vnmxu, vmgi29abksewzx00inuvfq = lqj8x429i9m0d4t48mub7p(jd1kyl9kiupik5ofji000i, 1048576)
    uuwomsxxf38p8qrkwx1gh3 = ivk31eanihhigh5g2vnmxu.decode('utf-8', errors='replace')
    jvuvjbpjxd56n2g131zkt1 = [rklr3lvkanbd47tx8af5fd for rklr3lvkanbd47tx8af5fd in uuwomsxxf38p8qrkwx1gh3.splitlines() if rklr3lvkanbd47tx8af5fd.strip()][:30]
    v1muzfbbvlvrigf0fccd6h, sovef4vomiazyxaikg8cua = (None, 0)
    for gvd8bicb8n2odmvu9ktrxg in [',', ';', '\t', '|']:
        idq3gp6m9t36n2vo88al6z = [len(rzgz9da2zyqwn1otf9klr2.split(gvd8bicb8n2odmvu9ktrxg)) for rzgz9da2zyqwn1otf9klr2 in jvuvjbpjxd56n2g131zkt1]
        if not idq3gp6m9t36n2vo88al6z:
            continue
        eowg0msbm8jbb0xpp7pz1d = max(set(idq3gp6m9t36n2vo88al6z), key=idq3gp6m9t36n2vo88al6z.count)
        if eowg0msbm8jbb0xpp7pz1d > 1:
            hvpjpbn825m6wrvih9h1p9 = idq3gp6m9t36n2vo88al6z.count(eowg0msbm8jbb0xpp7pz1d)
            if hvpjpbn825m6wrvih9h1p9 > sovef4vomiazyxaikg8cua:
                v1muzfbbvlvrigf0fccd6h, sovef4vomiazyxaikg8cua = (gvd8bicb8n2odmvu9ktrxg, hvpjpbn825m6wrvih9h1p9)
    hl6ru55c5ghkyeyjrpygdf = None
    hrcjjtcvo2ptxeix8y2fju = False
    if v1muzfbbvlvrigf0fccd6h and len(jvuvjbpjxd56n2g131zkt1) >= 2:
        xyq9a8smfhbfo3sw2p8uvk = [cocovibg97uh8r7qowdass.strip() for cocovibg97uh8r7qowdass in jvuvjbpjxd56n2g131zkt1[0].split(v1muzfbbvlvrigf0fccd6h)]
        nk8tuqi858ij3zkyjjogp4 = [ulklheklu9w4ajq8gju0nw.strip() for ulklheklu9w4ajq8gju0nw in jvuvjbpjxd56n2g131zkt1[1].split(v1muzfbbvlvrigf0fccd6h)]
        if len(xyq9a8smfhbfo3sw2p8uvk) == len(nk8tuqi858ij3zkyjjogp4) and ocf8chj5ypd0f3n70abug8(xyq9a8smfhbfo3sw2p8uvk) and (not ocf8chj5ypd0f3n70abug8(nk8tuqi858ij3zkyjjogp4)):
            hrcjjtcvo2ptxeix8y2fju = True
            hl6ru55c5ghkyeyjrpygdf = [p046mah7yx5w0b8zvenw63[:100] for p046mah7yx5w0b8zvenw63 in xyq9a8smfhbfo3sw2p8uvk]
    kr7uk4ngrie6iz2yskfdzl = None
    for zfn0bb8p4imqvw78psmf66, d3nw6nn0b62e7y97mc39ah in _LOG_TS_PATTERNS:
        if any((d3nw6nn0b62e7y97mc39ah.search(w2yp1gjlhcmi3edg9kz06r) for w2yp1gjlhcmi3edg9kz06r in jvuvjbpjxd56n2g131zkt1[:10])):
            kr7uk4ngrie6iz2yskfdzl = zfn0bb8p4imqvw78psmf66
            break
    return {'path': str(jd1kyl9kiupik5ofji000i), 'bytes': jd1kyl9kiupik5ofji000i.stat().st_size, 'total_lines': w73crvscom12eq7emuodf2(jd1kyl9kiupik5ofji000i), 'delimiter': v1muzfbbvlvrigf0fccd6h, 'has_header': hrcjjtcvo2ptxeix8y2fju, 'fields': hl6ru55c5ghkyeyjrpygdf, 'timestamp_format': kr7uk4ngrie6iz2yskfdzl, 'sample_lines': [c7ax9ygfrb1y1zcn89657f[:200] for c7ax9ygfrb1y1zcn89657f in jvuvjbpjxd56n2g131zkt1[:3]]}

def njy64jgrk8ufmfnw7ig3bo(ewi4839wavc6b8wpexjj6l):
    gtq0w85u2a5qw2jjp4no7n = b43pwr9dw5rarft7wgk814(ewi4839wavc6b8wpexjj6l['path'])
    gtq0w85u2a5qw2jjp4no7n.parent.mkdir(parents=True, exist_ok=True)
    x9ox7f7ymt8bmhpg80qx7c = ewi4839wavc6b8wpexjj6l.get('content', '')
    gtq0w85u2a5qw2jjp4no7n.write_text(x9ox7f7ymt8bmhpg80qx7c, encoding='utf-8')
    return {'path': str(gtq0w85u2a5qw2jjp4no7n), 'bytes': len(x9ox7f7ymt8bmhpg80qx7c.encode('utf-8'))}

def rt63u7hflbfe2rcitimsxh(nqksfy0sy2hx5aksx2m8ak):
    nq0cgwf3sp5rarj4isi9zr = b43pwr9dw5rarft7wgk814(nqksfy0sy2hx5aksx2m8ak['path'])
    if not nq0cgwf3sp5rarj4isi9zr.is_file():
        raise qxik4i1ab3x3aozq5e8hyt('arquivo nao encontrado: %s' % nq0cgwf3sp5rarj4isi9zr)
    pcslk4eieme34z5pco3l6z = nq0cgwf3sp5rarj4isi9zr.read_text(encoding='utf-8')
    piculw0kpudow3fxutqmyz = nqksfy0sy2hx5aksx2m8ak['old_text']
    o7ra2xno0z1wxx5uvtmv34 = nqksfy0sy2hx5aksx2m8ak['new_text']
    vquvn4svr241dx7pmh8cs6 = pcslk4eieme34z5pco3l6z.count(piculw0kpudow3fxutqmyz)
    if vquvn4svr241dx7pmh8cs6 == 0:
        raise qxik4i1ab3x3aozq5e8hyt('trecho nao encontrado em %s' % nq0cgwf3sp5rarj4isi9zr)
    if vquvn4svr241dx7pmh8cs6 > 1 and (not nqksfy0sy2hx5aksx2m8ak.get('replace_all', False)):
        raise qxik4i1ab3x3aozq5e8hyt('trecho aparece %d vezes em %s; use replace_all=true ou seja mais especifico' % (vquvn4svr241dx7pmh8cs6, nq0cgwf3sp5rarj4isi9zr))
    pcslk4eieme34z5pco3l6z = pcslk4eieme34z5pco3l6z.replace(piculw0kpudow3fxutqmyz, o7ra2xno0z1wxx5uvtmv34) if nqksfy0sy2hx5aksx2m8ak.get('replace_all', False) else pcslk4eieme34z5pco3l6z.replace(piculw0kpudow3fxutqmyz, o7ra2xno0z1wxx5uvtmv34, 1)
    nq0cgwf3sp5rarj4isi9zr.write_text(pcslk4eieme34z5pco3l6z, encoding='utf-8')
    return {'path': str(nq0cgwf3sp5rarj4isi9zr), 'replacements': vquvn4svr241dx7pmh8cs6 if nqksfy0sy2hx5aksx2m8ak.get('replace_all', False) else 1}

def kbj4z7ltro39incsw6i9i2(rjf2pcetcvdlzc9sb0va75):
    uzv9afojc40vyfv4n8gnat = b43pwr9dw5rarft7wgk814(rjf2pcetcvdlzc9sb0va75['path'])
    if not uzv9afojc40vyfv4n8gnat.is_dir():
        raise qxik4i1ab3x3aozq5e8hyt('diretorio nao encontrado: %s' % uzv9afojc40vyfv4n8gnat)
    kqkud2h50pyhj3absfxl2r = []
    for llkd1esq7clywwe1mb7abi in sorted(uzv9afojc40vyfv4n8gnat.iterdir(), key=lambda m3ffmsf6qtnejsbky73efz: (not m3ffmsf6qtnejsbky73efz.is_dir(), m3ffmsf6qtnejsbky73efz.name.lower())):
        try:
            jospfamld0c2gdupa634j1 = llkd1esq7clywwe1mb7abi.stat()
            kqkud2h50pyhj3absfxl2r.append({'name': llkd1esq7clywwe1mb7abi.name, 'type': 'directory' if llkd1esq7clywwe1mb7abi.is_dir() else 'file', 'size': jospfamld0c2gdupa634j1.st_size if llkd1esq7clywwe1mb7abi.is_file() else None, 'modified': datetime.fromtimestamp(jospfamld0c2gdupa634j1.st_mtime, timezone.utc).isoformat()})
        except OSError:
            kqkud2h50pyhj3absfxl2r.append({'name': llkd1esq7clywwe1mb7abi.name, 'type': 'unknown', 'size': None, 'modified': None})
    return {'path': str(uzv9afojc40vyfv4n8gnat), 'entries': kqkud2h50pyhj3absfxl2r}

def y6snldqapfqd73iae0763j(yyqk3v7sqgw4c9yxbc2z35):
    z06raed1xpe171qfqv4h44 = b43pwr9dw5rarft7wgk814(yyqk3v7sqgw4c9yxbc2z35['path'])
    z06raed1xpe171qfqv4h44.mkdir(parents=True, exist_ok=True)
    return {'path': str(z06raed1xpe171qfqv4h44)}

def twpn10a1lcv6i9rvle6kvd(nnz992ltluu7t02mwi0agr):
    fer5u8bnoe5lyogzbp0zlh = b43pwr9dw5rarft7wgk814(nnz992ltluu7t02mwi0agr['source'])
    bq0ovrqik3twk4s142scg9 = b43pwr9dw5rarft7wgk814(nnz992ltluu7t02mwi0agr['destination'])
    if not fer5u8bnoe5lyogzbp0zlh.exists():
        raise qxik4i1ab3x3aozq5e8hyt('origem nao encontrada: %s' % fer5u8bnoe5lyogzbp0zlh)
    bq0ovrqik3twk4s142scg9.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(fer5u8bnoe5lyogzbp0zlh), str(bq0ovrqik3twk4s142scg9))
    return {'source': str(fer5u8bnoe5lyogzbp0zlh), 'destination': str(bq0ovrqik3twk4s142scg9)}

def mxsis6gdgwwruvufztjy2i(fpqo523ue035cdw3zfvwvw):
    jovh668yix68nctkmb8i11 = b43pwr9dw5rarft7wgk814(fpqo523ue035cdw3zfvwvw['path'])
    if not jovh668yix68nctkmb8i11.exists():
        raise qxik4i1ab3x3aozq5e8hyt('caminho nao encontrado: %s' % jovh668yix68nctkmb8i11)
    if str(jovh668yix68nctkmb8i11) == ipb8ci0xyj9gp7zmvyadbo():
        raise qxik4i1ab3x3aozq5e8hyt('recusado: apagar a raiz do sistema de arquivos')
    if jovh668yix68nctkmb8i11.is_dir() and (not jovh668yix68nctkmb8i11.is_symlink()):
        shutil.rmtree(jovh668yix68nctkmb8i11)
        return {'path': str(jovh668yix68nctkmb8i11), 'deleted': 'directory'}
    jovh668yix68nctkmb8i11.unlink()
    return {'path': str(jovh668yix68nctkmb8i11), 'deleted': 'file'}

def q6e0u6d0glt3u4e59qzqu4(gi3uxezztl1d5g74gca3br):
    sctrasdb2w2tmdic3hrwgb = b43pwr9dw5rarft7wgk814(gi3uxezztl1d5g74gca3br['root'])
    ghct4p8ypzro58vqj777ym = gi3uxezztl1d5g74gca3br['pattern']
    ty4ru18uewk2e3c3dngxpy = w7t27t98j1w1o444e25cpf(gi3uxezztl1d5g74gca3br.get('max_results'), 50)
    if not sctrasdb2w2tmdic3hrwgb.is_dir():
        raise qxik4i1ab3x3aozq5e8hyt('diretorio raiz nao encontrado: %s' % sctrasdb2w2tmdic3hrwgb)
    dmk0a8zqjk6gouhoduo2fa = []
    for vsjr3l6bumsheqdrfcpcgv in sctrasdb2w2tmdic3hrwgb.rglob(ghct4p8ypzro58vqj777ym):
        try:
            vsjr3l6bumsheqdrfcpcgv.resolve().relative_to(sctrasdb2w2tmdic3hrwgb)
        except ValueError:
            continue
        dmk0a8zqjk6gouhoduo2fa.append(str(vsjr3l6bumsheqdrfcpcgv))
        if len(dmk0a8zqjk6gouhoduo2fa) >= ty4ru18uewk2e3c3dngxpy:
            break
    return {'root': str(sctrasdb2w2tmdic3hrwgb), 'pattern': ghct4p8ypzro58vqj777ym, 'results': dmk0a8zqjk6gouhoduo2fa, 'count': len(dmk0a8zqjk6gouhoduo2fa)}

def lqrase7ifwnlrsmq3dk693(k8cgx6lo4zp1oi80uzgvvp):
    ppexe97jxa14ypm83wf1wb = b43pwr9dw5rarft7wgk814(k8cgx6lo4zp1oi80uzgvvp['path'])
    if not ppexe97jxa14ypm83wf1wb.exists():
        raise qxik4i1ab3x3aozq5e8hyt('caminho nao encontrado: %s' % ppexe97jxa14ypm83wf1wb)
    xjmqwn7rasptqsdww7hr1l = ppexe97jxa14ypm83wf1wb.stat()
    return {'path': str(ppexe97jxa14ypm83wf1wb), 'type': 'directory' if ppexe97jxa14ypm83wf1wb.is_dir() else 'file', 'size': xjmqwn7rasptqsdww7hr1l.st_size, 'mode': oct(xjmqwn7rasptqsdww7hr1l.st_mode & 4095), 'modified': datetime.fromtimestamp(xjmqwn7rasptqsdww7hr1l.st_mtime, timezone.utc).isoformat(), 'created': datetime.fromtimestamp(xjmqwn7rasptqsdww7hr1l.st_ctime, timezone.utc).isoformat()}

def quwjwayk9bu8bcrninwy68(bofjnpxhekrtt4fdi8c2be):
    for adpofe1rq4o6evx9hfvdkx in CONFIG.get('blocked_command_patterns', []):
        try:
            if re.search(adpofe1rq4o6evx9hfvdkx, bofjnpxhekrtt4fdi8c2be):
                raise qxik4i1ab3x3aozq5e8hyt('comando bloqueado pela politica: %s' % bofjnpxhekrtt4fdi8c2be[:120])
        except re.error:
            continue

def kegxr3enidt00yb5gohwjd(oyntzpmrfmjdb3bbt5k0c1):
    tyb54noaf9lsc22r315zcy = oyntzpmrfmjdb3bbt5k0c1['command']
    quwjwayk9bu8bcrninwy68(tyb54noaf9lsc22r315zcy)
    c07cyd00yhqcgiz1plscxj = None
    if oyntzpmrfmjdb3bbt5k0c1.get('cwd'):
        c07cyd00yhqcgiz1plscxj = b43pwr9dw5rarft7wgk814(oyntzpmrfmjdb3bbt5k0c1['cwd'])
        if not c07cyd00yhqcgiz1plscxj.is_dir():
            raise qxik4i1ab3x3aozq5e8hyt('cwd nao e um diretorio: %s' % c07cyd00yhqcgiz1plscxj)
    mmxdsug02m9cvdog5adj8d = am2lity5ynwqh4swnl8y6j(oyntzpmrfmjdb3bbt5k0c1.get('timeout'))
    try:
        foaqqk1c708qpgwc75f5d0 = subprocess.run(tyb54noaf9lsc22r315zcy, shell=True, cwd=str(c07cyd00yhqcgiz1plscxj) if c07cyd00yhqcgiz1plscxj else None, capture_output=True, timeout=mmxdsug02m9cvdog5adj8d)
    except subprocess.TimeoutExpired:
        raise qxik4i1ab3x3aozq5e8hyt('comando excedeu o timeout de %ds' % mmxdsug02m9cvdog5adj8d)
    benj54f0j4der8ehwx8jj9, xfx0589lts3r1ugpe2eg3a = tst0zn7l94nw1xzfprnhl7(dhqoy4u44wcqwe6la8nzn2(foaqqk1c708qpgwc75f5d0.stdout), MAX_OUTPUT_BYTES)
    tcadblys4qg8nfkd1r0tlr, twil0elkkvtvzjfmqw3h9o = tst0zn7l94nw1xzfprnhl7(dhqoy4u44wcqwe6la8nzn2(foaqqk1c708qpgwc75f5d0.stderr), MAX_OUTPUT_BYTES)
    return {'exit_code': foaqqk1c708qpgwc75f5d0.returncode, 'stdout': benj54f0j4der8ehwx8jj9, 'stderr': tcadblys4qg8nfkd1r0tlr, 'truncated': xfx0589lts3r1ugpe2eg3a or twil0elkkvtvzjfmqw3h9o}

def af6gpsk4y5qsiz08qp72eg(zqa2y9hx1chf3th7kpvwt6):
    ds4101n5jd97jpraw44pbe = []
    cvfqg5qd77ozg5jx39waxi = Path('/proc')
    if cvfqg5qd77ozg5jx39waxi.is_dir():
        for zls9jii44aloypg3z01eok in cvfqg5qd77ozg5jx39waxi.iterdir():
            if not zls9jii44aloypg3z01eok.name.isdigit():
                continue
            try:
                gl6kg10w81142etmeejuav = (zls9jii44aloypg3z01eok / 'stat').read_text()
                ilxhqmewa3dm2mzmq808k7, bjvz2debx3mcymk880vqhm, seuiqboi5warqfptk0wy3y = gl6kg10w81142etmeejuav.partition('(')
                mof52nlc09zh0520h8ijag, bjvz2debx3mcymk880vqhm, seuiqboi5warqfptk0wy3y = seuiqboi5warqfptk0wy3y.rpartition(')')
                vuqbbbpuhp611y70k3jc3m = seuiqboi5warqfptk0wy3y.split()
                qcnyhcucedhmozxiddbpga = vuqbbbpuhp611y70k3jc3m[0]
                u58jlcumj4nuch6kwk0y9a = int(vuqbbbpuhp611y70k3jc3m[1])
                a7fgz3skk75gtghe08ljm2 = ''
                try:
                    a7fgz3skk75gtghe08ljm2 = (zls9jii44aloypg3z01eok / 'cmdline').read_bytes().replace(b'\x00', b' ').decode('utf-8', errors='replace').strip()[:200]
                except OSError:
                    pass
                ds4101n5jd97jpraw44pbe.append({'pid': int(zls9jii44aloypg3z01eok.name), 'ppid': u58jlcumj4nuch6kwk0y9a, 'name': mof52nlc09zh0520h8ijag, 'state': qcnyhcucedhmozxiddbpga, 'cmdline': a7fgz3skk75gtghe08ljm2})
            except (OSError, ValueError):
                continue
    else:
        wbgk46c8ytfv0g501yh23t = dhqoy4u44wcqwe6la8nzn2(subprocess.run(['ps', '-eo', 'pid=,ppid=,comm='], capture_output=True, timeout=10).stdout)
        for ao0fa2ulike1r570exajfe in wbgk46c8ytfv0g501yh23t.splitlines():
            n13qb0ms4f48ekac4d96a2 = ao0fa2ulike1r570exajfe.split(None, 2)
            if len(n13qb0ms4f48ekac4d96a2) == 3:
                ds4101n5jd97jpraw44pbe.append({'pid': int(n13qb0ms4f48ekac4d96a2[0]), 'ppid': int(n13qb0ms4f48ekac4d96a2[1]), 'name': n13qb0ms4f48ekac4d96a2[2], 'state': '?', 'cmdline': n13qb0ms4f48ekac4d96a2[2]})
    ds4101n5jd97jpraw44pbe.sort(key=lambda qb1k8bhl7jjjh3gf9f3iwy: qb1k8bhl7jjjh3gf9f3iwy['pid'])
    return {'processes': ds4101n5jd97jpraw44pbe, 'count': len(ds4101n5jd97jpraw44pbe)}

def f8iisatqpaac9llg1qtdqb(kl1evbznz81kurt37133xc):
    dn1s3b3gx81lftjrd0elol = int(kl1evbznz81kurt37133xc['pid'])
    if dn1s3b3gx81lftjrd0elol <= 0:
        raise qxik4i1ab3x3aozq5e8hyt('pid invalido: %s' % dn1s3b3gx81lftjrd0elol)
    if dn1s3b3gx81lftjrd0elol == os.getpid():
        raise qxik4i1ab3x3aozq5e8hyt('o servidor nao pode encerrar a si mesmo')
    zeos50iasuucl022nn2uhl = str(kl1evbznz81kurt37133xc.get('signal', 'TERM')).upper()
    x980nt7op19coo0kd5e77f = getattr(signal, 'SIG' + zeos50iasuucl022nn2uhl, None)
    if x980nt7op19coo0kd5e77f is None:
        raise qxik4i1ab3x3aozq5e8hyt('sinal desconhecido: %s' % zeos50iasuucl022nn2uhl)
    try:
        os.kill(dn1s3b3gx81lftjrd0elol, x980nt7op19coo0kd5e77f)
    except ProcessLookupError:
        raise qxik4i1ab3x3aozq5e8hyt('processo nao encontrado: %d' % dn1s3b3gx81lftjrd0elol)
    except PermissionError:
        raise qxik4i1ab3x3aozq5e8hyt('sem permissao para encerrar o processo %d' % dn1s3b3gx81lftjrd0elol)
    return {'pid': dn1s3b3gx81lftjrd0elol, 'signal': zeos50iasuucl022nn2uhl}

def okt8w0ruryp6b3ll2cgl9c():
    if os.name == 'nt':
        wpk09sqd17uiwg0b8n8vb6 = os.environ.get('SystemRoot', 'C:\\Windows')
        izz7pfy7r7jtx3jowuurv7 = []
        z8n2gw24ydp98q9f2f8xsn = os.environ.get('TEMP') or os.environ.get('TMP')
        if z8n2gw24ydp98q9f2f8xsn:
            izz7pfy7r7jtx3jowuurv7.append(z8n2gw24ydp98q9f2f8xsn)
        izz7pfy7r7jtx3jowuurv7.append(os.path.join(wpk09sqd17uiwg0b8n8vb6, 'Temp'))
        izz7pfy7r7jtx3jowuurv7.append(os.path.join(wpk09sqd17uiwg0b8n8vb6, 'Prefetch'))
        izz7pfy7r7jtx3jowuurv7.append(os.path.join(wpk09sqd17uiwg0b8n8vb6, 'Logs'))
        return izz7pfy7r7jtx3jowuurv7
    import tempfile
    return [tempfile.gettempdir()]

def k4unfvmnl37k77vw6ctn7o(nr7wc5x492f1it0lipgy4n):
    u2k1zitow0rw60dtp48gxp = bool(nr7wc5x492f1it0lipgy4n.get('dry_run', True))
    x0gah8ad4clpwvdhw5rfqw = nr7wc5x492f1it0lipgy4n.get('paths') or okt8w0ruryp6b3ll2cgl9c()
    yyks1xohroo0d75qg1433c = []
    b36k3x28r5j8scyadgsyhu = {'files': 0, 'bytes': 0, 'deleted': 0, 'freed_bytes': 0, 'skipped': 0}
    for xchya5h39b5dhszw2ravw9 in x0gah8ad4clpwvdhw5rfqw:
        qijax49okh1oq95uf35p1i = {'path': str(xchya5h39b5dhszw2ravw9), 'exists': False, 'files': 0, 'bytes': 0, 'deleted': 0, 'freed_bytes': 0, 'skipped': 0}
        try:
            i2d7ydpbpehrn18f0oxcgo = b43pwr9dw5rarft7wgk814(xchya5h39b5dhszw2ravw9)
        except qxik4i1ab3x3aozq5e8hyt:
            qijax49okh1oq95uf35p1i['note'] = 'fora do escopo permitido'
            qijax49okh1oq95uf35p1i['skipped'] = 1
            b36k3x28r5j8scyadgsyhu['skipped'] += 1
            yyks1xohroo0d75qg1433c.append(qijax49okh1oq95uf35p1i)
            continue
        if not i2d7ydpbpehrn18f0oxcgo.is_dir():
            yyks1xohroo0d75qg1433c.append(qijax49okh1oq95uf35p1i)
            continue
        qijax49okh1oq95uf35p1i['path'] = str(i2d7ydpbpehrn18f0oxcgo)
        qijax49okh1oq95uf35p1i['exists'] = True
        for j9gge40b2ycok8i855ypi9, mnijnsfyk0ly7z9ndnwmky, fn5yyxn9pzg4rbnmvzb9ar in os.walk(i2d7ydpbpehrn18f0oxcgo):
            for cyvbmo7z0bv4bmbzcdueky in fn5yyxn9pzg4rbnmvzb9ar:
                nrkhsvdbjsbnyx3zprbe4h = Path(j9gge40b2ycok8i855ypi9) / cyvbmo7z0bv4bmbzcdueky
                try:
                    h97hlep7xaidj3x1n5nu0a = nrkhsvdbjsbnyx3zprbe4h.stat().st_size
                except OSError:
                    qijax49okh1oq95uf35p1i['skipped'] += 1
                    continue
                qijax49okh1oq95uf35p1i['files'] += 1
                qijax49okh1oq95uf35p1i['bytes'] += h97hlep7xaidj3x1n5nu0a
                if not u2k1zitow0rw60dtp48gxp:
                    try:
                        nrkhsvdbjsbnyx3zprbe4h.unlink()
                        qijax49okh1oq95uf35p1i['deleted'] += 1
                        qijax49okh1oq95uf35p1i['freed_bytes'] += h97hlep7xaidj3x1n5nu0a
                    except OSError:
                        qijax49okh1oq95uf35p1i['skipped'] += 1
        for h5lsvvh0jactn00eu43k25 in ('files', 'bytes', 'deleted', 'freed_bytes', 'skipped'):
            b36k3x28r5j8scyadgsyhu[h5lsvvh0jactn00eu43k25] += qijax49okh1oq95uf35p1i[h5lsvvh0jactn00eu43k25]
        yyks1xohroo0d75qg1433c.append(qijax49okh1oq95uf35p1i)
    return {'dry_run': u2k1zitow0rw60dtp48gxp, 'targets': yyks1xohroo0d75qg1433c, 'total': b36k3x28r5j8scyadgsyhu}

def fce4454p0am6plq4kbf3pz():
    return str(Path.home() / '.config' / SERVER_NAME / 'fts_index.db')

def b9jpx8moj3b6iwezag952y(krmnph32xzz7csnnn85h5z):
    import sqlite3
    l6475z8m2ca5xlgkq52b88 = sqlite3.connect(str(krmnph32xzz7csnnn85h5z))
    try:
        l6475z8m2ca5xlgkq52b88.execute("CREATE VIRTUAL TABLE IF NOT EXISTS fts USING fts5(path, content, tokenize='unicode61')")
    except Exception as upq3agif714ieojpn01ges:
        l6475z8m2ca5xlgkq52b88.close()
        raise qxik4i1ab3x3aozq5e8hyt('FTS5 indisponivel ou indice nao pode ser criado: %s' % upq3agif714ieojpn01ges)
    return l6475z8m2ca5xlgkq52b88

def lsej6w7hxae3nrpgb0p8fh(kdcov816yq8dhoz2qmyb3a):
    y3g4s2xbps43yzzynzudvy = kdcov816yq8dhoz2qmyb3a.get('paths')
    if not y3g4s2xbps43yzzynzudvy:
        raise qxik4i1ab3x3aozq5e8hyt('paths e obrigatorio: lista de arquivos ou diretorios')
    fu3ecfbmneehwc4q6dew5c = b43pwr9dw5rarft7wgk814(kdcov816yq8dhoz2qmyb3a.get('index_path', fce4454p0am6plq4kbf3pz()))
    d7mdggg01f1j34c28ti1iz = cr2qu1uhln4t1n5dwt8vdm()
    docc7k9ek09l95dgejf4ln = set()
    for qzx0aiyu1cek8ou499kgv5 in y3g4s2xbps43yzzynzudvy:
        try:
            tfnawfohg7nrhl0s8o41cu = b43pwr9dw5rarft7wgk814(qzx0aiyu1cek8ou499kgv5)
        except qxik4i1ab3x3aozq5e8hyt:
            continue
        if tfnawfohg7nrhl0s8o41cu.is_file():
            docc7k9ek09l95dgejf4ln.add(str(tfnawfohg7nrhl0s8o41cu))
        elif tfnawfohg7nrhl0s8o41cu.is_dir():
            for k3hu4im3d69aospa5win8z, l64595td63hb9l8be4zb5b, s7nieknkqfvzd8ohxaqtsw in os.walk(tfnawfohg7nrhl0s8o41cu):
                for k5cagkvdpxxjtwbgqp9s3k in s7nieknkqfvzd8ohxaqtsw:
                    docc7k9ek09l95dgejf4ln.add(str(Path(k3hu4im3d69aospa5win8z) / k5cagkvdpxxjtwbgqp9s3k))
    k6i6g4w0tfskwphbrdgg8t = udotlor6dp6x8vi9t0d1xx = lvsf8m1tpqret0e3cx2aas = 0
    eqcma92dq1dnj9g9ehbw7x = 0
    z1xa383ja16o2rt9tmaj6x = b9jpx8moj3b6iwezag952y(fu3ecfbmneehwc4q6dew5c)
    try:
        z1xa383ja16o2rt9tmaj6x.execute('DELETE FROM fts')
        for yuw2shhc1kahce8ox04zfy in sorted(docc7k9ek09l95dgejf4ln):
            try:
                with open(yuw2shhc1kahce8ox04zfy, 'rb') as oqbil3hhp35qlb0cxeib0r:
                    h4tcj9tvfwjyrz1u9e1cdk = oqbil3hhp35qlb0cxeib0r.read(4096)
                if b'\x00' in h4tcj9tvfwjyrz1u9e1cdk:
                    udotlor6dp6x8vi9t0d1xx += 1
                    continue
                o4zu58acq0k0umzqp7afjw, pxpxxj3v50ebrm5514q73l = lqj8x429i9m0d4t48mub7p(yuw2shhc1kahce8ox04zfy, d7mdggg01f1j34c28ti1iz)
            except OSError:
                lvsf8m1tpqret0e3cx2aas += 1
                continue
            z1xa383ja16o2rt9tmaj6x.execute('INSERT INTO fts (path, content) VALUES (?, ?)', (yuw2shhc1kahce8ox04zfy, o4zu58acq0k0umzqp7afjw.decode('utf-8', errors='replace')))
            k6i6g4w0tfskwphbrdgg8t += 1
            eqcma92dq1dnj9g9ehbw7x += len(o4zu58acq0k0umzqp7afjw)
        z1xa383ja16o2rt9tmaj6x.commit()
    finally:
        z1xa383ja16o2rt9tmaj6x.close()
    return {'index_path': str(fu3ecfbmneehwc4q6dew5c), 'files': k6i6g4w0tfskwphbrdgg8t, 'skipped_binary': udotlor6dp6x8vi9t0d1xx, 'skipped_errors': lvsf8m1tpqret0e3cx2aas, 'bytes_indexed': eqcma92dq1dnj9g9ehbw7x}

def lrg2ahup7wq18omwzljsdg(ug8zk1ssc5ibbgidq51drr):
    f5merby6t6ottd12jcs8ul = ug8zk1ssc5ibbgidq51drr.get('query')
    if not f5merby6t6ottd12jcs8ul:
        raise qxik4i1ab3x3aozq5e8hyt('query e obrigatoria (sintaxe FTS5 MATCH)')
    kj8t33h91eu3gy816pcbin = w7t27t98j1w1o444e25cpf(ug8zk1ssc5ibbgidq51drr.get('limit'), 20)
    e45skd1vzxoqj7zavyu99c = b43pwr9dw5rarft7wgk814(ug8zk1ssc5ibbgidq51drr.get('index_path', fce4454p0am6plq4kbf3pz()))
    if not e45skd1vzxoqj7zavyu99c.is_file():
        raise qxik4i1ab3x3aozq5e8hyt('indice nao existe: %s (rode index_files primeiro)' % e45skd1vzxoqj7zavyu99c)
    try:
        import sqlite3
        rhaoxf6vs9bln1zog7whlo = sqlite3.connect(str(e45skd1vzxoqj7zavyu99c))
        ac90wxazkz39w7j6u3om5j = rhaoxf6vs9bln1zog7whlo.execute("SELECT path, snippet(fts, 1, '[', ']', '...', 12) FROM fts WHERE fts MATCH ? ORDER BY rank LIMIT ?", (f5merby6t6ottd12jcs8ul, kj8t33h91eu3gy816pcbin)).fetchall()
        rhaoxf6vs9bln1zog7whlo.close()
    except qxik4i1ab3x3aozq5e8hyt:
        raise
    except Exception as q1onxxrres6ttx3r6jg372:
        raise qxik4i1ab3x3aozq5e8hyt('consulta FTS5 invalida ou indice ilegivel: %s' % q1onxxrres6ttx3r6jg372)
    return {'query': f5merby6t6ottd12jcs8ul, 'results': [{'path': ptkplssypitapzwcofhzso, 'snippet': p630m7ns4ii2nw4n0kono4} for ptkplssypitapzwcofhzso, p630m7ns4ii2nw4n0kono4 in ac90wxazkz39w7j6u3om5j], 'count': len(ac90wxazkz39w7j6u3om5j)}

def q6yhh4x5v0b6zh6sv7n6hq(iss62d8zmzd7jnonrr34in, uh3cl7j6tucxn8u069ee2a):
    return {'type': 'object', 'properties': iss62d8zmzd7jnonrr34in, 'required': uh3cl7j6tucxn8u069ee2a, 'additionalProperties': False}

def bni5amxkwb9r3f1h64u1kg(e9nx6hsk408vi5zmtw9ghx):
    return {'type': 'string', 'description': e9nx6hsk408vi5zmtw9ghx}

def s11e7vtjt2uk0b1coynaih(ne74bcyvpcm2rp9lw7roar, s8du7a67izes7tezdzapki=90):
    if os.name != 'nt':
        raise qxik4i1ab3x3aozq5e8hyt('ferramenta disponivel apenas no Windows')
    hsb8uumwdedtu3z54qh1qn = base64.b64encode(ne74bcyvpcm2rp9lw7roar.encode('utf-16-le')).decode('ascii')
    try:
        ps2q6dybieufke8vqmdggh = subprocess.run(['powershell.exe', '-NoProfile', '-NonInteractive', '-EncodedCommand', hsb8uumwdedtu3z54qh1qn], capture_output=True, timeout=s8du7a67izes7tezdzapki)
    except subprocess.TimeoutExpired:
        raise qxik4i1ab3x3aozq5e8hyt('powershell excedeu o timeout de %ds' % s8du7a67izes7tezdzapki)
    if ps2q6dybieufke8vqmdggh.returncode != 0:
        yvwftt8vm42gk1zwohr2vn = dhqoy4u44wcqwe6la8nzn2(ps2q6dybieufke8vqmdggh.stderr) or dhqoy4u44wcqwe6la8nzn2(ps2q6dybieufke8vqmdggh.stdout) or 'sem saida'
        raise qxik4i1ab3x3aozq5e8hyt('powershell falhou: %s' % yvwftt8vm42gk1zwohr2vn[:400])
    return dhqoy4u44wcqwe6la8nzn2(ps2q6dybieufke8vqmdggh.stdout).strip()
PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'

def wfyezws77dj2z0go8phfuo(te6dan6xkzjbrx2sm7ltjx):
    if len(te6dan6xkzjbrx2sm7ltjx) < 33 or te6dan6xkzjbrx2sm7ltjx[:8] != PNG_SIGNATURE:
        raise qxik4i1ab3x3aozq5e8hyt('blob nao e PNG valido: assinatura ausente ou truncada')
    uj8r0ikpof7p7emjragb2j, = struct.unpack('>I', te6dan6xkzjbrx2sm7ltjx[8:12])
    if te6dan6xkzjbrx2sm7ltjx[12:16] != b'IHDR' or uj8r0ikpof7p7emjragb2j != 13:
        raise qxik4i1ab3x3aozq5e8hyt('blob nao e PNG valido: chunk IHDR ausente ou malformado')
    kxp0ac1rj1aleiks8cq41m, dzqrq506p6bpmwozedpuya = struct.unpack('>II', te6dan6xkzjbrx2sm7ltjx[16:24])
    if kxp0ac1rj1aleiks8cq41m == 0 or dzqrq506p6bpmwozedpuya == 0:
        raise qxik4i1ab3x3aozq5e8hyt('blob nao e PNG valido: dimensoes zeradas')
    return {'width': kxp0ac1rj1aleiks8cq41m, 'height': dzqrq506p6bpmwozedpuya}

def dq1q6yif7t8ztypfxg6d8w(w9tjyxcgmthcov7r0gc54i):
    w7p7lxmqh7nsxjj4wnmb9j = float(w9tjyxcgmthcov7r0gc54i.get('scale', 0.5))
    w7p7lxmqh7nsxjj4wnmb9j = min(max(w7p7lxmqh7nsxjj4wnmb9j, 0.1), 1.0)
    r44w76acz3z2aacdkgsbvq = bool(w9tjyxcgmthcov7r0gc54i.get('compress', False))
    rljb6o854ry09syymj5bha = '\nAdd-Type -AssemblyName System.Windows.Forms\nAdd-Type -AssemblyName System.Drawing\n$b = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds\n$bmp = New-Object System.Drawing.Bitmap($b.Width, $b.Height)\n$g = [System.Drawing.Graphics]::FromImage($bmp)\n$g.CopyFromScreen($b.Location, [System.Drawing.Point]::Empty, $b.Size)\n$g.Dispose()\n$w = [int]($b.Width * %SCALE%); $h = [int]($b.Height * %SCALE%)\n$small = New-Object System.Drawing.Bitmap($w, $h)\n$sg = [System.Drawing.Graphics]::FromImage($small)\n$sg.DrawImage($bmp, 0, 0, $w, $h); $sg.Dispose(); $bmp.Dispose()\n$ms = New-Object System.IO.MemoryStream\n$small.Save($ms, [System.Drawing.Imaging.ImageFormat]::Png); $small.Dispose()\n[Convert]::ToBase64String($ms.ToArray())\n'.replace('%SCALE%', repr(w7p7lxmqh7nsxjj4wnmb9j))
    hkdf66x00kbv40ihxj9007 = s11e7vtjt2uk0b1coynaih(rljb6o854ry09syymj5bha)
    if not hkdf66x00kbv40ihxj9007:
        raise qxik4i1ab3x3aozq5e8hyt('captura vazia')
    try:
        u259bswluc0phfdl2fif8z = base64.b64decode(hkdf66x00kbv40ihxj9007, validate=True)
    except ValueError:
        raise qxik4i1ab3x3aozq5e8hyt('captura retornou base64 invalido')
    kmcn75c9bahvspsc07l7s9 = wfyezws77dj2z0go8phfuo(u259bswluc0phfdl2fif8z)
    yr0dbt5pqdcaq430moy3u5 = {'ok': True, 'scale': w7p7lxmqh7nsxjj4wnmb9j, 'width': kmcn75c9bahvspsc07l7s9['width'], 'height': kmcn75c9bahvspsc07l7s9['height'], 'png_bytes': len(u259bswluc0phfdl2fif8z), 'limitation': 'captura apenas a tela principal; janelas sobrepostas aparecem como estao na tela'}
    if r44w76acz3z2aacdkgsbvq:
        b9l3jqvc0x48mhvg2mxvng = zlib.compress(u259bswluc0phfdl2fif8z, 9)
        yr0dbt5pqdcaq430moy3u5['compression'] = 'zlib'
        yr0dbt5pqdcaq430moy3u5['compressed_bytes'] = len(b9l3jqvc0x48mhvg2mxvng)
        yr0dbt5pqdcaq430moy3u5['png_zlib_base64'] = base64.b64encode(b9l3jqvc0x48mhvg2mxvng).decode('ascii')
    else:
        yr0dbt5pqdcaq430moy3u5['png_base64'] = hkdf66x00kbv40ihxj9007
    return yr0dbt5pqdcaq430moy3u5

def xj7ibzfp8gvvlj8a8jd8a6(sg2gqwoz4c86yl5ilqqhns):
    nw5m766lcnzgysz6ydti1k = int(sg2gqwoz4c86yl5ilqqhns.get('max', 150))
    nw5m766lcnzgysz6ydti1k = min(max(nw5m766lcnzgysz6ydti1k, 1), 500)
    ljuncghue6kyqfzxmb83kj = '\nAdd-Type -AssemblyName UIAutomationClient\nAdd-Type -AssemblyName UIAutomationTypes\n$walker = [System.Windows.Automation.TreeWalker]::ControlViewWalker\n$root = [System.Windows.Automation.AutomationElement]::RootElement\n$out = @(); $n = 0\n$stack = New-Object System.Collections.Stack\n$stack.Push($root)\nwhile ($stack.Count -gt 0 -and $n -lt %MAX%) {\n  $el = $stack.Pop()\n  try {\n    $r = $el.Current.BoundingRectangle\n    $name = $el.Current.Name\n    if ($name -and $r.Width -gt 0) {\n      $out += [pscustomobject]@{\n        name = $name\n        type = $el.Current.LocalizedControlType\n        x = [int]($r.X + $r.Width / 2); y = [int]($r.Y + $r.Height / 2)\n        w = [int]$r.Width; h = [int]$r.Height\n      }\n      $n++\n    }\n    $child = $walker.GetFirstChild($el)\n    while ($child -ne $null) { $stack.Push($child); $child = $walker.GetNextSibling($child) }\n  } catch { }\n}\n$out | ConvertTo-Json -Compress -Depth 2\n'.replace('%MAX%', str(nw5m766lcnzgysz6ydti1k))
    p3n2fc8u10o3yyh9ron9nh = s11e7vtjt2uk0b1coynaih(ljuncghue6kyqfzxmb83kj, s8du7a67izes7tezdzapki=120)
    try:
        lyt23r62xyjwoflzvtry1i = json.loads(p3n2fc8u10o3yyh9ron9nh) if p3n2fc8u10o3yyh9ron9nh else []
    except (ValueError, TypeError):
        lyt23r62xyjwoflzvtry1i = []
    if isinstance(lyt23r62xyjwoflzvtry1i, dict):
        lyt23r62xyjwoflzvtry1i = [lyt23r62xyjwoflzvtry1i]
    return {'ok': True, 'count': len(lyt23r62xyjwoflzvtry1i), 'elements': lyt23r62xyjwoflzvtry1i, 'limitation': 'apps que desenham a propria tela (jogos, canvas) nao expoem elementos; use find_template para esses'}

def u4gw5wnckai7pb7b1lqmdl(f6xzpznfgam2ldltbrajal):
    qabj7npsrx6hjksrmzflg3 = int(f6xzpznfgam2ldltbrajal['x'])
    duqjswmwcaqz3i3k7i33ce = int(f6xzpznfgam2ldltbrajal['y'])
    oli9451uwotpgy77rp29ob = str(f6xzpznfgam2ldltbrajal.get('button', 'left')).lower()
    aarxdxe4rqb21d5vr0gkjr = min(max(int(f6xzpznfgam2ldltbrajal.get('clicks', 1)), 1), 3)
    b96cdm7raxpshrcplds57f, rvg2q9jjortf4lkkvxgmvt = (2, 4) if oli9451uwotpgy77rp29ob != 'right' else (8, 16)
    l339skmygohcmcwdtve757 = '\nAdd-Type -TypeDefinition @"\nusing System; using System.Runtime.InteropServices;\npublic static class M {\n  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);\n  [DllImport("user32.dll")] public static extern void mouse_event(int f, int dx, int dy, int d, int e);\n}\n"@\nfor ($i = 0; $i -lt %CLICKS%; $i++) {\n  [M]::SetCursorPos(%X%, %Y%) | Out-Null\n  [M]::mouse_event(%DOWN%, 0, 0, 0, 0); [M]::mouse_event(%UP%, 0, 0, 0, 0)\n  Start-Sleep -Milliseconds 120\n}\n"OK"\n'.replace('%X%', str(qabj7npsrx6hjksrmzflg3)).replace('%Y%', str(duqjswmwcaqz3i3k7i33ce)).replace('%DOWN%', str(b96cdm7raxpshrcplds57f)).replace('%UP%', str(rvg2q9jjortf4lkkvxgmvt)).replace('%CLICKS%', str(aarxdxe4rqb21d5vr0gkjr))
    s11e7vtjt2uk0b1coynaih(l339skmygohcmcwdtve757)
    return {'ok': True, 'x': qabj7npsrx6hjksrmzflg3, 'y': duqjswmwcaqz3i3k7i33ce, 'button': oli9451uwotpgy77rp29ob, 'clicks': aarxdxe4rqb21d5vr0gkjr}

def mddtipxcs9bmnfts1utbdm(ayu6c78837kukcftncckud):
    return ''.join(('{%s}' % bdfctnhrcdlm2b5ez9ao2n if bdfctnhrcdlm2b5ez9ao2n in '+^%~()[]{}' else bdfctnhrcdlm2b5ez9ao2n for bdfctnhrcdlm2b5ez9ao2n in ayu6c78837kukcftncckud))

def k1qo56pfok7nnwxdpbh2xt(xyplo55r1yhx4m9v0tisy7):
    yrlmh7ncgpxdwptf2iuov8 = str(xyplo55r1yhx4m9v0tisy7.get('text', ''))
    if not yrlmh7ncgpxdwptf2iuov8:
        raise qxik4i1ab3x3aozq5e8hyt('text vazio')
    pxod1yk5wyd9is3v13wp6q = '\nAdd-Type -AssemblyName System.Windows.Forms\n[System.Windows.Forms.SendKeys]::SendWait(@\'\n%TEXT%\n\'@)\n"OK"\n'.replace('%TEXT%', mddtipxcs9bmnfts1utbdm(yrlmh7ncgpxdwptf2iuov8).replace("'", "''"))
    s11e7vtjt2uk0b1coynaih(pxod1yk5wyd9is3v13wp6q)
    return {'ok': True, 'chars': len(yrlmh7ncgpxdwptf2iuov8), 'limitation': 'digita na janela com foco atual'}
_PRESS_KEYS = {'enter': '{ENTER}', 'tab': '{TAB}', 'esc': '{ESC}', 'escape': '{ESC}', 'space': ' ', 'backspace': '{BACKSPACE}', 'delete': '{DELETE}', 'up': '{UP}', 'down': '{DOWN}', 'left': '{LEFT}', 'right': '{RIGHT}', 'home': '{HOME}', 'end': '{END}', 'pgup': '{PGUP}', 'pgdn': '{PGDN}', 'f1': '{F1}', 'f2': '{F2}', 'f3': '{F3}', 'f4': '{F4}', 'f5': '{F5}', 'f6': '{F6}', 'f7': '{F7}', 'f8': '{F8}', 'f9': '{F9}', 'f10': '{F10}', 'f11': '{F11}', 'f12': '{F12}', 'win': '^{ESC}'}

def tcamd89fej07tsw6benjyb(ojsjzfqy4nmz4g2wwfhezz):
    p5link628nptv9xqwdj12c = str(ojsjzfqy4nmz4g2wwfhezz.get('key', '')).lower()
    e1o6cf2vtcdy7xycu2pm57 = _PRESS_KEYS.get(p5link628nptv9xqwdj12c)
    if e1o6cf2vtcdy7xycu2pm57 is None:
        raise qxik4i1ab3x3aozq5e8hyt('tecla desconhecida: %s (use: %s)' % (p5link628nptv9xqwdj12c, ', '.join(sorted(_PRESS_KEYS))))
    er7b1kpy4ftukti43fs50l = '\nAdd-Type -AssemblyName System.Windows.Forms\n[System.Windows.Forms.SendKeys]::SendWait(\'%CODE%\')\n"OK"\n'.replace('%CODE%', e1o6cf2vtcdy7xycu2pm57)
    s11e7vtjt2uk0b1coynaih(er7b1kpy4ftukti43fs50l)
    return {'ok': True, 'key': p5link628nptv9xqwdj12c}

def s9yzkdqnbautmij4n62y3l(q6diwlp3ywn4ely7zgdjpq):
    egcbidmepzrf36slb1v03q = str(q6diwlp3ywn4ely7zgdjpq.get('template_base64', ''))
    if not egcbidmepzrf36slb1v03q:
        raise qxik4i1ab3x3aozq5e8hyt('template_base64 vazio (PNG em base64)')
    vy58o89em3uuxs9kzvw033 = min(max(int(q6diwlp3ywn4ely7zgdjpq.get('downscale', 3)), 1), 6)
    o2y84yevnsoc0a28cjemhk = str(q6diwlp3ywn4ely7zgdjpq.get('screenshot_base64', ''))
    vxies3xhoqz8f1p3eajnjn = '\nAdd-Type -AssemblyName System.Drawing\nfunction ShotB64($scale) {\n  Add-Type -AssemblyName System.Windows.Forms\n  $b = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds\n  $bmp = New-Object System.Drawing.Bitmap($b.Width, $b.Height)\n  $g = [System.Drawing.Graphics]::FromImage($bmp)\n  $g.CopyFromScreen($b.Location, [System.Drawing.Point]::Empty, $b.Size); $g.Dispose()\n  $ms = New-Object System.IO.MemoryStream\n  $bmp.Save($ms, [System.Drawing.Imaging.ImageFormat]::Png); $bmp.Dispose()\n  return [Convert]::ToBase64String($ms.ToArray())\n}\n$shotB64 = @\'\n%SHOT%\n\'@\nif (-not $shotB64) { $shotB64 = ShotB64 }\n$tmplB64 = @\'\n%TMPL%\n\'@\nAdd-Type -ReferencedAssemblies System.Drawing -TypeDefinition @"\nusing System; using System.Drawing; using System.IO;\npublic static class TM {\n  static byte[] Gray(Bitmap b, int w, int h) {\n    var bd = b.LockBits(new Rectangle(0,0,b.Width,b.Height), ImageLockMode.ReadOnly, System.Drawing.Imaging.PixelFormat.Format24bppRgb);\n    var g = new byte[w*h];\n    unsafe { byte* p = (byte*)bd.Scan0;\n      for (int y=0;y<h;y++) for (int x=0;x<w;x++) {\n        int sx = x*b.Width/w, sy = y*b.Height/h;\n        byte* px = p + sy*bd.Stride + sx*3;\n        g[y*w+x] = (byte)((px[2]+px[1]+px[0])/3);\n      } }\n    b.UnlockBits(bd); return g;\n  }\n  public static string Find(string s64, string t64, int ds) {\n    using (var ms = new MemoryStream(Convert.FromBase64String(s64)))\n    using (var mt = new MemoryStream(Convert.FromBase64String(t64)))\n    using (var s0 = new Bitmap(ms)) using (var t0 = new Bitmap(mt)) {\n      int sw=s0.Width/ds, sh=s0.Height/ds, tw=t0.Width/ds, th=t0.Height/ds;\n      if (tw<1||th<1||tw>sw||th>sh) return "0,0,1.0000";\n      var sg=Gray(s0,sw,sh); var tg=Gray(t0,tw,th);\n      long best=long.MaxValue; int bx=0, by=0;\n      for (int y=0;y<=sh-th;y++) for (int x=0;x<=sw-tw;x++) {\n        long sad=0;\n        for (int j=0;j<th && sad<best;j++) for (int i=0;i<tw;i++)\n          sad += Math.Abs((int)sg[(y+j)*sw+x+i]-(int)tg[j*tw+i]);\n        if (sad<best){best=sad;bx=x;by=y;}\n      }\n      return (bx*ds)+","+(by*ds)+","+((double)best/(tw*th*255)).ToString("F4");\n    }\n  }\n}\n"@\n[TM]::Find($shotB64, $tmplB64, %DS%)\n'.replace('%SHOT%', o2y84yevnsoc0a28cjemhk).replace('%TMPL%', egcbidmepzrf36slb1v03q).replace('%DS%', str(vy58o89em3uuxs9kzvw033))
    lykttu1ep61k3r6xnzgyb8 = s11e7vtjt2uk0b1coynaih(vxies3xhoqz8f1p3eajnjn, s8du7a67izes7tezdzapki=180)
    try:
        ahf6mgvdkf956nocbwttwo, hjjgxabcox6s5veb2l8z3p, izhu3m0zrodcp5ue7cbfzm = lykttu1ep61k3r6xnzgyb8.split(',')
        ahf6mgvdkf956nocbwttwo, hjjgxabcox6s5veb2l8z3p, izhu3m0zrodcp5ue7cbfzm = (int(ahf6mgvdkf956nocbwttwo), int(hjjgxabcox6s5veb2l8z3p), float(izhu3m0zrodcp5ue7cbfzm))
    except (ValueError, AttributeError):
        raise qxik4i1ab3x3aozq5e8hyt('resposta inesperada do matcher: %s' % lykttu1ep61k3r6xnzgyb8[:200])
    return {'ok': True, 'x': ahf6mgvdkf956nocbwttwo, 'y': hjjgxabcox6s5veb2l8z3p, 'score': izhu3m0zrodcp5ue7cbfzm, 'limitation': 'SAD em tons de cinza com reducao %dx; score 0=igual, proximo de 0=bom' % vy58o89em3uuxs9kzvw033}
TOOLS = [{'name': 'read_file', 'description': 'Le um arquivo de texto dentro do escopo permitido, parte a parte: offset e limit em bytes (teto real de 1 MB por chamada). O retorno traz o tamanho real (bytes), o offset lido, next_offset e truncated — um arquivo de 28 GB e lido fatia a fatia, sem nunca entrar inteiro na memoria.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho absoluto ou relativo a home.'), 'offset': {'type': 'integer', 'description': 'Byte inicial da fatia (padrao 0).'}, 'limit': {'type': 'integer', 'description': 'Bytes desta fatia (padrao e teto: 1 MB).'}}, ['path']), 'handler': kgukosv3qx4hz9dh1ihube}, {'name': 'sniff_log', 'description': 'Reconhece o formato de um log .txt sem ler o conteudo inteiro: delimitador, cabecalho e campos, formato de timestamp, total de linhas e amostra das primeiras linhas. Use antes de processar logs grandes ou de formato desconhecido.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho do log.')}, ['path']), 'handler': reci56s279cy4e66jxzj80}, {'name': 'write_file', 'description': 'Escreve (cria ou sobrescreve) um arquivo de texto; cria diretorios pais.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho do arquivo.'), 'content': bni5amxkwb9r3f1h64u1kg('Conteudo completo.')}, ['path', 'content']), 'handler': njy64jgrk8ufmfnw7ig3bo}, {'name': 'edit_file', 'description': 'Substitui um trecho exato de um arquivo. Se o trecho aparecer mais de uma vez, exige replace_all=true.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho do arquivo.'), 'old_text': bni5amxkwb9r3f1h64u1kg('Trecho exato atual.'), 'new_text': bni5amxkwb9r3f1h64u1kg('Trecho novo.'), 'replace_all': {'type': 'boolean', 'description': 'Substituir todas as ocorrencias.'}}, ['path', 'old_text', 'new_text']), 'handler': rt63u7hflbfe2rcitimsxh}, {'name': 'list_directory', 'description': 'Lista o conteudo de um diretorio com tipo, tamanho e data de modificacao.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho do diretorio.')}, ['path']), 'handler': kbj4z7ltro39incsw6i9i2}, {'name': 'create_directory', 'description': 'Cria um diretorio (e pais, se preciso).', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho do diretorio.')}, ['path']), 'handler': y6snldqapfqd73iae0763j}, {'name': 'move_file', 'description': 'Move ou renomeia um arquivo ou diretorio dentro do escopo.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'source': bni5amxkwb9r3f1h64u1kg('Origem.'), 'destination': bni5amxkwb9r3f1h64u1kg('Destino.')}, ['source', 'destination']), 'handler': twpn10a1lcv6i9rvle6kvd}, {'name': 'delete_path', 'description': 'Apaga permanentemente (sem Lixeira) um arquivo ou um diretorio (recursivo, inclusive nao vazio). A raiz do sistema e recusada.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho a apagar.')}, ['path']), 'handler': mxsis6gdgwwruvufztjy2i}, {'name': 'search_files', 'description': 'Busca arquivos por padrao glob sob um diretorio raiz do escopo.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'root': bni5amxkwb9r3f1h64u1kg('Diretorio raiz.'), 'pattern': bni5amxkwb9r3f1h64u1kg('Padrao glob, ex.: **/*.py.'), 'max_results': {'type': 'integer', 'description': 'Limite de resultados (padrao 50, maximo 200).'}}, ['root', 'pattern']), 'handler': q6e0u6d0glt3u4e59qzqu4}, {'name': 'get_file_info', 'description': 'Retorna metadados (tamanho, permissoes, datas) de um arquivo ou diretorio.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'path': bni5amxkwb9r3f1h64u1kg('Caminho.')}, ['path']), 'handler': lqrase7ifwnlrsmq3dk693}, {'name': 'execute_command', 'description': 'Executa um comando de shell com timeout e saida truncada. Comandos perigosos sao bloqueados pela politica configurada.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'command': bni5amxkwb9r3f1h64u1kg('Comando de shell.'), 'cwd': bni5amxkwb9r3f1h64u1kg('Diretorio de trabalho dentro do escopo (opcional).'), 'timeout': {'type': 'integer', 'description': 'Timeout em segundos.'}}, ['command']), 'handler': kegxr3enidt00yb5gohwjd}, {'name': 'list_processes', 'description': 'Lista os processos em execucao (pid, ppid, nome, estado, linha de comando).', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({}, []), 'handler': af6gpsk4y5qsiz08qp72eg}, {'name': 'kill_process', 'description': 'Envia um sinal a um processo (padrao TERM).', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'pid': {'type': 'integer', 'description': 'PID do processo.'}, 'signal': bni5amxkwb9r3f1h64u1kg('Sinal sem prefixo SIG, ex.: TERM, KILL (opcional).')}, ['pid']), 'handler': f8iisatqpaac9llg1qtdqb}, {'name': 'clean_temp', 'description': 'Comando padrao de limpeza de temporarios, sempre PERMANENTE (nada vai para a Lixeira). dry_run=true (padrao) so inventaria; dry_run=false apaga os arquivos. Alvos padrao no Windows: TEMP do usuario, Windows\\Temp, Prefetch e Logs; no POSIX: o diretorio temporario do sistema. Apaga apenas arquivos (nunca as pastas); arquivos em uso sao pulados e contados.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'paths': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Diretorios alvo (opcional; padrao: os temporarios do sistema).'}, 'dry_run': {'type': 'boolean', 'description': 'true = so inventaria (padrao); false = apaga os arquivos.'}}, []), 'handler': k4unfvmnl37k77vw6ctn7o}, {'name': 'index_files', 'description': 'Indexa arquivos de texto em um indice SQLite FTS5: qualquer pasta, todas as subpastas, recursivo e deterministico (reindexar substitui o indice). Arquivos binarios sao pulados; cada arquivo indexa no maximo o limite de leitura (o mesmo do read_file).', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'paths': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Arquivos ou diretorios a indexar (obrigatorio).'}, 'index_path': bni5amxkwb9r3f1h64u1kg('Caminho do arquivo de indice (opcional; padrao: ~/.config/muse-terminal-commander/fts_index.db).')}, ['paths']), 'handler': lsej6w7hxae3nrpgb0p8fh}, {'name': 'search_index', 'description': 'Busca full-text no indice FTS5 (sintaxe MATCH): retorna caminho e snippet, ordenado por relevancia. O limite de resultados e capado em MAX_SEARCH_RESULTS.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'query': bni5amxkwb9r3f1h64u1kg('Consulta FTS5, ex.: erro OR timeout (obrigatorio).'), 'limit': {'type': 'integer', 'description': 'Maximo de resultados (padrao 20, teto 200).'}, 'index_path': bni5amxkwb9r3f1h64u1kg('Caminho do arquivo de indice (opcional).')}, ['query']), 'handler': lrg2ahup7wq18omwzljsdg}, {'name': 'verify_audit', 'description': 'Verifica a cadeia de integridade (hash-chain) do log de auditoria: detecta linhas adulteradas, removidas ou inseridas. Retorna entradas encadeadas, linhas legadas sem hash, validade e onde a cadeia quebra.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({}, []), 'handler': f20fqy37s9juxubprzj97g}, {'name': 'capture_baseline', 'description': 'Fotografa a referencia: hash SHA-256 de cada arquivo das arvores pedidas (padrao: o diretorio do proprio servidor), nomes dos processos em execucao e identificacao da maquina. Guarda em baseline.json.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'paths': {'type': 'array', 'description': 'Arvores a fotografar (padrao: diretorio do servidor).'}, 'name': bni5amxkwb9r3f1h64u1kg('Nome da baseline (padrao: default).'), 'baseline_path': bni5amxkwb9r3f1h64u1kg('Caminho do arquivo da baseline (opcional).')}, []), 'handler': uhuclyznb5kgv29kk8xi9p}, {'name': 'screenshot', 'description': 'Captura a tela principal do computador (PNG em base64). Sem instalar nada: usa o .NET do proprio Windows.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'scale': {'type': 'number', 'description': 'Escala 0.1-1.0 (padrao 0.5).'}, 'compress': {'type': 'boolean', 'description': 'Comprime o PNG com zlib antes do base64 (padrao false; com true a resposta traz png_zlib_base64).'}}, []), 'handler': dq1q6yif7t8ztypfxg6d8w}, {'name': 'ui_elements', 'description': 'Lista os elementos visiveis da interface do Windows (nome, tipo, centro x/y, tamanho) via UI Automation. Para clicar num botao, ache aqui as coordenadas.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'max': {'type': 'integer', 'description': 'Maximo de elementos (padrao 150, teto 500).'}}, []), 'handler': xj7ibzfp8gvvlj8a8jd8a6}, {'name': 'click', 'description': 'Clica na tela do computador nas coordenadas x,y.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'x': {'type': 'integer', 'description': 'Coordenada x em pixels.'}, 'y': {'type': 'integer', 'description': 'Coordenada y em pixels.'}, 'button': {'type': 'string', 'description': 'left ou right (padrao left).'}, 'clicks': {'type': 'integer', 'description': '1-3 cliques (padrao 1).'}}, ['x', 'y']), 'handler': u4gw5wnckai7pb7b1lqmdl}, {'name': 'type_text', 'description': 'Digita texto na janela com foco atual (teclado virtual via SendKeys).', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'text': bni5amxkwb9r3f1h64u1kg('Texto a digitar.')}, ['text']), 'handler': k1qo56pfok7nnwxdpbh2xt}, {'name': 'press_key', 'description': 'Pressiona uma tecla especial: enter, tab, esc, space, backspace, delete, setas, home, end, pgup, pgdn, f1-f12, win.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'key': bni5amxkwb9r3f1h64u1kg('Nome da tecla.')}, ['key']), 'handler': tcamd89fej07tsw6benjyb}, {'name': 'find_template', 'description': 'Procura uma imagem-modelo (PNG em base64) dentro da tela e devolve x,y do melhor casamento e score (0=igual). Para botoes em jogos e telas que nao expoem elementos.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'template_base64': bni5amxkwb9r3f1h64u1kg('PNG do modelo em base64.'), 'screenshot_base64': {'type': 'string', 'description': 'PNG da tela em base64 (se vazio, captura na hora).'}, 'downscale': {'type': 'integer', 'description': 'Reducao para velocidade 1-6 (padrao 3).'}}, ['template_base64']), 'handler': s9yzkdqnbautmij4n62y3l}, {'name': 'check_baseline', 'description': 'Compara o estado atual com a baseline: arquivos alterados, removidos e novos; processos novos e encerrados. O teste de auditoria periodico: rodar de novo e o monitoramento continuo.', 'inputSchema': q6yhh4x5v0b6zh6sv7n6hq({'baseline_path': bni5amxkwb9r3f1h64u1kg('Caminho do arquivo da baseline (opcional).')}, []), 'handler': jse02550lk0v9ge2rtif95}]
HANDLERS = {dq6dq3d1su3hwel6f23o24['name']: dq6dq3d1su3hwel6f23o24['handler'] for dq6dq3d1su3hwel6f23o24 in TOOLS}

def qs5fhchded1psdr5v3y9bm(yg8i7hrm7fttrgxeewyro8, bp7rlrek39l07o81i0o7g4):
    return {'jsonrpc': '2.0', 'id': yg8i7hrm7fttrgxeewyro8, 'result': bp7rlrek39l07o81i0o7g4}

def zjze6g5nmlnoe19fydqqh1(dxlit16sw7mfmhmkq54usa, gk5o2bm5jp11rj5a8jd83z, j7cpiyuka4hu2tmbo7kas3):
    return {'jsonrpc': '2.0', 'id': dxlit16sw7mfmhmkq54usa, 'error': {'code': gk5o2bm5jp11rj5a8jd83z, 'message': j7cpiyuka4hu2tmbo7kas3}}

def v1v6r8zoyxbfra37iszrvm(qos7dk1kem9pr8rb0gfkzy):
    if not isinstance(qos7dk1kem9pr8rb0gfkzy, dict) or 'method' not in qos7dk1kem9pr8rb0gfkzy:
        return None
    au3ykh275ujndzdsy9xbml = qos7dk1kem9pr8rb0gfkzy['method']
    wkjr0a20luaw976tpyn6sc = qos7dk1kem9pr8rb0gfkzy.get('params') or {}
    k4ts3w224krntjwrx4d4hw = 'id' not in qos7dk1kem9pr8rb0gfkzy
    sd9ms5eodic3blbo5heojw = qos7dk1kem9pr8rb0gfkzy.get('id')
    if au3ykh275ujndzdsy9xbml == 'initialize':
        if k4ts3w224krntjwrx4d4hw:
            return None
        return qs5fhchded1psdr5v3y9bm(sd9ms5eodic3blbo5heojw, {'protocolVersion': PROTOCOL_VERSION, 'capabilities': {'tools': {}}, 'serverInfo': {'name': SERVER_NAME, 'version': SERVER_VERSION}})
    if au3ykh275ujndzdsy9xbml == 'ping':
        return None if k4ts3w224krntjwrx4d4hw else qs5fhchded1psdr5v3y9bm(sd9ms5eodic3blbo5heojw, {})
    if au3ykh275ujndzdsy9xbml.startswith('notifications/'):
        return None
    if au3ykh275ujndzdsy9xbml == 'tools/list':
        if k4ts3w224krntjwrx4d4hw:
            return None
        q8zabrwryb3oe01b20h1k2 = [{'name': a37l44ss9s32flh1fh4tfe['name'], 'description': a37l44ss9s32flh1fh4tfe['description'], 'inputSchema': a37l44ss9s32flh1fh4tfe['inputSchema']} for a37l44ss9s32flh1fh4tfe in TOOLS]
        return qs5fhchded1psdr5v3y9bm(sd9ms5eodic3blbo5heojw, {'tools': q8zabrwryb3oe01b20h1k2})
    if au3ykh275ujndzdsy9xbml == 'tools/call':
        bvw48ivep2uqgrx505ld6f = wkjr0a20luaw976tpyn6sc.get('name')
        s4th61cf9qwyjgqt6oqeu4 = wkjr0a20luaw976tpyn6sc.get('arguments') or {}
        ra2o233fh0xvvkzjltfetx = HANDLERS.get(bvw48ivep2uqgrx505ld6f)
        if ra2o233fh0xvvkzjltfetx is None:
            return None if k4ts3w224krntjwrx4d4hw else zjze6g5nmlnoe19fydqqh1(sd9ms5eodic3blbo5heojw, -32602, 'tool desconhecida: %s' % bvw48ivep2uqgrx505ld6f)
        try:
            d6c75kdary4s7xrjt1urts(bvw48ivep2uqgrx505ld6f, s4th61cf9qwyjgqt6oqeu4)
            obn2b7x7x29irsbkudz77b = ra2o233fh0xvvkzjltfetx(s4th61cf9qwyjgqt6oqeu4)
            nmixv3w3l02delmlzv9dhd(bvw48ivep2uqgrx505ld6f, jwhqegqhu9qycdeuqh8x4x(bvw48ivep2uqgrx505ld6f, s4th61cf9qwyjgqt6oqeu4), True)
            if k4ts3w224krntjwrx4d4hw:
                return None
            return qs5fhchded1psdr5v3y9bm(sd9ms5eodic3blbo5heojw, {'content': [{'type': 'text', 'text': json.dumps(obn2b7x7x29irsbkudz77b, ensure_ascii=False)}], 'isError': False})
        except qxik4i1ab3x3aozq5e8hyt as g8pz5s2iogpldy0whitvk3:
            nmixv3w3l02delmlzv9dhd(bvw48ivep2uqgrx505ld6f, jwhqegqhu9qycdeuqh8x4x(bvw48ivep2uqgrx505ld6f, s4th61cf9qwyjgqt6oqeu4), False, g8pz5s2iogpldy0whitvk3)
            if k4ts3w224krntjwrx4d4hw:
                return None
            return qs5fhchded1psdr5v3y9bm(sd9ms5eodic3blbo5heojw, {'content': [{'type': 'text', 'text': str(g8pz5s2iogpldy0whitvk3)}], 'isError': True})
        except KeyError as g8pz5s2iogpldy0whitvk3:
            nmixv3w3l02delmlzv9dhd(bvw48ivep2uqgrx505ld6f, jwhqegqhu9qycdeuqh8x4x(bvw48ivep2uqgrx505ld6f, s4th61cf9qwyjgqt6oqeu4), False, 'argumento faltando: %s' % g8pz5s2iogpldy0whitvk3)
            if k4ts3w224krntjwrx4d4hw:
                return None
            return qs5fhchded1psdr5v3y9bm(sd9ms5eodic3blbo5heojw, {'content': [{'type': 'text', 'text': 'argumento obrigatorio faltando: %s' % g8pz5s2iogpldy0whitvk3}], 'isError': True})
        except Exception as g8pz5s2iogpldy0whitvk3:
            nmixv3w3l02delmlzv9dhd(bvw48ivep2uqgrx505ld6f, jwhqegqhu9qycdeuqh8x4x(bvw48ivep2uqgrx505ld6f, s4th61cf9qwyjgqt6oqeu4), False, g8pz5s2iogpldy0whitvk3)
            return None if k4ts3w224krntjwrx4d4hw else zjze6g5nmlnoe19fydqqh1(sd9ms5eodic3blbo5heojw, -32603, 'erro interno: %s' % g8pz5s2iogpldy0whitvk3)
    return None if k4ts3w224krntjwrx4d4hw else zjze6g5nmlnoe19fydqqh1(sd9ms5eodic3blbo5heojw, -32601, 'metodo desconhecido: %s' % au3ykh275ujndzdsy9xbml)

def xbmjnvy9k18vmbvbavkonf():
    for n3jxo4hu4d0mhkxxy9kntb in sys.stdin:
        n3jxo4hu4d0mhkxxy9kntb = n3jxo4hu4d0mhkxxy9kntb.strip()
        if not n3jxo4hu4d0mhkxxy9kntb:
            continue
        try:
            a73iim17fgsi7fefgkm3xl = json.loads(n3jxo4hu4d0mhkxxy9kntb)
        except json.JSONDecodeError:
            continue
        noys55s3kcuhh8qbowtmbj = v1v6r8zoyxbfra37iszrvm(a73iim17fgsi7fefgkm3xl)
        if noys55s3kcuhh8qbowtmbj is not None:
            sys.stdout.write(json.dumps(noys55s3kcuhh8qbowtmbj, ensure_ascii=False) + '\n')
            sys.stdout.flush()
if __name__ == '__main__':
    xbmjnvy9k18vmbvbavkonf()
