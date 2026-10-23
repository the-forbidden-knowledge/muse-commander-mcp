import base64
import binascii
import struct
import sys
import unittest
import zlib
from pathlib import Path
BATCH = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BATCH))
import vmmaieuzwn7j9llhbznbgs

def hribp0kwyfakrzu5339ymo(jduwq5t885wjmxsw605yas, xgssc6vjotjsc8kfi3qzt0, ok8on2i23u3bqwvulcfi81=(200, 100, 50)):
    o5xiya2l19p1wszrpsgg2y = b''.join((b'\x00' + bytes(ok8on2i23u3bqwvulcfi81) * jduwq5t885wjmxsw605yas for jzstzem0gpj2boccll87pg in range(xgssc6vjotjsc8kfi3qzt0)))
    qgbzgm3jr7yd1l16elzwn0 = struct.pack('>IIBBBBB', jduwq5t885wjmxsw605yas, xgssc6vjotjsc8kfi3qzt0, 8, 2, 0, 0, 0)
    y7sq9qiteh9qpbuiqlku8h = b''
    for emt521ug86jey9nlcawleb, ib41j8ckbtj1a6tb528v9n in [(b'IHDR', qgbzgm3jr7yd1l16elzwn0), (b'IDAT', zlib.compress(o5xiya2l19p1wszrpsgg2y)), (b'IEND', b'')]:
        y7sq9qiteh9qpbuiqlku8h += struct.pack('>I', len(ib41j8ckbtj1a6tb528v9n)) + emt521ug86jey9nlcawleb + ib41j8ckbtj1a6tb528v9n
        y7sq9qiteh9qpbuiqlku8h += struct.pack('>I', binascii.crc32(emt521ug86jey9nlcawleb + ib41j8ckbtj1a6tb528v9n) & 4294967295)
    return b'\x89PNG\r\n\x1a\n' + y7sq9qiteh9qpbuiqlku8h

