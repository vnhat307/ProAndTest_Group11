from dataclasses import dataclass, field
from typing import List
from .question import Question

@dataclass
class QuestionBank:
    BankID: int
    TeacherID: int
    Questions: List[Question] = field(default_factory=list)

    # AadQuestion()
    def add_Question(self, question: Question) -> None:
        self.Questions.append(question)
        print(f"Question {question.QuestionID} added to bank {self.BankID}.")

    # RemoveQuestion()
    def remove_Question(self, question_id: int) -> None:
        before = len(self.Questions)
        self.Questions = [q for q in self.Questions if q.QuestionID != question_id]
        after = len(self.Questions)
        if before == after:
            print(f"Question {question_id} not found in bank {self.BankID}.")
        else:
            print(f"Question {question_id} removed from bank {self.BankID}.")

    # SearchQuestion()
    def search_Question(self, keyword: str) -> List[Question]:
        result = [q for q in self.Questions if keyword.lower() in q.Content.lower()]
        print(f"Found {len(result)} question(s) in bank {self.BankID} containing '{keyword}'.")
        return result
