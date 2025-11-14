from dataclasses import dataclass
from typing import List, Dict
from .result import Result

@dataclass
class System:
    # autoGrading()
    def auto_Grading(self, answer_key: Dict[int, str], student_answers: Dict[int, str]) -> tuple[int, int]:
        total = len(answer_key)
        correct = 0
        for qid, correct_ans in answer_key.items():
            if student_answers.get(qid, "").upper() == correct_ans.upper():
                correct += 1
        print(f"Auto grading complete: {correct}/{total} correct.")
        return correct, total

    # generateStatistics()
    def generate_Statistics(self, results: List[Result]) -> None:
        if not results:
            print("No results available for statistics.")
            return
        scores = [r.Score for r in results]
        avg = sum(scores) / len(scores)
        highest = max(scores)
        lowest = min(scores)
        print("=== STATISTICS ===")
        print(f"Total results: {len(results)}")
        print(f"Average score: {avg:.2f}")
        print(f"Highest score: {highest}")
        print(f"Lowest score: {lowest}")

    # backupDatabase()
    def backup_Database(self, results: List[Result]) -> None:
        print("Backing up database...")
        for r in results:
            print(f"Backup -> Result {r.ResultID}: Student {r.StudentID}, Score {r.Score}")
        print("Backup complete.")
