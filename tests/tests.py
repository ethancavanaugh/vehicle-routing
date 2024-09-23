import unittest
import dataloaders
from Package import Package
from RouteFinder import RouteFinder
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


class TestRouteFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.package_map = dataloaders.load_package_data("../WGUPS Package Table.csv")

        distance_table = dataloaders.load_distance_data("../WGUPS Distance Table.csv")
        addr_index_map = dataloaders.load_address_data("../WGUPS Address Table.csv")
        cls.route_finder = RouteFinder(distance_table, addr_index_map)

    def test_swap_edges(self):
        tour = ['A', 'B', 'E', 'D', 'C', 'F', 'G', 'H', 'A']
        tour = self.route_finder._RouteFinder__swap_edges(tour, 1, 4)
        self.assertEqual(tour, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'A'])

    def test_swap_difference(self):
        def length(tour):
            tour_len = 0
            for i in range(1, len(tour)):
                tour_len += self.route_finder._RouteFinder__distance_between(tour[i - 1], tour[i])
            return tour_len

        package_ids = [2, 7, 5, 9, 11, 32, 21]
        pkgs = [self.package_map[i] for i in package_ids]

        expected_diff = self.route_finder._RouteFinder__get_swap_difference(pkgs, 1, 5)

        start_length = length(pkgs)
        pkgs = self.route_finder._RouteFinder__swap_edges(pkgs, 1, 5)
        final_length = length(pkgs)
        actual_diff = final_length - start_length

        self.assertTrue(abs(expected_diff - actual_diff) < 0.001)

    # Ensure hub is at start and end, and all packages remain in the route
    def test_two_opt(self):
        hub = Package(-1, "4001 South 700 East", None, None, None, None, None, "HUB ADDRESS")
        package_ids = [2, 7, 5, 9, 11, 32, 21, 27, 39, 40, 1, 17, 22, 33, 23, 15, 29]
        pkgs = [hub] + [self.package_map[i] for i in package_ids] + [hub]

        optimized_pkgs = self.route_finder.two_opt_tour(pkgs)

        self.assertEqual(optimized_pkgs[0], hub)
        self.assertEqual(optimized_pkgs[-1], hub)
        self.assertEqual(sorted(pkgs, key=lambda p: p.pkg_id),
                         sorted(optimized_pkgs, key=lambda p: p.pkg_id))


if __name__ == '__main__':
    unittest.main()
