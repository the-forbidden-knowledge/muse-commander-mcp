import sys
import unittest
from pathlib import Path
from unittest import mock
BATCH = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BATCH))
import vmmaieuzwn7j9llhbznbgs

class wt9tii5t1364bqscz1zhxo(unittest.TestCase):

    def testqw1f2wk65u8em4pfa9(self):
        self.assertEqual(vmmaieuzwn7j9llhbznbgs.dhqoy4u44wcqwe6la8nzn2(b'hello'), 'hello')

    def testp7e0jyet09vrjzw56x(self):
        self.assertEqual(vmmaieuzwn7j9llhbznbgs.dhqoy4u44wcqwe6la8nzn2('ação'.encode('utf-8')), 'ação')

    def testckvfo6ky4lnp8ot83c(self):
        c4ok3vl7qqgftvx4it1cpz = vmmaieuzwn7j9llhbznbgs.dhqoy4u44wcqwe6la8nzn2(b'\xa1')
        self.assertIsInstance(c4ok3vl7qqgftvx4it1cpz, str)

    def testpj4rxx27qpvgtptiv1(self):
        self.assertEqual(vmmaieuzwn7j9llhbznbgs.dhqoy4u44wcqwe6la8nzn2('ação'.encode('cp1252')), 'ação')

    def testi6d1cnxwf361apbdv0(self):
        self.assertEqual(vmmaieuzwn7j9llhbznbgs.dhqoy4u44wcqwe6la8nzn2(b''), '')
        self.assertEqual(vmmaieuzwn7j9llhbznbgs.dhqoy4u44wcqwe6la8nzn2(None), '')

    def testgwycln0fb7aouk618t(self):
        self.assertEqual(vmmaieuzwn7j9llhbznbgs.dhqoy4u44wcqwe6la8nzn2('ja texto'), 'ja texto')

    def testne5nwcl1h3y806ygsq(self):
        yq8yvqt1c1f1cim2zqoavy = mock.Mock()
        yq8yvqt1c1f1cim2zqoavy.returncode = 0
        yq8yvqt1c1f1cim2zqoavy.stdout = b'Conex\xa1o estabelecida\n'
        yq8yvqt1c1f1cim2zqoavy.stderr = b''
        with mock.patch.object(vmmaieuzwn7j9llhbznbgs.subprocess, 'run', return_value=yq8yvqt1c1f1cim2zqoavy):
            g61nqazmuxs4hep1wgkf17 = vmmaieuzwn7j9llhbznbgs.kegxr3enidt00yb5gohwjd({'command': 'qualquer-coisa'})
        self.assertEqual(g61nqazmuxs4hep1wgkf17['exit_code'], 0)
        self.assertIsInstance(g61nqazmuxs4hep1wgkf17['stdout'], str)
        self.assertIn('Conex', g61nqazmuxs4hep1wgkf17['stdout'])
if __name__ == '__main__':
    unittest.main(verbosity=2)
