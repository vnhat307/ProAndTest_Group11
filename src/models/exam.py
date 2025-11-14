from dataclasses import dataclass, field
from typing import List
from datetime import date
from .question import Question

@dataclass
class Exam:
    ExamID: int
    Title: str
    Description: str
    Duration: int            # phút
    DateCreated: date
    Status: str              # 'draft' | 'published' | 'closed'
    TeacherID: int
    Questions: List[Question] = field(default_factory=list)

    # addQuestionToExam()
    def add_QuestionToExam(self, question: Question) -> None:
        self.Questions.append(question)
        print(f"Added Q{question.QuestionID} to exam {self.ExamID}.")

    # removeQuestionFromExam()
    def remove_QuestionFromExam(self, question_id: int) -> None:
        before = len(self.Questions)
        self.Questions = [q for q in self.Questions if q.QuestionID != question_id]
        after = len(self.Questions)
        if before == after:
            print(f"Question {question_id} not found in exam {self.ExamID}.")
        else:
            print(f"Removed Q{question_id} from exam {self.ExamID}.")

    # editExam()
    def edit_Exam(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        print(f"Exam {self.ExamID} edited.")

    # publishExam()
    def publish_Exam(self) -> None:
        self.Status = "published"
        print(f"Exam {self.ExamID} published.")

    # deleteExam()
    def delete_Exam(self) -> None:
        # tuỳ bạn chọn xoá mềm/hard; ở đây chỉ in trạng thái
        print(f"Exam {self.ExamID} deleted (logical).")
