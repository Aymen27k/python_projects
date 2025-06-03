from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = []
    for question in question_data:
        q = Question(question['question'], question['correct_answer'])
        question_bank.append(q)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    final_score = quiz.score
    print("You've completed the Quiz !")
    print(f"Your final score was: {final_score}/{len(question_bank)}")


if __name__ == "__main__":
    main()
