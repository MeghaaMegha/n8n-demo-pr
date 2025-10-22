# Model.py12

from datetime import datetime
from typing import List

class TeamMember:
    """Represents a member of a project team."""
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"TeamMember(name='{self.name}', role='{self.role}'"


class Task:
    """Represents a task within a project."""
    def __init__(self, title: str, assignee: TeamMember, due_date: str, status: str = "Pending"):
        self.title = title
        self.assignee = assignee
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = status

    def mark_complete(self):
        self.status = "Completed"

    def __repr__(self):
        return f"Task(title='{self.title}', assignee={self.assignee.name}, status='{self.status}')"


class Project:
    """Represents a full project with multiple tasks."""
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_pending_tasks(self):
        return [task for task in self.tasks if task.status != "Completed"]

    def __repr__(self):
        return f"Project(name='{self.name}', total_tasks={len(self.tasks)})"


if __name__ == "__main__":
    # Example usage
    megha = TeamMember("Megha", "Project Manager")
    jerry = TeamMember("Jerry", "Data Engineer")

    project = Project("AI Automation")

    task1 = Task("Set up Databricks pipeline", jerry, "2025-11-01")
    task2 = Task("Prepare project plan", megha, "2025-10-30")

    project.add_task(task1)
    project.add_task(task2)

    print(project)
    print("Pending tasks:", project.get_pending_tasks())

    # Mark task complete
    task2.mark_complete()
    print("After completion:", project.get_pending_tasks())
# This will generate the code review for the python
# This is for review purpose, only




