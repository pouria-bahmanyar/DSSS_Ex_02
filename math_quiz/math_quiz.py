import random


def Random_Nmber(min, max):
    """
    choose random number.
    """
    return random.randint(min, max)


def Random_Operation():
    """
    This function chooses randomly between the three mathematical operations:        ############
    """
    return random.choice(['+', '-', '*'])

def Create_Q_and_A(first_number, second_number, operation):
    problem = f"{first_number} {operation} {second_number}"
    if operation == '+':                                                                  
        answer = first_number + second_number
    elif operation == '-': 
        answer = first_number - second_number
    else: 
        answer = first_number * second_number
    return problem, answer

def math_quiz():
    """
    the function provides a math question for the user                                 
    """
    total_points = 0
    total_questions = 5                               
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        first_random_number = Random_Nmber(1, 10) 
        second_random_number = Random_Nmber(1, 5) 
        random_operation = Random_Operation()

        PROBLEM, ANSWER = Create_Q_and_A(first_random_number, second_random_number, random_operation)
        print(f"\nQuestion: {PROBLEM}")
        while True:
            useranswer = input("Your answer: ")
            try:
                useranswer = int(useranswer)
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a number.")
          
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            total_points += (1)                                           
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {total_points}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
