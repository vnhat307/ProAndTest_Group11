from dataclasses import dataclass
from .user import User

@dataclass

class Teacher(User):
    Department: str =""

# CreateQuestion(), EditQuestion(), DeleteQuestion(), ManageQuestionBank()
# CreateExam(), EditExam(), DeleteExam(), PublishExam(), ViewResults()

    def create_Question(self):
        print(f"{self.UserName} is creating a new question.")

    def edit_Question(self, question_id: int):
        print(f"{self.UserName} is editing question ID {question_id}.")

    def delete_Question(self, question_id: int):
        print(f"{self.UserName} is deleting question ID {question_id}.")

    def manage_QuestionBank(self):
        print(f"{self.UserName} is managing the question bank.")

    def create_Exam(self, exam_title: str):
        print(f"{self.UserName} is creating exam '{exam_title}'.")

    def edit_Exam(self, exam_id: int):
        print(f"{self.UserName} is editing exam ID {exam_id}.")

    def delete_Exam(self, exam_id: int):
        print(f"{self.UserName} is deleting exam ID {exam_id}.")

    def publish_Exam(self, exam_id: int):
        print(f"{self.UserName} is publishing exam ID {exam_id}.")
        
    def view_Results(self, exam_id: int):
        print(f"{self.UserName} is viewing results for exam ID {exam_id}.")