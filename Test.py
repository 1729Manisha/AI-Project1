import unittest
from main import Water


class TestMethods(unittest.TestCase):

    def test_example1(self):
        problem = {
            "size": [1,4,10,15,22],
            "target": 181
        }
        water = Water()
        result = water.run(problem=problem)
        print(f"Min number of steps: {result}")
        print("\n")
        self.assertEqual(result, 19)

    def test_example2(self):
        problem = {
            "size": [2,5,6,72],
            "target": 143
        }
        water = Water()
        result = water.run(problem=problem)
        print(f"Min number of steps: {result}")
        print("\n")
        self.assertEqual(result, 7)


    def test_example3(self):
        problem = {
            "size": [3,6],
            "target": 2
        }
        water = Water()
        result = water.run(problem=problem)
        print(f"Min number of steps: {result}")
        print("\n")
        self.assertEqual(result, -1)

    def test_example4(self):
        problem = {
            "size": [2,3,5,19,121,852],
            "target": 11443
        }
        water = Water()
        result = water.run(problem=problem)
        print(f"Min number of steps: {result}")
        print("\n")
        self.assertEqual(result, 36)

    def test_example5(self):
        problem = {
            "size": [1,3,5],
            "target": 0
        }
        water = Water()
        result = water.run(problem=problem)
        print(f"Min number of steps: {result}")
        print("\n")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
