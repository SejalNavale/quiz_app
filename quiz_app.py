import json
import random

with open("questions.json","r") as file:
    questions=json.load(file)

score=0
print("Welcome to the Quiz App!")

random.shuffle(questions)

for index, q in enumerate(questions,start=1):
    print(f"\nQ{index}: {q['question']}")

    options = q["options"]
    random.shuffle(options)

    for i, option in enumerate(options,start=1):
        print(f"{i}.{option}")

    answer = int(input("Your answer(1-4): "))

    if options[answer - 1]== q["answer"]:
        print("Correct Answer!")
        score+=1
    else:
        print("Wrong Answer!")
        print("Correct answer:",q["answer"])

print("\nQuiz Finished!")
print(f"Your Score:{score}/{len(questions)}")