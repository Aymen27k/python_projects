class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):  # Add this method
        return f"Question: {self.text}, Answer: {self.answer}"