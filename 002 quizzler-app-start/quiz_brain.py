import html
from data import QuestionFetcher
from question_model import Question
from datetime import datetime
import json

TIMER = 15


class QuizBrain:

    def __init__(self, data: QuestionFetcher):
        self.question_number = 0
        self.data = data
        self.score = 0
        self.question_list = []
        self.current_question = None
        self.time_left = TIMER
        self.question_bank = []
        self.extract_questions()

    def extract_questions(self):
        self.question_list = self.data.fetch_questions()
        for question in self.question_list:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_bank.append(new_question)

    def decrement_time(self):
        self.time_left -= 1

    def reset_timer(self):
        self.time_left = TIMER

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        self.current_question = self.question_bank[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def reset_game(self):
        self.question_bank = []
        self.score = 0
        self.question_number = 0
        self.extract_questions()

    def saving_score(self, name):
        player_name = name.capitalize()
        new_entry = {
            "name": player_name,
            "score": self.score,
            "timestamp": datetime.now().isoformat()
        }
        file_path = "leaderboard.json"
        try:
            # Reading JSON data
            with open(file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(file_path, "w") as file:
                json.dump([new_entry], file, indent=4)
        else:
            try:
                # Updating old data with new data
                data.append(new_entry)
                # Saving updated Data
                with open(file_path, "w") as file:
                    json.dump(data, file, indent=4)
            except Exception as e:
                print(f"Something went wrong while saving the score: {e}")

    def get_sorted_scores(self):
        try:
            with open("leaderboard.json", "r") as file:
                scores = json.load(file)
            sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)
            return sorted_scores
        except (FileNotFoundError, json.JSONDecoder):
            return []

