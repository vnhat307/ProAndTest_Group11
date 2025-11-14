from dataclasses import dataclass

@dataclass
class Question:
    QuestionID: int
    Content: str
    OptionA: str
    OptionB: str
    OptionC: str
    OptionD: str
    CorrectAnswer: str # 'A', 'B', 'C', or 'D'
    DifficultyLevel: str
    Topic: str
    CreatedBy: int = 0  # teacher'
    # EditQuestion(), DeleteQuestion()
    def Edit_Question(self, kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        print(f"Question {self.QuestionID} Edit Successfully.")
    def Delete_Question(self) -> None: 
        print(f"Question {self.QuestionID} Deleted Successfully.") 