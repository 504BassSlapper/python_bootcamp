from question_model import Question
from data import question_data
import random


def map_answer(integer_prompt) -> bool:
    if integer_prompt == 0:
        return True
    else:
        return False


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

processing_game = 0
score = 0
print("Welcome, anwer True or False")
random.shuffle(question_bank)
while processing_game < 10 and score < 5:
    for question in question_bank:
        if score == 5:
            print("You win")
            break
        elif processing_game >=10:
            print("You loose")
        print(question.question_text)
        prompted_answer = map_answer(int(input("0 for True, 1 for False \n")))
        if prompted_answer == eval(question.question_answer):
            score += 1
            print(f"correct, +1 your actual score is {score}")
        else:
            print("wrong answer , moove to next question ")

