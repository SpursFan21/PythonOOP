# QuestionModelClass.py

class QuestionModel:
    def __init__(self, question_data):
        self.text = question_data["question"]
        self.answer = question_data["correct_answer"]
