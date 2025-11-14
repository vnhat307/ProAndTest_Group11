# src/main.py
from datetime import date, datetime
from typing import List, Dict

from models.user import User
from models.admin import Admin
from models.teacher import Teacher
from models.student import Student
from models.question import Question
from models.questionbank import QuestionBank
from models.exam import Exam
from models.result import Result
from models.system import System

# ====== INITIAL DATA SEED ======
admin = Admin(1, "AdminUser", "admin@gmail.com", "123", "admin", True)
teacher = Teacher(2, "Ms. Tien", "teacher@gmail.com", "456", "teacher", True, "IT")
student = Student(3, "Nhat", "student@gmail.com", "789", "student", True, 3007, "SE1")
USERS: List[User] = [admin, teacher, student]

BANK = QuestionBank(1, teacher.UserID)
EXAMS: List[Exam] = []
RESULTS: List[Result] = []

SYS = System()


# ====== HELPER FUNCTIONS ======
def pause():
    input("\n(Press Enter to continue) ")


def next_user_id() -> int:
    return max((u.UserID for u in USERS), default=0) + 1


def find_user_by_email_role(email: str, role: str):
    return next((u for u in USERS if u.Email == email and u.Role == role), None)


def pick_user() -> User:
    print("\n=== SELECT USER TYPE ===")
    print("1) Admin")
    print("2) Teacher")
    print("3) Student")
    print("0) Exit")
    c = input("Choose: ").strip()
    if c == "1":
        return admin
    if c == "2":
        return teacher
    if c == "3":
        return student
    return None


# ====== ADMIN MENU ======
def admin_menu(a: Admin):
    while True:
        print("\n[ADMIN MENU]")
        print("1) List users")
        print("2) Reset user password")
        print("3) Lock/Unlock user")
        print("4) View result statistics")
        print("0) Back")
        c = input("Choose: ").strip()

        if c == "1":
            for u in USERS:
                print(
                    u.UserID,
                    u.UserName,
                    u.Email,
                    u.Role,
                    "Active" if u.Status else "Locked",
                )
            pause()

        elif c == "2":
            try:
                uid = int(input("Enter UserID to reset password: "))
                npw = input("New password: ")
                tgt = next((u for u in USERS if u.UserID == uid), None)
                if tgt:
                    a.reset_UserPassword(tgt, npw)
                else:
                    print("User not found.")
            except ValueError:
                print("Invalid UserID.")
            pause()

        elif c == "3":
            try:
                uid = int(input("Enter UserID to toggle lock/unlock: "))
                tgt = next((u for u in USERS if u.UserID == uid), None)
                if not tgt:
                    print("User not found.")
                else:
                    if tgt.Status:
                        a.manage_User("lock", tgt)
                    else:
                        a.manage_User("unlock", tgt)
            except ValueError:
                print("Invalid UserID.")
            pause()

        elif c == "4":
            if not RESULTS:
                print("No results available.")
            else:
                SYS.generate_Statistics(RESULTS)
            pause()

        elif c == "0":
            break
        else:
            print("Invalid choice.")


# ====== TEACHER MENU ======
def teacher_menu(t: Teacher):
    while True:
        print("\n[TEACHER MENU]")
        print("1) Add question to QuestionBank")
        print("2) View QuestionBank")
        print("3) Create exam (draft) from QuestionBank")
        print("4) Publish exam")
        print("5) List my exams")
        print("0) Back")
        c = input("Choose: ").strip()

        if c == "1":
            qid = (BANK.Questions[-1].QuestionID + 1) if BANK.Questions else 1
            content = input("Question content: ")
            A = input("A: ")
            B = input("B: ")
            C = input("C: ")
            D = input("D: ")
            ans = input("Correct answer (A/B/C/D): ").upper()
            q = Question(qid, content, A, B, C, D, ans, "easy", "general", t.UserID)
            BANK.add_Question(q)
            pause()

        elif c == "2":
            if not BANK.Questions:
                print("QuestionBank is empty.")
            else:
                for q in BANK.Questions:
                    print(f"Q{q.QuestionID}: {q.Content} (Ans {q.CorrectAnswer})")
            pause()

        elif c == "3":
            if not BANK.Questions:
                print("QuestionBank is empty, please add questions first.")
                pause()
                continue
            eid = (EXAMS[-1].ExamID + 1) if EXAMS else 1
            title = input("Exam title: ")
            e = Exam(eid, title, "", 10, date.today(), "draft", t.UserID)
            for q in BANK.Questions:
                e.add_QuestionToExam(q)
            EXAMS.append(e)
            print(f"Created draft exam ID={eid} with {len(e.Questions)} questions.")
            pause()

        elif c == "4":
            if not EXAMS:
                print("No exams available.")
                pause()
                continue
            try:
                eid = int(input("Enter ExamID to publish: "))
                e = next(
                    (x for x in EXAMS if x.ExamID == eid and x.TeacherID == t.UserID),
                    None,
                )
                if e:
                    e.publish_Exam()
                else:
                    print("Not found or not owned by you.")
            except ValueError:
                print("Invalid ExamID.")
            pause()

        elif c == "5":
            mine = [e for e in EXAMS if e.TeacherID == t.UserID]
            if not mine:
                print("You have no exams.")
            else:
                for e in mine:
                    print(
                        f"Exam {e.ExamID} | {e.Title} | {e.Status} | {len(e.Questions)} questions"
                    )
            pause()

        elif c == "0":
            break
        else:
            print("Invalid choice.")


