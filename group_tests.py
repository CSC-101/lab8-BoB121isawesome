import group, unittest

class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        self.assertEqual([[1, 2, 3], [5, 2, 1], [3, 1, 5], [5, 2, 3], [2, 3]],
                         group.groups_of_3(([1, 2, 3, 5, 2, 1, 3, 1, 5, 5, 2, 3, 2, 3])))

    def test_groups_of_3_2(self):
        self.assertEqual([[1, 3, 4], [2, 2, 3], [5, 2, 62], [5, 522, 3], [12, 3]],
                         group.groups_of_3(([1, 3, 4, 2, 2, 3, 5, 2, 62, 5, 522, 3, 12, 3])))

if __name__ == '__main__':
    unittest.main()