from QuizGame.QuizBrainClass import QuizBrain
from QuizGame.DataClass import Data

if __name__ == "__main__":
    quiz_data = Data()
    quiz = QuizBrain(quiz_data)
    quiz.start_quiz()