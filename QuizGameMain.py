from QuizBrainClass import QuizBrain
from DataClass import Data

if __name__ == "__main__":
    quiz_data = Data()
    quiz = QuizBrain(quiz_data)
    quiz.start_quiz()