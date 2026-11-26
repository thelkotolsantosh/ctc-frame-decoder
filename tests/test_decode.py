import unittest
from io import StringIO

from decode import decode


class FrameTests(unittest.TestCase):
    def test_repeat_after_blank(self):
        out = decode(StringIO("_,A\n0,1\n0,1\n1,0\n0,1"))
        self.assertEqual(out["tokens"], ["A", "A"])
        self.assertEqual([(s["start"], s["stop"]) for s in out["spans"]], [(0, 2), (3, 4)])

    def test_ties_and_custom_blank(self):
        self.assertEqual(decode(StringIO("X,void\n-1,-1"), "void")["tokens"], ["X"])

    def test_silence(self):
        self.assertEqual(decode(StringIO("_,a\n1,0"))["tokens"], [])

    def test_invalid(self):
        for data in ("A", "_,A,A", "_,A\n0", "_,A\n0,nan", "_,A\nx,2"):
            with self.subTest(data=data), self.assertRaises(ValueError):
                decode(StringIO(data))
