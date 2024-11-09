import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        for _ in range(100):
            random_operation = function_B()
            self.assertTrue(random_operation in "+ - *")
        
    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 6, '-', '5 - 6', -1),
                (4, 2, '*', '4 * 2', 8),
                (1, -1, '+', '1 + (-1)', 0),
                (0, 2, '*', '0 * 2', 0),
                
                
            ]

            for sample in test_cases:
                num1, num2, operator, expected_problem, expected_answer = sample
                PROBLEM, ANSWER = function_C(num1, num2, operator)
                print(f"\nQuestion: {expected_problem}")
                print(f"\nfunctions_answer: {ANSWER}, expected_answer = {expected_answer}")


if __name__ == "__main__":
    unittest.main()
