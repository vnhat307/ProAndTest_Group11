from dataclasses import dataclass
from .user import User

@dataclass
class Admin(User):
     # ManageUser(): Add, edit, delete, lock/unlock → stub actions
    def manage_User(self, action: str, user: User) -> None:
        if action == "lock":
            user.Status = False
        elif action == "unlock":
            user.Status = True
        if action == "edit": 
            user.UserName = kwargs.get("UserName", user.UserName) # kwargs: keyword arguments
            user.Email = kwargs.get("Email", user.Email)
        if action == "add":
            pass  # Logic to add user would go here
        if action == "delete":
            pass  # Logic to delete user would go here
    # ManageExam(): approve, delete, or pause exams
    def manage_Exam(self, exam: "Exam", action: str) -> None:
        if action == "approve":
            exam.Status = "Approved"
        elif action == "delete":
            pass  # Logic to delete exam would go here
        elif action == "pause":
            exam.Status = "Paused"
    # DeleteOldResults(): delete old results data
    def delete_OldResults(self, results: list, threshold_date) -> list:
        return [result for result in results if result.date >= threshold_date]
    # ResetUserPassword(): reset a user's password
    def reset_UserPassword(self, user: User, new_PassWord: str) -> None:
        user.reset_PassWord(new_PassWord)