from data import QuestionFetcher
from quiz_brain import QuizBrain
from ui import QuizUi


def main():
    question_fetcher = QuestionFetcher()
    quiz = QuizBrain(question_fetcher)
    quiz_ui = QuizUi(quiz)


if __name__ == "__main__":
    main()