# ====== STUDENT REGISTRATION / LOGIN ======
def student_entry() -> Student | None:
    while True:
        print("\n[STUDENT ENTRY]")
        print("1) log in")
        print("2) register")
        print("0) Back")
        c = input("Choose: ").strip()

        if c == "1":
            email = input("Email: ").strip()
            pw = input("Password: ").strip()
            s = find_user_by_email_role(email, "student")
            if not s or not s.login(email, pw):
                print("Invalid email/password or account locked.")
                continue
            return s

        elif c == "2":
            username = input("Full name: ").strip()
            email = input("Email: ").strip()

            if find_user_by_email_role(email, "student"):
                print("Email already exists. Please log in instead.")
                continue

            password = input("Password: ").strip()
            try:
                sid = int(input("Student ID: "))
            except ValueError:
                print("Invalid Student ID.")
                continue
            clazz = input("Class name: ").strip()

            new_id = next_user_id()
            s = Student(new_id, username, email, password, "student", True, sid, clazz)
            USERS.append(s)
            print(f"Registration successful! Your UserID is {new_id}.")
            return s

        elif c == "0":
            return None
        else:
            print("Invalid choice.")


# ====== STUDENT MENU ======
def student_menu(s: Student):
    if not s.StudentID:
        print("You must register before taking exams.")
        pause()
        return

    pubs = [e for e in EXAMS if e.Status == "published" and len(e.Questions) > 0]
    if not pubs:
        print("No published exams available.")
        pause()
        return

    print("\n[AVAILABLE EXAMS]")
    for e in pubs:
        print(f"{e.ExamID}) {e.Title} ({len(e.Questions)} questions)")

    try:
        eid = int(input("Enter ExamID to take: "))
    except ValueError:
        print("Invalid ExamID.")
        pause()
        return

    exam = next((x for x in pubs if x.ExamID == eid), None)
    if not exam:
        print("Exam not found.")
        pause()
        return

    already_done = any(
        r for r in RESULTS if r.StudentID == s.StudentID and r.ExamID == exam.ExamID
    )
    if already_done:
        print("You have already taken this exam.")
        pause()
        return

    print(f"\nSTART EXAM: {exam.Title}")
    answers: Dict[int, str] = {}
    for q in exam.Questions:
        while True:
            print(f"\nQ{q.QuestionID}: {q.Content}")
            print("A)", q.OptionA)
            print("B)", q.OptionB)
            print("C)", q.OptionC)
            print("D)", q.OptionD)
            ans = input("Your choice (A/B/C/D): ").strip().upper()
            if ans in {"A", "B", "C", "D"}:
                answers[q.QuestionID] = ans
                break
            print("Invalid choice. Please enter A, B, C, or D.")

    key = {q.QuestionID: q.CorrectAnswer for q in exam.Questions}
    correct, total = SYS.auto_Grading(key, answers)

    rid = (RESULTS[-1].ResultID + 1) if RESULTS else 1
    r = Result(rid, s.StudentID, exam.ExamID, 0, total, correct, datetime.now())
    r.calculate_Score()
    RESULTS.append(r)

    print(f"\nCompleted. Score: {r.Score}/10 | Correct {r.CorrectAnswers}/{r.TotalQuestions}")
    pause()


# ====== MAIN PROGRAM ======
def main():
    if not BANK.Questions:
        BANK.add_Question(
            Question(1, "4+2=?", "2", "6", "3", "5", "B", "easy", "Math", teacher.UserID)
        )
        BANK.add_Question(
            Question(
                2,
                "Which statement about Acceptance testing is correct?",
                "Performed by developers before release",
                "Conducted to decide if the customer accepts the product",
                "Always automated",
                "Only checks for performance issues",
                "B",
                "easy",
                "Software engineering",
                teacher.UserID,
            )
        )
        BANK.add_Question(
            Question(
                3,
                "Verification ensures that the system?",
                "Meets user needs",
                "Has no bugs",
                "Runs fast",
                "Is built correctly according to its specification",
                "D",
                "easy",
                "software engineering",
                teacher.UserID,
            )
        )

    while True:
        u = pick_user()
        if u is None:
            print("Goodbye!")
            break

        if u.Role == "student":
            s = student_entry()
            if s:
                student_menu(s)
            continue

        print(f"\n== LOGIN ({u.Role.upper()}) ==")
        email = input("Email: ").strip()
        pw = input("Password: ").strip()
        if not u.login(email, pw):
            print("Wrong email/password or account locked.")
            continue

        if u.Role == "admin":
            admin_menu(admin)
        elif u.Role == "teacher":
            teacher_menu(teacher)
        else:
            print("Invalid role.")


if __name__ == "__main__":
    main()
