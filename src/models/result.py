from dataclasses import dataclass
from datetime import datetime

@dataclass
class Result:
    ResultID: int
    StudentID: int
    ExamID: int
    Score: float
    TotalQuestions: int
    CorrectAnswers: int
    SubmittedTime: datetime

    # CalculateScore()
    def calculate_Score(self) -> None:
        if self.TotalQuestions > 0:
            self.Score = round((self.CorrectAnswers / self.TotalQuestions) * 10, 2)
            print(f"Score calculated: {self.Score}/10")
        else:
            self.Score = 0
            print("No questions in exam — score set to 0.")

    # ViewResultDetails()
    def view_ResultDetails(self) -> None:
        print("=== RESULT DETAILS ===")
        print(f"Result ID: {self.ResultID}")
        print(f"Student ID: {self.StudentID}")
        print(f"Exam ID: {self.ExamID}")
        print(f"Score: {self.Score}/10")
        print(f"Correct Answers: {self.CorrectAnswers}/{self.TotalQuestions}")
        print(f"Submitted Time: {self.SubmittedTime}")

    # DeleteResult()
    def delete_Result(self) -> None:
        print(f"Result {self.ResultID} deleted (logical).")
