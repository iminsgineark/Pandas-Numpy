import tkinter as tk
import json

class QuizApp:
    def __init__(self, quiz_file):
        self.quiz_file = quiz_file
        self.current_question = 0
        self.score = 0
        self.questions = []
        self.load_questions()
        self.setup_gui()

    def load_questions(self):
        with open(self.quiz_file, 'r') as f:
            self.questions = json.load(f)

    def setup_gui(self):
        self.window = tk.Tk()
        self.window.title("Python Quiz App")

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(self.window, textvariable=self.answer_var)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(self.window, text="")
        self.score_label.pack()

        self.show_question()

        self.window.mainloop()

    def show_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.configure(text=question['question'])
        else:
            self.question_label.configure(text="Quiz complete!")
            self.answer_entry.destroy()
            self.submit_button.destroy()
            self.show_score()

    def submit_answer(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            answer = self.answer_var.get()
            if answer.lower() == question['answer'].lower():
                self.score += 1
            self.current_question += 1
            self.show_question()

    def show_score(self):
        self.score_label.configure(text="Your score: {}/{}".format(self.score, len(self.questions)))

quiz = QuizApp("quiz.json")
