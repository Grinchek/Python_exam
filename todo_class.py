import csv
from datetime import datetime, timedelta

# filename = "tasks.csv"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, priority, datetime):
        task = {
            'name': name,
            'description': description,
            'priority': priority,
            'datetime': datetime
        }
        self.tasks.append(task)

    def show_tasks(self, timeframe):
        now = datetime.now()
        if timeframe == 'month':
            filtered_tasks = [
                task for task in self.tasks if task['datetime'].month == now.month]
            if len(filtered_tasks) > 0:
                for row in filtered_tasks:
                    for i in row:
                        print(f"[{row[i]}];", end="")
                    print("")
            else:
                print("The list is empty")
        elif timeframe == 'week':
            week_start = now - timedelta(days=now.weekday())
            week_end = week_start + timedelta(days=6)
            filtered_tasks = [
                task for task in self.tasks if week_start <= task['datetime'] <= week_end]
            if len(filtered_tasks) > 0:
                for row in filtered_tasks:
                    for i in row:
                        print(f"[{row[i]}];", end="")
                    print("")
            else:
                print("The list is empty")
        elif timeframe == 'day':
            filtered_tasks = [task for task in self.tasks if task['datetime'].date() == now.date()]
            if len(filtered_tasks) > 0:
                for row in filtered_tasks:
                    for i in row:
                        print(f"[{row[i]}];", end="")
                    print("")
            else:
                print("The list is empty")
        elif timeframe == 'all':
            if len(self.tasks) > 0:
                for row in self.tasks:
                    for i in row:
                        print(f"[{row[i]}];", end="")
                    print("")
            else:
                print("The list is empty")

    def search_tasks(self, search_string):
        return [task for task in self.tasks if
                search_string in task['name'] or
                search_string in task['priority']]

    def search_index(self):
        search_task = input("Enter name wanted task:\n")
        a = 0
        for task in self.tasks:
            if search_task in task['name']:
                return a
            elif search_task not in task['name']:
                a += 1

    def edit_task(self, index, field, value):
        if 0 <= index < len(self.tasks):
            self.tasks[index][field] = value

    def delete_task_by_name(self, name):
        tasks_to_remove = [task for task in self.tasks if task['name'] == name]
        for task in tasks_to_remove:
            self.tasks.remove(task)

    def save_to_csv(self, filename):
        with open(filename, '+a', newline='') as csvfile:
            fieldnames = ['name', 'description', 'priority', 'datetime']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for task in self.tasks:
                writer.writerow(task)

    def load_from_csv(self, filename):

        self.tasks = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row['datetime'] = datetime.strptime(
                        row['datetime'], '%Y-%m-%d %H:%M:%S')
                    self.tasks.append(row)
        except (FileNotFoundError):
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['name', 'description', 'priority', 'datetime']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    def clear_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'description', 'priority', 'datetime']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def sort_by_datetime(self):
        self.tasks.sort(key=lambda task: task['datetime'])

    def sort_by_priority(self):
        self.tasks.sort(key=lambda task: task['priority'])
