#!/bin/python
# python -m unittest tests.py

import unittest

from namifier import namifier


class TestNamifier(unittest.TestCase):
    def namify(self, name="") -> str:
        nf = namifier()
        n = nf.namify(name)
        name = " ".join([n.first, n.middle, n.last]).replace("  ", " ").strip()
        # print("Sending: **{0}**".format(name))
        return name

    def test_none(self):
        name = ""
        raw = self.namify(name)
        self.assertTrue(raw == "")

    def test_one(self):
        name = "first"
        raw = self.namify(name)
        self.assertTrue(raw == "First")

    def test_two(self):
        name = "first last"
        raw = self.namify(name)
        self.assertTrue(raw == "First Last")

    def test_three(self):
        name = "first middle last"
        raw = self.namify(name)
        self.assertTrue(raw == "First Middle Last")

    def test_four(self):
        name = "first middle other last"
        raw = self.namify(name)
        self.assertTrue(raw == "First Middle Other Last")


if __name__ == "__main__":
    unittest.main(verbosity=0)
