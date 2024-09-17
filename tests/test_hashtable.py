import unittest
from OpenAddressHashTable import OpenAddressHashTable


class TestHashTable(unittest.TestCase):
    def setUp(self) -> None:
        self.tbl = OpenAddressHashTable()

    def test_add(self):
        self.tbl[1] = "One"
        self.tbl["Two"] = 2

        self.assertEqual(self.tbl[1], "One")
        self.assertEqual(self.tbl["Two"], 2)
        self.assertEqual(self.tbl.size, 2)

    def test_resize(self):
        for i in range(8):
            self.tbl[i] = str(i)

        self.assertEqual(len(self.tbl.table), 32)
        for i in range(8):
            self.assertEqual(self.tbl[i], str(i))

    def test_set(self):
        self.tbl[1] = "set"
        self.tbl[1] = "set again"

        self.assertEqual(self.tbl[1], "set again")
        self.assertEqual(self.tbl.size, 1)

    def test_contains(self):
        self.tbl[1] = "One"

        self.assertIn(1, self.tbl)
        self.assertNotIn(2, self.tbl)

    def test_del(self):
        self.tbl[1] = "One"
        del self.tbl[1]

        self.assertNotIn(1, self.tbl)
        self.assertEqual(self.tbl.size, 0)

    def test_exceptions(self):
        self.assertRaises(KeyError, lambda: self.tbl[1])


if __name__ == '__main__':
    unittest.main()