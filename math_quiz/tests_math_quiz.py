import unittest
from math_quiz import Random_Nmber, Random_Operation, Create_Q_and_A


class TestMathGame(unittest.TestCase):

    def test_Random_Nmber(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_Nmber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Random_Operation(self):
        for _ in range(100):
            random_operation = Random_Operation()
            self.assertTrue(random_operation in "+ - *")
        
    def test_Create_Q_and_A(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 6, '-', '5 - 6', -1),
                (4, 2, '*', '4 * 2', 8),
                (1, -1, '+', '1 + (-1)', 0),
                (0, 2, '*', '0 * 2', 0),
                
                
            ]

            for sample in test_cases:
                num1, num2, operator, expected_problem, expected_answer = sample
                PROBLEM, ANSWER = Create_Q_and_A(num1, num2, operator)
                print(f"\nQuestion: {expected_problem}")
                print(f"\nfunctions_answer: {ANSWER}, expected_answer = {expected_answer}")


if __name__ == "__main__":
    unittest.main()
