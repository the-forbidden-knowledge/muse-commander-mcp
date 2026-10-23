import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SERVER = ROOT / 'vmmaieuzwn7j9llhbznbgs.py'
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

class k2qargg4sjxl1nj8en8t98:

    def __init__(self, pmuocy6cok0p6hh56cijx2: Path, st0xc8gkthu6tvtib5ug30=None):
        self.workdir = pmuocy6cok0p6hh56cijx2
        if st0xc8gkthu6tvtib5ug30 is None:
            st0xc8gkthu6tvtib5ug30 = {'allowed_directories': [str(pmuocy6cok0p6hh56cijx2)], 'blocked_command_patterns': ['(^|\\s)rm\\s+-rf?\\s+/'], 'audit_log': str(pmuocy6cok0p6hh56cijx2 / 'audit.log')}
        bi0bhju53vawggujfwgv80 = pmuocy6cok0p6hh56cijx2 / 'config.json'
        bi0bhju53vawggujfwgv80.write_text(json.dumps(st0xc8gkthu6tvtib5ug30), encoding='utf-8')
        pcx753danavmb9reorxjt0 = dict(os.environ, MUSE_COMMANDER_CONFIG=str(bi0bhju53vawggujfwgv80))
        self.proc = subprocess.Popen([sys.executable, str(SERVER)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', env=pcx753danavmb9reorxjt0)
        self._id = 0

    def wlxembuljv2qmtbb69rwex(self, hfypvbhkc8lbxvhzse087z, fdm1tsiuz55nqeg89xr9m5=None):
        self._id += 1
        n9nyjnp2dioes3o95rjg50 = {'jsonrpc': '2.0', 'id': self._id, 'method': hfypvbhkc8lbxvhzse087z}
        if fdm1tsiuz55nqeg89xr9m5 is not None:
            n9nyjnp2dioes3o95rjg50['params'] = fdm1tsiuz55nqeg89xr9m5
        self.proc.stdin.write(json.dumps(n9nyjnp2dioes3o95rjg50) + '\n')
        self.proc.stdin.flush()
        gze0xh0dya0nakqa9ygu1j = self.proc.stdout.readline()
        self.assert_line = gze0xh0dya0nakqa9ygu1j
        return json.loads(gze0xh0dya0nakqa9ygu1j)

    def xca160sphuc218o5fwh2gu(self, olxfdpj7vu10zfn280af5q):
        self.proc.stdin.write(json.dumps({'jsonrpc': '2.0', 'method': olxfdpj7vu10zfn280af5q}) + '\n')
        self.proc.stdin.flush()

    def xne5s4oipf7nf8lj2gktrz(self, n0v9hd53y60ht87jgv76pv, bxylzq8omwu9ad96l0erxr=None):
        l00ljgmtdrqfoa1we8r66k = self.wlxembuljv2qmtbb69rwex('tools/call', {'name': n0v9hd53y60ht87jgv76pv, 'arguments': bxylzq8omwu9ad96l0erxr or {}})
        penr8j5amykzf4pz5pkt9n = l00ljgmtdrqfoa1we8r66k['result']
        aib5yi139nkkxvnldh0wjj = penr8j5amykzf4pz5pkt9n['content'][0]['text']
        if penr8j5amykzf4pz5pkt9n.get('isError'):
            return (True, aib5yi139nkkxvnldh0wjj)
        return (False, json.loads(aib5yi139nkkxvnldh0wjj))

    def mz6l4lt2lbfiybgon5ubmd(self):
        try:
            self.proc.stdin.close()
            self.proc.wait(timeout=5)
        except Exception:
            self.proc.kill()

class fa6y94qnd8zvxjf0vp36b6(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name).resolve()
        self.server = k2qargg4sjxl1nj8en8t98(self.dir)
        rrcejz37yfah43yuda8tl9 = self.server.wlxembuljv2qmtbb69rwex('initialize', {'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 'tests', 'version': '0'}})
        self.init = rrcejz37yfah43yuda8tl9['result']
        self.server.xca160sphuc218o5fwh2gu('notifications/initialized')

    def tearDown(self):
        self.server.mz6l4lt2lbfiybgon5ubmd()
        self.tmp.cleanup()

    def testi6048ikehx6r77bse9(self):
        self.assertEqual(self.init['protocolVersion'], '2025-06-18')
        self.assertEqual(self.init['serverInfo']['name'], 'muse-terminal-commander')

    def testd04qff59mf3m1f0fgk(self):
        fr2s5frcgcvvwv3k7qqdhz = self.server.wlxembuljv2qmtbb69rwex('tools/list')
        cf9oc0ufzjrvmyif60cpzj = {ltg0w3hsmq30c3pkdg8gjb['name'] for ltg0w3hsmq30c3pkdg8gjb in fr2s5frcgcvvwv3k7qqdhz['result']['tools']}
        self.assertEqual(len(cf9oc0ufzjrvmyif60cpzj), 25)
        self.assertIn('execute_command', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('kill_process', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('clean_temp', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('index_files', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('search_index', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('verify_audit', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('capture_baseline', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('check_baseline', cf9oc0ufzjrvmyif60cpzj)
        self.assertIn('sniff_log', cf9oc0ufzjrvmyif60cpzj)

    def testl2h9u9mg9va0iz2g93(self):
        ni94or9i1qpadk4aelo2te = str(self.dir / 'notes' / 'hello.txt')
        janno74b7lp887f47pm23s, pbtgey59hxl2jd25gk87su = self.server.xne5s4oipf7nf8lj2gktrz('write_file', {'path': ni94or9i1qpadk4aelo2te, 'content': 'ola mundo'})
        self.assertFalse(janno74b7lp887f47pm23s)
        self.assertEqual(pbtgey59hxl2jd25gk87su['bytes'], 9)
        janno74b7lp887f47pm23s, pbtgey59hxl2jd25gk87su = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': ni94or9i1qpadk4aelo2te})
        self.assertFalse(janno74b7lp887f47pm23s)
        self.assertEqual(pbtgey59hxl2jd25gk87su['content'], 'ola mundo')

    def testtlkaxr8zkt4b964drw(self):
        qb26ej1tcxex06cfk0hsu8 = str(self.dir / 'a.txt')
        self.server.xne5s4oipf7nf8lj2gktrz('write_file', {'path': qb26ej1tcxex06cfk0hsu8, 'content': 'um dois tres'})
        dtmmimwmt3t633bohkij5o, dzbw79fb5ystuz139ra0x0 = self.server.xne5s4oipf7nf8lj2gktrz('edit_file', {'path': qb26ej1tcxex06cfk0hsu8, 'old_text': 'dois', 'new_text': 'DOIS'})
        self.assertFalse(dtmmimwmt3t633bohkij5o)
        self.assertEqual(dzbw79fb5ystuz139ra0x0['replacements'], 1)
        h8njqm1mg6wrg42j8xvhz0, dzbw79fb5ystuz139ra0x0 = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': qb26ej1tcxex06cfk0hsu8})
        self.assertEqual(dzbw79fb5ystuz139ra0x0['content'], 'um DOIS tres')

    def testyjb6jcxc0t4b7erugr(self):
        bgd5b57iy2vudg0sc370h0 = str(self.dir / 'b.txt')
        self.server.xne5s4oipf7nf8lj2gktrz('write_file', {'path': bgd5b57iy2vudg0sc370h0, 'content': 'x x x'})
        qdvnkoszfkxhixvti8xfqy, uxlknpighpd37x7wtk4epy = self.server.xne5s4oipf7nf8lj2gktrz('edit_file', {'path': bgd5b57iy2vudg0sc370h0, 'old_text': 'x', 'new_text': 'y'})
        self.assertTrue(qdvnkoszfkxhixvti8xfqy)
        self.assertIn('3 vezes', uxlknpighpd37x7wtk4epy)

    def testhjcqd3rsieww4ri9nu(self):
        d19ip8bb613rt7wuzo89bq, hsuvjzay84ye2xfsog3h7e = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': '/etc/hostname'})
        self.assertTrue(d19ip8bb613rt7wuzo89bq)
        self.assertIn('fora do escopo', hsuvjzay84ye2xfsog3h7e)

    def testfg6bjx80s6ecnd05i6(self):
        wf7unrx50yfad40n12hkup = str(self.dir / 'sub')
        sw71aybjme3oa5k5ij1h1v, j652aqx1gnrk51o3ea89wo = self.server.xne5s4oipf7nf8lj2gktrz('create_directory', {'path': wf7unrx50yfad40n12hkup})
        self.assertFalse(sw71aybjme3oa5k5ij1h1v)
        self.server.xne5s4oipf7nf8lj2gktrz('write_file', {'path': wf7unrx50yfad40n12hkup + '/f.txt', 'content': '1'})
        sw71aybjme3oa5k5ij1h1v, spixqc2yyx7qix97g37wxz = self.server.xne5s4oipf7nf8lj2gktrz('list_directory', {'path': str(self.dir)})
        self.assertFalse(sw71aybjme3oa5k5ij1h1v)
        hpcqlugpva0hwiz2n23if6 = [bilctqkhxm8zp735htiqdq['name'] for bilctqkhxm8zp735htiqdq in spixqc2yyx7qix97g37wxz['entries']]
        self.assertIn('sub', hpcqlugpva0hwiz2n23if6)

    def testldttc1pofdsxdywonh(self):
        qx69qm1bxwfycgkd7qzsku = str(self.dir / 'full')
        self.server.xne5s4oipf7nf8lj2gktrz('create_directory', {'path': qx69qm1bxwfycgkd7qzsku})
        self.server.xne5s4oipf7nf8lj2gktrz('write_file', {'path': qx69qm1bxwfycgkd7qzsku + '/f.txt', 'content': '1'})
        pcnn8hb9ck585nb25nf074, rbwqhg6c585vokwkuo8lpe = self.server.xne5s4oipf7nf8lj2gktrz('delete_path', {'path': qx69qm1bxwfycgkd7qzsku})
        self.assertFalse(pcnn8hb9ck585nb25nf074)
        self.assertEqual(rbwqhg6c585vokwkuo8lpe['deleted'], 'directory')
        self.assertFalse(Path(qx69qm1bxwfycgkd7qzsku).exists())

    def testyq49jfjnmgw7erpdki(self):
        rjrziy1qols377r5cbpopj = k2qargg4sjxl1nj8en8t98(self.dir, st0xc8gkthu6tvtib5ug30={'audit_log': str(self.dir / 'audit-defaults.log')})
        try:
            rjrziy1qols377r5cbpopj.wlxembuljv2qmtbb69rwex('initialize', {'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 't', 'version': '0'}})
            ur8abi2lrzsf9kvszlax9p, ogl5qgrl335wuabmvf8nwj = rjrziy1qols377r5cbpopj.xne5s4oipf7nf8lj2gktrz('read_file', {'path': '/etc/hosts'})
            self.assertFalse(ur8abi2lrzsf9kvszlax9p)
            self.assertTrue(ogl5qgrl335wuabmvf8nwj['content'].strip())
            ur8abi2lrzsf9kvszlax9p, ogl5qgrl335wuabmvf8nwj = rjrziy1qols377r5cbpopj.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'echo full-access'})
            self.assertFalse(ur8abi2lrzsf9kvszlax9p)
            self.assertIn('full-access', ogl5qgrl335wuabmvf8nwj['stdout'])
            ur8abi2lrzsf9kvszlax9p, hiywgkhdp7bsfs99j1lbms = rjrziy1qols377r5cbpopj.xne5s4oipf7nf8lj2gktrz('delete_path', {'path': '/'})
            self.assertTrue(ur8abi2lrzsf9kvszlax9p)
            self.assertIn('raiz', hiywgkhdp7bsfs99j1lbms)
        finally:
            rjrziy1qols377r5cbpopj.mz6l4lt2lbfiybgon5ubmd()

    def testqeoaq9hhe2h7mb3k67(self):
        sj6d9stq7q2d3jnrdgw9rb = str(self.dir / 'old.py')
        w8hkz22fmdv4s8co1rkm4z = str(self.dir / 'pkg' / 'new.py')
        self.server.xne5s4oipf7nf8lj2gktrz('write_file', {'path': sj6d9stq7q2d3jnrdgw9rb, 'content': 'print(1)'})
        gqw2pl2f4brc3wtzvnxh94, dgyy87cvdnvdfptt3qaowq = self.server.xne5s4oipf7nf8lj2gktrz('move_file', {'source': sj6d9stq7q2d3jnrdgw9rb, 'destination': w8hkz22fmdv4s8co1rkm4z})
        self.assertFalse(gqw2pl2f4brc3wtzvnxh94)
        gqw2pl2f4brc3wtzvnxh94, eylctxac23a1ggqxgoayiy = self.server.xne5s4oipf7nf8lj2gktrz('get_file_info', {'path': w8hkz22fmdv4s8co1rkm4z})
        self.assertFalse(gqw2pl2f4brc3wtzvnxh94)
        self.assertEqual(eylctxac23a1ggqxgoayiy['size'], 8)
        gqw2pl2f4brc3wtzvnxh94, vmwyfar4nw8fik0ievwnqw = self.server.xne5s4oipf7nf8lj2gktrz('search_files', {'root': str(self.dir), 'pattern': '**/*.py'})
        self.assertFalse(gqw2pl2f4brc3wtzvnxh94)
        self.assertEqual(vmwyfar4nw8fik0ievwnqw['count'], 1)
        self.assertTrue(vmwyfar4nw8fik0ievwnqw['results'][0].endswith('new.py'))

    def testacgt38toz43rgx92f4(self):
        dno99uow33cq46b9fpwif3, aadysw7uwz3z2opr8ctt6t = self.server.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'echo hello-mcp'})
        self.assertFalse(dno99uow33cq46b9fpwif3)
        self.assertEqual(aadysw7uwz3z2opr8ctt6t['exit_code'], 0)
        self.assertIn('hello-mcp', aadysw7uwz3z2opr8ctt6t['stdout'])

    def testjr5u7kgzdp9hf7beqk(self):
        yx90whfbg5egwu2dv4me1o, f0jigi4yhvd68dta9ms5q9 = self.server.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'rm -rf /'})
        self.assertTrue(yx90whfbg5egwu2dv4me1o)
        self.assertIn('bloqueado', f0jigi4yhvd68dta9ms5q9)

    def testhjv2hlxk6eq5k9t9d8(self):
        c2y360w7noqnx5064bp95b, lv19y42f7ct1thqgksg7wf = self.server.xne5s4oipf7nf8lj2gktrz('list_processes')
        self.assertFalse(c2y360w7noqnx5064bp95b)
        self.assertGreater(lv19y42f7ct1thqgksg7wf['count'], 0)
        self.assertIn('pid', lv19y42f7ct1thqgksg7wf['processes'][0])

    def testr5djwg2yuo0ek7h3ww(self):
        hj2wo2gqt8j78yetd8xxd3 = subprocess.Popen(['sleep', '60'])
        try:
            cb97up4b8hfroiqtwrbunu, zwo9g30ujpjsr0t0m3znfq = self.server.xne5s4oipf7nf8lj2gktrz('kill_process', {'pid': hj2wo2gqt8j78yetd8xxd3.pid})
            self.assertFalse(cb97up4b8hfroiqtwrbunu)
            v9g6hxdrqef9k6om7ejmkr = time.time() + 5
            while hj2wo2gqt8j78yetd8xxd3.poll() is None and time.time() < v9g6hxdrqef9k6om7ejmkr:
                time.sleep(0.1)
            self.assertIsNotNone(hj2wo2gqt8j78yetd8xxd3.poll())
        finally:
            if hj2wo2gqt8j78yetd8xxd3.poll() is None:
                hj2wo2gqt8j78yetd8xxd3.kill()

    def testul9o9rf2o0wg2fs02c(self):
        bjpwgs5pnrzotjizpvq999, fvgwud4kbns125a7r9zbx3 = self.server.xne5s4oipf7nf8lj2gktrz('kill_process', {'pid': self.server.proc.pid})
        self.assertTrue(bjpwgs5pnrzotjizpvq999)
        self.assertIn('si mesmo', fvgwud4kbns125a7r9zbx3)

    def testf260cuxc5jg9c5tq08(self):
        self.server.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'true'})
        ve9olt0gfcgf267gsbzev9 = (self.dir / 'audit.log').read_text(encoding='utf-8')
        icgdtk7r7625wsija48daa = [json.loads(lqvyn8itjvz2znuhzwfhlg) for lqvyn8itjvz2znuhzwfhlg in ve9olt0gfcgf267gsbzev9.splitlines() if lqvyn8itjvz2znuhzwfhlg.strip()]
        self.assertTrue(any((vqedwmlf4rrbujnfnxs640['tool'] == 'execute_command' and vqedwmlf4rrbujnfnxs640['ok'] for vqedwmlf4rrbujnfnxs640 in icgdtk7r7625wsija48daa)))

    def hs6tzorw91p5xkli6rcsui(self):
        yi1h5cw4bwgu3qodvykfd9 = self.dir / 'residue'
        (yi1h5cw4bwgu3qodvykfd9 / 'sub').mkdir(parents=True)
        (yi1h5cw4bwgu3qodvykfd9 / 'a.log').write_bytes(b'12345')
        (yi1h5cw4bwgu3qodvykfd9 / 'sub' / 'b.tmp').write_bytes(b'123')
        return str(yi1h5cw4bwgu3qodvykfd9)

    def testt1m1lre96urgz2asuw(self):
        j4iy7ay39mhj81q546zdid = self.hs6tzorw91p5xkli6rcsui()
        ube6qmlg7nh3dekbpotz64, soxfflcorzl1a70r27m563 = self.server.xne5s4oipf7nf8lj2gktrz('clean_temp', {'paths': [j4iy7ay39mhj81q546zdid]})
        self.assertFalse(ube6qmlg7nh3dekbpotz64)
        self.assertTrue(soxfflcorzl1a70r27m563['dry_run'])
        self.assertEqual(soxfflcorzl1a70r27m563['total']['files'], 2)
        self.assertEqual(soxfflcorzl1a70r27m563['total']['bytes'], 8)
        self.assertEqual(soxfflcorzl1a70r27m563['total']['deleted'], 0)
        self.assertTrue(Path(j4iy7ay39mhj81q546zdid, 'a.log').exists())

    def testr7ceo30el9fv1qr0u7(self):
        zrdxjimvu5fvwbax4qhnjw = self.hs6tzorw91p5xkli6rcsui()
        drdwvmtcpjom1q9eh8lu8v, x0b5yla7brqlrhb07grb34 = self.server.xne5s4oipf7nf8lj2gktrz('clean_temp', {'paths': [zrdxjimvu5fvwbax4qhnjw], 'dry_run': False})
        self.assertFalse(drdwvmtcpjom1q9eh8lu8v)
        self.assertEqual(x0b5yla7brqlrhb07grb34['total']['deleted'], 2)
        self.assertEqual(x0b5yla7brqlrhb07grb34['total']['freed_bytes'], 8)
        self.assertFalse(Path(zrdxjimvu5fvwbax4qhnjw, 'a.log').exists())
        self.assertTrue(Path(zrdxjimvu5fvwbax4qhnjw).is_dir())

    def testuqc3ojsrqpfttyp34t(self):
        cyx5pcolj1sq6guok3otk9 = self.dir / 'big.txt'
        cyx5pcolj1sq6guok3otk9.write_bytes(b'a' * (2 * 1024 * 1024))
        ow1e41bj9hbljeym6xry0x, ewq3vtukm3ms13fw37gpt7 = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': str(cyx5pcolj1sq6guok3otk9)})
        self.assertFalse(ow1e41bj9hbljeym6xry0x)
        self.assertTrue(ewq3vtukm3ms13fw37gpt7['truncated'])
        self.assertEqual(ewq3vtukm3ms13fw37gpt7['bytes'], 2 * 1024 * 1024)
        self.assertEqual(len(ewq3vtukm3ms13fw37gpt7['content'].encode('utf-8')), 1048576)

    def testpvvc0ky0xjbtdv9zs4(self):
        x3frb5q6wkpb81ip9ovm9e = k2qargg4sjxl1nj8en8t98(self.dir, st0xc8gkthu6tvtib5ug30={'allowed_directories': [str(self.dir)], 'audit_log': str(self.dir / 'audit2.log'), 'max_read_bytes': 50000000})
        try:
            x3frb5q6wkpb81ip9ovm9e.wlxembuljv2qmtbb69rwex('initialize', {'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 't', 'version': '0'}})
            o2uewamev8mc7gpothatzj = self.dir / 'big2.txt'
            o2uewamev8mc7gpothatzj.write_bytes(b'b' * (2 * 1024 * 1024))
            xhhtxvoqezqvx725p585pf, as4cczb3d3oop4ih8a6chm = x3frb5q6wkpb81ip9ovm9e.xne5s4oipf7nf8lj2gktrz('read_file', {'path': str(o2uewamev8mc7gpothatzj)})
            self.assertFalse(xhhtxvoqezqvx725p585pf)
            self.assertEqual(len(as4cczb3d3oop4ih8a6chm['content'].encode('utf-8')), 1048576)
        finally:
            x3frb5q6wkpb81ip9ovm9e.mz6l4lt2lbfiybgon5ubmd()

    def testlna9mbofsyfds2hr4i(self):
        bzf7hddyst6tp15dscyd6t, z21wi7s4ldsve81tghqz8e = self.server.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'python3 -c "print(\'é\' * 100000)"'})
        self.assertFalse(bzf7hddyst6tp15dscyd6t)
        self.assertTrue(z21wi7s4ldsve81tghqz8e['truncated'])
        self.assertLessEqual(len(z21wi7s4ldsve81tghqz8e['stdout'].encode('utf-8')), 65536)

    def testlf5uk1kotd6uczxdvl(self):
        for s1x1b5wvo1k31n54i82mvu in range(210):
            (self.dir / ('f%03d.txt' % s1x1b5wvo1k31n54i82mvu)).write_text('x', encoding='utf-8')
        hmg0ta6wdcrilk8lgblqiq, chs4urnpj10o6nfwg9l0qk = self.server.xne5s4oipf7nf8lj2gktrz('search_files', {'root': str(self.dir), 'pattern': '*.txt', 'max_results': 999})
        self.assertFalse(hmg0ta6wdcrilk8lgblqiq)
        self.assertEqual(chs4urnpj10o6nfwg9l0qk['count'], 200)

    def testlt1i16uwlfpnuowl8w(self):
        import importlib.util
        i6f2a3l2u3k2efqefan4jt = importlib.util.spec_from_file_location('srv_mod', SERVER)
        hght4flx9p5ol9v43hkf8s = importlib.util.module_from_spec(i6f2a3l2u3k2efqefan4jt)
        i6f2a3l2u3k2efqefan4jt.loader.exec_module(hght4flx9p5ol9v43hkf8s)
        self.assertEqual(hght4flx9p5ol9v43hkf8s.luzso6wcodee5z4cdau6ld(-5, 120, 600), 120)
        self.assertEqual(hght4flx9p5ol9v43hkf8s.luzso6wcodee5z4cdau6ld(0, 120, 600), 120)
        self.assertEqual(hght4flx9p5ol9v43hkf8s.luzso6wcodee5z4cdau6ld(30, 120, 600), 30)
        self.assertEqual(hght4flx9p5ol9v43hkf8s.luzso6wcodee5z4cdau6ld(5000, 120, 600), 600)
        self.assertEqual(hght4flx9p5ol9v43hkf8s.am2lity5ynwqh4swnl8y6j(10000), 600)
        self.assertEqual(hght4flx9p5ol9v43hkf8s.am2lity5ynwqh4swnl8y6j(-1), hght4flx9p5ol9v43hkf8s.DEFAULT_COMMAND_TIMEOUT)

    def c93obobzpb654gyvaglhlo(self, lv089lkmpge5z4o2zny666='fts.db'):
        return str(self.dir / lv089lkmpge5z4o2zny666)

    def testnz5m85epzfsz8rz1kp(self):
        d69n5yh86tl7ifmq25fmgi = self.dir / 'docs'
        d69n5yh86tl7ifmq25fmgi.mkdir()
        (d69n5yh86tl7ifmq25fmgi / 'a.txt').write_text('o log registrou um erro critico no servico', encoding='utf-8')
        r1zysvo9s8iubed7kxe5z6 = d69n5yh86tl7ifmq25fmgi / 'sub'
        r1zysvo9s8iubed7kxe5z6.mkdir()
        (r1zysvo9s8iubed7kxe5z6 / 'b.txt').write_text('tudo certo, zebra listrada', encoding='utf-8')
        ucgioq8bmqana4rl1qby7q = self.c93obobzpb654gyvaglhlo()
        tyxs92tcig3u7g08xhfrmz, opvzj29gi4k2stcowajjbx = self.server.xne5s4oipf7nf8lj2gktrz('index_files', {'paths': [str(d69n5yh86tl7ifmq25fmgi)], 'index_path': ucgioq8bmqana4rl1qby7q})
        self.assertFalse(tyxs92tcig3u7g08xhfrmz)
        self.assertEqual(opvzj29gi4k2stcowajjbx['files'], 2)
        tyxs92tcig3u7g08xhfrmz, opvzj29gi4k2stcowajjbx = self.server.xne5s4oipf7nf8lj2gktrz('search_index', {'query': 'zebra', 'index_path': ucgioq8bmqana4rl1qby7q})
        self.assertFalse(tyxs92tcig3u7g08xhfrmz)
        self.assertEqual(opvzj29gi4k2stcowajjbx['count'], 1)
        self.assertTrue(opvzj29gi4k2stcowajjbx['results'][0]['path'].endswith('b.txt'))
        tyxs92tcig3u7g08xhfrmz, opvzj29gi4k2stcowajjbx = self.server.xne5s4oipf7nf8lj2gktrz('search_index', {'query': 'erro', 'index_path': ucgioq8bmqana4rl1qby7q})
        self.assertFalse(tyxs92tcig3u7g08xhfrmz)
        self.assertEqual(opvzj29gi4k2stcowajjbx['count'], 1)

    def testb66rdityv2u1l2kulh(self):
        caygh9kq482fmlspiyvjgz = self.dir / 'docs'
        caygh9kq482fmlspiyvjgz.mkdir()
        l2myqv43zomhcm29h8t7c2 = caygh9kq482fmlspiyvjgz / 'c.txt'
        l2myqv43zomhcm29h8t7c2.write_text('zebra unica', encoding='utf-8')
        tkxnge68z1u89jtd563986 = self.c93obobzpb654gyvaglhlo()
        self.server.xne5s4oipf7nf8lj2gktrz('index_files', {'paths': [str(caygh9kq482fmlspiyvjgz)], 'index_path': tkxnge68z1u89jtd563986})
        gzuoi8kom15v2z806nh5mp, kvbdsvc7mygqtetk4zuk6a = self.server.xne5s4oipf7nf8lj2gktrz('search_index', {'query': 'zebra', 'index_path': tkxnge68z1u89jtd563986})
        self.assertEqual(kvbdsvc7mygqtetk4zuk6a['count'], 1)
        l2myqv43zomhcm29h8t7c2.unlink()
        self.server.xne5s4oipf7nf8lj2gktrz('index_files', {'paths': [str(caygh9kq482fmlspiyvjgz)], 'index_path': tkxnge68z1u89jtd563986})
        gzuoi8kom15v2z806nh5mp, kvbdsvc7mygqtetk4zuk6a = self.server.xne5s4oipf7nf8lj2gktrz('search_index', {'query': 'zebra', 'index_path': tkxnge68z1u89jtd563986})
        self.assertFalse(gzuoi8kom15v2z806nh5mp)
        self.assertEqual(kvbdsvc7mygqtetk4zuk6a['count'], 0)

    def testz1i7rm519xtj9zj0yf(self):
        for r3ejh7fp45ppednq2w7dur in range(210):
            (self.dir / ('d%03d.txt' % r3ejh7fp45ppednq2w7dur)).write_text('termo comum em todos', encoding='utf-8')
        klegou0vbl9cfdj17h5ry6 = self.c93obobzpb654gyvaglhlo()
        self.server.xne5s4oipf7nf8lj2gktrz('index_files', {'paths': [str(self.dir)], 'index_path': klegou0vbl9cfdj17h5ry6})
        rzzyh6umgl392iyt69m76a, j6zasshhjsbgupee9dos7v = self.server.xne5s4oipf7nf8lj2gktrz('search_index', {'query': 'comum', 'limit': 999, 'index_path': klegou0vbl9cfdj17h5ry6})
        self.assertFalse(rzzyh6umgl392iyt69m76a)
        self.assertEqual(j6zasshhjsbgupee9dos7v['count'], 200)

    def testtnjvpa7yzg5uk8idnz(self):
        (self.dir / 'e.txt').write_text('conteudo qualquer', encoding='utf-8')
        ou04ykbezf832oe0569qja = self.c93obobzpb654gyvaglhlo()
        self.server.xne5s4oipf7nf8lj2gktrz('index_files', {'paths': [str(self.dir)], 'index_path': ou04ykbezf832oe0569qja})
        nbcoq1qn84uomt4xachx81, bymvym6bc1erfsiytvkjar = self.server.xne5s4oipf7nf8lj2gktrz('search_index', {'query': '"abc', 'index_path': ou04ykbezf832oe0569qja})
        self.assertTrue(nbcoq1qn84uomt4xachx81)

    def testfxzs8yrxdl654y9080(self):
        self.server.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'true'})
        self.server.xne5s4oipf7nf8lj2gktrz('write_file', {'path': str(self.dir / 'x.txt'), 'content': 'y'})
        kcspvibzdz9cbmzgu3yjrk, ple2w54t2phh625a2ubp9h = self.server.xne5s4oipf7nf8lj2gktrz('verify_audit', {})
        self.assertFalse(kcspvibzdz9cbmzgu3yjrk)
        self.assertTrue(ple2w54t2phh625a2ubp9h['valid'])
        self.assertIsNone(ple2w54t2phh625a2ubp9h['broken_at'])
        self.assertGreaterEqual(ple2w54t2phh625a2ubp9h['entries'], 2)

    def testiqrdpqxwx7wjteopf1(self):
        self.server.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'true'})
        y2l75ghw5s3gjn9hijul72 = self.dir / 'audit.log'
        with y2l75ghw5s3gjn9hijul72.open('a', encoding='utf-8') as lpkh9ijmy56k4d9hvdwzbt:
            lpkh9ijmy56k4d9hvdwzbt.write('{"ts":"x","tool":"invasor","summary":{},"ok":true,"prev_hash":"","hash":"falso"}\n')
        le0o1dvy0w76mm0mtq566y, u0ea3p25gjw3ck7gp208nz = self.server.xne5s4oipf7nf8lj2gktrz('verify_audit', {})
        self.assertFalse(le0o1dvy0w76mm0mtq566y)
        self.assertFalse(u0ea3p25gjw3ck7gp208nz['valid'])
        self.assertIsNotNone(u0ea3p25gjw3ck7gp208nz['broken_at'])

    def testpp62rdwpifwtexdmlp(self):
        gbyd9uhuh84akzeyvbv1l4, xai7za03auz9sbelg22pii = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': 123})
        self.assertTrue(gbyd9uhuh84akzeyvbv1l4)
        self.assertIn('deve ser do tipo', xai7za03auz9sbelg22pii)

    def testkt4i9y7xkhcbw1bxpa(self):
        uoecv1mhe4cbotfkic17ff = self.dir / 'tree'
        uoecv1mhe4cbotfkic17ff.mkdir()
        (uoecv1mhe4cbotfkic17ff / 'a.txt').write_text('alfa', encoding='utf-8')
        (uoecv1mhe4cbotfkic17ff / 'b.txt').write_text('beta', encoding='utf-8')
        wm3fy0k3mcwol8mgydo2vh = str(self.dir / 'base.json')
        pri6edscdobuweh8f4gb9i, f14wdkcfcfkguqa6mqo8gn = self.server.xne5s4oipf7nf8lj2gktrz('capture_baseline', {'paths': [str(uoecv1mhe4cbotfkic17ff)], 'baseline_path': wm3fy0k3mcwol8mgydo2vh})
        self.assertFalse(pri6edscdobuweh8f4gb9i, f14wdkcfcfkguqa6mqo8gn)
        self.assertEqual(f14wdkcfcfkguqa6mqo8gn['files'], 2)
        pri6edscdobuweh8f4gb9i, f14wdkcfcfkguqa6mqo8gn = self.server.xne5s4oipf7nf8lj2gktrz('check_baseline', {'baseline_path': wm3fy0k3mcwol8mgydo2vh})
        self.assertFalse(pri6edscdobuweh8f4gb9i, f14wdkcfcfkguqa6mqo8gn)
        self.assertTrue(f14wdkcfcfkguqa6mqo8gn['valid'])

    def testrzx3c4brurzfj5j8jp(self):
        rzok10b4sv1c906ga4jefm = self.dir / 'tree'
        rzok10b4sv1c906ga4jefm.mkdir()
        sh7oqqji6mkq7pehawpjca = rzok10b4sv1c906ga4jefm / 'a.txt'
        sh7oqqji6mkq7pehawpjca.write_text('alfa', encoding='utf-8')
        gxs40ctzr99wbmb4fgobxd = str(self.dir / 'base.json')
        self.server.xne5s4oipf7nf8lj2gktrz('capture_baseline', {'paths': [str(rzok10b4sv1c906ga4jefm)], 'baseline_path': gxs40ctzr99wbmb4fgobxd})
        sh7oqqji6mkq7pehawpjca.write_text('ALTERADO', encoding='utf-8')
        (rzok10b4sv1c906ga4jefm / 'novo.txt').write_text('novo', encoding='utf-8')
        kzrth4izgix9mj03672627, hiqoe9t1jdx21kwz2nzn3g = self.server.xne5s4oipf7nf8lj2gktrz('check_baseline', {'baseline_path': gxs40ctzr99wbmb4fgobxd})
        self.assertFalse(kzrth4izgix9mj03672627, hiqoe9t1jdx21kwz2nzn3g)
        self.assertFalse(hiqoe9t1jdx21kwz2nzn3g['valid'])
        self.assertIn(str(sh7oqqji6mkq7pehawpjca), hiqoe9t1jdx21kwz2nzn3g['files_changed'])
        self.assertEqual(len(hiqoe9t1jdx21kwz2nzn3g['files_added']), 1)

    def testvqbzik6ikj7ovk63st(self):
        htwld3hzfozy38ybtg65bv = {'allowed_directories': [str(self.dir)], 'audit_log': str(self.dir / 'rot' / 'audit.log'), 'audit_log_max_bytes': 1024}
        xq9zwcmvdyznw1pdglvl6u = k2qargg4sjxl1nj8en8t98(self.dir, st0xc8gkthu6tvtib5ug30=htwld3hzfozy38ybtg65bv)
        try:
            for z23n2zo1x567z2h9yi1lk8 in range(5):
                xq9zwcmvdyznw1pdglvl6u.xne5s4oipf7nf8lj2gktrz('execute_command', {'command': 'true'})
            reuc5k2aj5li3jrrlgqe82, ugdxk9b7tlqonrt6x494er = xq9zwcmvdyznw1pdglvl6u.xne5s4oipf7nf8lj2gktrz('verify_audit', {})
            self.assertFalse(reuc5k2aj5li3jrrlgqe82, ugdxk9b7tlqonrt6x494er)
            self.assertTrue(ugdxk9b7tlqonrt6x494er['valid'])
            r2cc54x9zff2a1bd76ucg4 = self.dir / 'rot'
            j0ywbxxue06lwo3t0iexrc = [sbni4i6d0ibt5qz12a37th for sbni4i6d0ibt5qz12a37th in r2cc54x9zff2a1bd76ucg4.glob('*.bak')]
            self.assertGreaterEqual(len(j0ywbxxue06lwo3t0iexrc), 1)
        finally:
            xq9zwcmvdyznw1pdglvl6u.mz6l4lt2lbfiybgon5ubmd()

    def testf4wvfby3bhw6cr8t4c(self):
        ua6iry59s4ctttfxn54lbv = self.dir / 'paged.txt'
        ua6iry59s4ctttfxn54lbv.write_text('A' * 500 + 'B' * 500 + 'C' * 500, encoding='utf-8')
        zc9w9dogqvi02ebzjc6n0c, wkl1ax13kr6yqwnhf1k5dw = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': str(ua6iry59s4ctttfxn54lbv), 'offset': 500, 'limit': 500})
        self.assertFalse(zc9w9dogqvi02ebzjc6n0c, wkl1ax13kr6yqwnhf1k5dw)
        self.assertEqual(wkl1ax13kr6yqwnhf1k5dw['content'], 'B' * 500)
        self.assertEqual(wkl1ax13kr6yqwnhf1k5dw['offset'], 500)
        self.assertEqual(wkl1ax13kr6yqwnhf1k5dw['next_offset'], 1000)
        self.assertTrue(wkl1ax13kr6yqwnhf1k5dw['truncated'])
        zc9w9dogqvi02ebzjc6n0c, wkl1ax13kr6yqwnhf1k5dw = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': str(ua6iry59s4ctttfxn54lbv), 'offset': 1000, 'limit': 500})
        self.assertFalse(zc9w9dogqvi02ebzjc6n0c, wkl1ax13kr6yqwnhf1k5dw)
        self.assertEqual(wkl1ax13kr6yqwnhf1k5dw['content'], 'C' * 500)
        self.assertIsNone(wkl1ax13kr6yqwnhf1k5dw['next_offset'])
        self.assertFalse(wkl1ax13kr6yqwnhf1k5dw['truncated'])

    def testzcrkcv02t52o3hadz9(self):
        pomfhffn7pvtkucqdvmmk7 = self.dir / 'small.txt'
        pomfhffn7pvtkucqdvmmk7.write_text('abc', encoding='utf-8')
        jb9eqbeh7orhg2y5f0laqe, du1vxpdc15i1jsxjp0jjjq = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': str(pomfhffn7pvtkucqdvmmk7), 'offset': 999999})
        self.assertFalse(jb9eqbeh7orhg2y5f0laqe, du1vxpdc15i1jsxjp0jjjq)
        self.assertEqual(du1vxpdc15i1jsxjp0jjjq['content'], '')
        self.assertFalse(du1vxpdc15i1jsxjp0jjjq['truncated'])

    def testjppjtt9ddmmzbwuul6(self):
        xtescoawagjoz4vnio7yy7 = self.dir / 'big.txt'
        xtescoawagjoz4vnio7yy7.write_text('x' * 1100000, encoding='utf-8')
        ujx4piou2jbsv2d9jn4999, bkxbq72sppn4no17ctzbtz = self.server.xne5s4oipf7nf8lj2gktrz('read_file', {'path': str(xtescoawagjoz4vnio7yy7), 'limit': 9000000})
        self.assertFalse(ujx4piou2jbsv2d9jn4999, bkxbq72sppn4no17ctzbtz)
        self.assertEqual(len(bkxbq72sppn4no17ctzbtz['content']), 1048576)
        self.assertTrue(bkxbq72sppn4no17ctzbtz['truncated'])

    def testspxj72uo66npvvtduz(self):
        fmekgxcileb85te9y0mzf0 = self.dir / 'leak.csv'
        fmekgxcileb85te9y0mzf0.write_text('ts,user,action\n2026-01-02T03:04:05,alice,login\n2026-01-02T03:05:11,bob,logout\n2026-01-02T03:06:00,alice,purchase\n', encoding='utf-8')
        y0hdd0o27y2rj5wt95zwmg, vn9g0q7kdze429ajccjnti = self.server.xne5s4oipf7nf8lj2gktrz('sniff_log', {'path': str(fmekgxcileb85te9y0mzf0)})
        self.assertFalse(y0hdd0o27y2rj5wt95zwmg, vn9g0q7kdze429ajccjnti)
        self.assertEqual(vn9g0q7kdze429ajccjnti['delimiter'], ',')
        self.assertTrue(vn9g0q7kdze429ajccjnti['has_header'])
        self.assertIn('user', vn9g0q7kdze429ajccjnti['fields'])
        self.assertEqual(vn9g0q7kdze429ajccjnti['timestamp_format'], 'iso8601')
        self.assertEqual(vn9g0q7kdze429ajccjnti['total_lines'], 4)

    def testez7md69up0rzuhp3kr(self):
        i77cua3oaw29kf2tixhsy7 = self.dir / 'free.txt'
        i77cua3oaw29kf2tixhsy7.write_text('erro na conexao\ntentativa de login falhou\n', encoding='utf-8')
        t2pizdvrswp52303qb8si3, r3u4nv0bs16kp1g82xe3h8 = self.server.xne5s4oipf7nf8lj2gktrz('sniff_log', {'path': str(i77cua3oaw29kf2tixhsy7)})
        self.assertFalse(t2pizdvrswp52303qb8si3, r3u4nv0bs16kp1g82xe3h8)
        self.assertIsNone(r3u4nv0bs16kp1g82xe3h8['delimiter'])
        self.assertFalse(r3u4nv0bs16kp1g82xe3h8['has_header'])
        self.assertEqual(r3u4nv0bs16kp1g82xe3h8['total_lines'], 2)

    def testpx7k9px06si9xtz7af(self):
        gizw561yf0ounfxz5facuq = self.server.wlxembuljv2qmtbb69rwex('does/not/exist')
        self.assertEqual(gizw561yf0ounfxz5facuq['error']['code'], -32601)

class oy07j5lkaumop8rdpk54hc(unittest.TestCase):

    def testxhk1fv14wztss0d0l1(self):
        import vmmaieuzwn7j9llhbznbgs
        qfeyis4121slkbu6dume03 = [mq6p26vm0ohe0kgxxhrwhy['name'] for mq6p26vm0ohe0kgxxhrwhy in vmmaieuzwn7j9llhbznbgs.TOOLS]
        for ss7qf7rdwrbvk3rops0yka in ['screenshot', 'ui_elements', 'click', 'type_text', 'press_key', 'find_template']:
            self.assertIn(ss7qf7rdwrbvk3rops0yka, qfeyis4121slkbu6dume03)

    def testj279op6ny3grpe0egi(self):
        import vmmaieuzwn7j9llhbznbgs
        if __import__('os').name == 'nt':
            self.skipTest('so fora do Windows')
        q8c8wh8t24ieqg0yk2s5lg = [(vmmaieuzwn7j9llhbznbgs.dq1q6yif7t8ztypfxg6d8w, {}), (vmmaieuzwn7j9llhbznbgs.xj7ibzfp8gvvlj8a8jd8a6, {}), (vmmaieuzwn7j9llhbznbgs.u4gw5wnckai7pb7b1lqmdl, {'x': 1, 'y': 1}), (vmmaieuzwn7j9llhbznbgs.k1qo56pfok7nnwxdpbh2xt, {'text': 'a'}), (vmmaieuzwn7j9llhbznbgs.tcamd89fej07tsw6benjyb, {'key': 'enter'}), (vmmaieuzwn7j9llhbznbgs.s9yzkdqnbautmij4n62y3l, {'template_base64': 'x'})]
        for vob3oljod31ut9fmtuvs6f, y6480yqjdxdui91k5039ww in q8c8wh8t24ieqg0yk2s5lg:
            with self.assertRaises(vmmaieuzwn7j9llhbznbgs.qxik4i1ab3x3aozq5e8hyt, msg=vob3oljod31ut9fmtuvs6f.__name__) as p7x3kurwu5l9i5zcoy2uz7:
                vob3oljod31ut9fmtuvs6f(y6480yqjdxdui91k5039ww)
            self.assertIn('Windows', str(p7x3kurwu5l9i5zcoy2uz7.exception))

    def testkj26cg95boxedu8esg(self):
        import vmmaieuzwn7j9llhbznbgs
        with self.assertRaises(vmmaieuzwn7j9llhbznbgs.qxik4i1ab3x3aozq5e8hyt):
            vmmaieuzwn7j9llhbznbgs.tcamd89fej07tsw6benjyb({'key': 'f99'})
if __name__ == '__main__':
    unittest.main(verbosity=2)
