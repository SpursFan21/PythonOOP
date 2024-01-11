import random
from QuestionModelClass import QuestionModel

class QuizBrain:
    def __init__(self, data):
        self.question_number = 0
        self.score = 0
        self.question_list = [QuestionModel(question["text"], question["answer"]) for question in data.question_data]

    def next_question(self):
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
            self.check_answer(user_answer, current_question.answer)
        else:
            self.end_quiz()

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        self.next_question()

    def start_quiz(self):
        random.shuffle(self.question_list)
        self.next_question()

    def end_quiz(self):
        print("You've completed the quiz!")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")