class p4zpil4plwzneljvsu8wnh(unittest.TestCase):

    def setUp(self):
        self._real_powershell = vmmaieuzwn7j9llhbznbgs.s11e7vtjt2uk0b1coynaih

    def tearDown(self):
        vmmaieuzwn7j9llhbznbgs.s11e7vtjt2uk0b1coynaih = self._real_powershell

    def m0ptodkqh436122250z6nc(self, gkbo29w9mqr0e6zbljceub):
        vmmaieuzwn7j9llhbznbgs.s11e7vtjt2uk0b1coynaih = lambda ne74bcyvpcm2rp9lw7roar, s8du7a67izes7tezdzapki=90: gkbo29w9mqr0e6zbljceub

    def testynke1m1pa51oickije(self):
        nio5xh9hu5wbjx5tb9w7hi = hribp0kwyfakrzu5339ymo(1366, 768)
        self.m0ptodkqh436122250z6nc(base64.b64encode(nio5xh9hu5wbjx5tb9w7hi).decode('ascii'))
        hyuch7oppsxuvl4z6thz37 = vmmaieuzwn7j9llhbznbgs.dq1q6yif7t8ztypfxg6d8w({})
        self.assertTrue(hyuch7oppsxuvl4z6thz37['ok'])
        self.assertEqual(hyuch7oppsxuvl4z6thz37['width'], 1366)
        self.assertEqual(hyuch7oppsxuvl4z6thz37['height'], 768)
        self.assertEqual(hyuch7oppsxuvl4z6thz37['png_bytes'], len(nio5xh9hu5wbjx5tb9w7hi))
        self.assertIn('png_base64', hyuch7oppsxuvl4z6thz37)

    def testhwopngk277wnesut4c(self):
        q2kuenvgo7uh7jiioxh35j = bytearray(hribp0kwyfakrzu5339ymo(64, 64))
        q2kuenvgo7uh7jiioxh35j[0] = 0
        self.m0ptodkqh436122250z6nc(base64.b64encode(bytes(q2kuenvgo7uh7jiioxh35j)).decode('ascii'))
        with self.assertRaises(vmmaieuzwn7j9llhbznbgs.qxik4i1ab3x3aozq5e8hyt) as qj5uhig1obwb5deq9itsxi:
            vmmaieuzwn7j9llhbznbgs.dq1q6yif7t8ztypfxg6d8w({})
        self.assertIn('PNG', str(qj5uhig1obwb5deq9itsxi.exception))

    def testjq4ze49mx62jy7e68u(self):
        nvatiadyy50rx3uqcl4xc3 = hribp0kwyfakrzu5339ymo(64, 64)[:20]
        self.m0ptodkqh436122250z6nc(base64.b64encode(nvatiadyy50rx3uqcl4xc3).decode('ascii'))
        with self.assertRaises(vmmaieuzwn7j9llhbznbgs.qxik4i1ab3x3aozq5e8hyt):
            vmmaieuzwn7j9llhbznbgs.dq1q6yif7t8ztypfxg6d8w({})

    def testuo6moc3vugdp0grmat(self):
        self.m0ptodkqh436122250z6nc('!!!nao-e-base64!!!')
        with self.assertRaises(vmmaieuzwn7j9llhbznbgs.qxik4i1ab3x3aozq5e8hyt) as c1mra14c0tcqw160w9cyjv:
            vmmaieuzwn7j9llhbznbgs.dq1q6yif7t8ztypfxg6d8w({})
        self.assertIn('base64', str(c1mra14c0tcqw160w9cyjv.exception))

    def testgf9ppyzy9k4hqvdzjw(self):
        r5erc5j2blvff0cwjm5z2l = hribp0kwyfakrzu5339ymo(64, 64)
        pc2iaxgh4pqghmoaoufspj = r5erc5j2blvff0cwjm5z2l[:12] + b'XXXX' + r5erc5j2blvff0cwjm5z2l[16:]
        self.m0ptodkqh436122250z6nc(base64.b64encode(pc2iaxgh4pqghmoaoufspj).decode('ascii'))
        with self.assertRaises(vmmaieuzwn7j9llhbznbgs.qxik4i1ab3x3aozq5e8hyt):
            vmmaieuzwn7j9llhbznbgs.dq1q6yif7t8ztypfxg6d8w({})

    def testjp6jw5fc3m1sqef4u8(self):
        tksq9i5llq95gmzlkjhudf = hribp0kwyfakrzu5339ymo(1366, 768)
        self.m0ptodkqh436122250z6nc(base64.b64encode(tksq9i5llq95gmzlkjhudf).decode('ascii'))
        sqc1v87ozwdz7navbnepl9 = vmmaieuzwn7j9llhbznbgs.dq1q6yif7t8ztypfxg6d8w({'compress': True})
        self.assertEqual(sqc1v87ozwdz7navbnepl9['compression'], 'zlib')
        self.assertNotIn('png_base64', sqc1v87ozwdz7navbnepl9)
        flfar523jxrn8f6jp9lqkn = zlib.decompress(base64.b64decode(sqc1v87ozwdz7navbnepl9['png_zlib_base64']))
        self.assertEqual(flfar523jxrn8f6jp9lqkn, tksq9i5llq95gmzlkjhudf)
        self.assertLess(sqc1v87ozwdz7navbnepl9['compressed_bytes'], sqc1v87ozwdz7navbnepl9['png_bytes'])

    def testypqunfs5yc2dg7ectd(self):
        with self.assertRaises(vmmaieuzwn7j9llhbznbgs.qxik4i1ab3x3aozq5e8hyt):
            vmmaieuzwn7j9llhbznbgs.d6c75kdary4s7xrjt1urts('screenshot', {'compress': 1})

    def testvq6nqisente10iaeuk(self):
        vmmaieuzwn7j9llhbznbgs.d6c75kdary4s7xrjt1urts('screenshot', {'compress': True, 'scale': 0.5})
if __name__ == '__main__':
    unittest.main(verbosity=2)
