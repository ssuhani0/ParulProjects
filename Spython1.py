import random

quiz_data = {
    "What is 5 + 3?": 8,
    "What is 10 - 4?": 6,
    "What is 7 x 2?": 14,
    "What is 16 / 4?": 4,
    "What is 9 + 6?": 15
}

questions = list(quiz_data.keys())
random.shuffle(questions)

score = 0

print("Welcome to the Math Quiz!\n")

for question in questions:
    user_answer = input(f"{question} Your answer: ")

    if user_answer.isdigit() and int(user_answer) == quiz_data[question]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The correct answer is {quiz_data[question]}.\n")

print(f"You scored {score}/{len(quiz_data)}. Thanks for playing!")