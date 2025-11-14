from dataclasses import dataclass
from .user import User

@dataclass
class Student(User):
    StudentID: int
    ClassName: str = ""

    # RegisterAccount()
    def register_Account(self, student_id: int, class_name: str) -> None:
        self.StudentID = student_id
        self.ClassName = class_name
    # viewAvailableExams(), takeQuiz(), submitExam(), viewResult(), viewExamHistory()
    def view_available_exams(self, exams: list["Exam"]): 
        available = [e for e in exams if e.status == "published"]
        print(f"Found {len(available)} available exams.")
        return available
    
    def take_Quiz(self, exam):
        print(f"{self.UserName} is taking exam '{exam.title}'.")

    def submit_Exam(self, exam):
        print(f"{self.UserName} submitted exam '{exam.title}'.")

    def view_Result(self, result):
        print(f"{self.UserName} scored {result.score}/10 in exam {result.exam_id}.")

    def view_ExamHistory(self, results):
        print(f"Exam history for {self.UserName}:")
        for r in results:
            if r.student_id == self.UserID:
                print(f"Exam {r.exam_id}: Score {r.score}")
    