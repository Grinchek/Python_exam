import csv
import os
from datetime import datetime, timedelta

filename = "tasks.csv"


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
        elif timeframe == 'week':
            week_start = now - timedelta(days=now.weekday())
            week_end = week_start + timedelta(days=6)
            filtered_tasks = [
                task for task in self.tasks if week_start <= task['datetime'] <= week_end]
        elif timeframe == 'day':
            filtered_tasks = [
                task for task in self.tasks if task['datetime'].date() == now.date()]
        else:
            filtered_tasks = self.tasks
        for row in filtered_tasks:
            for i in row:
                print(f"[{row[i]}];", end="")
            print("")

    def search_tasks(self, search_string):
        return [task for task in self.tasks if
                search_string in task['name'] or
                search_string in task['priority']]

    def search_index(self, search_string):
        for task in todo.tasks:
            if search_string in task:
                for fields in task:
                    print(fields)

    def edit_task(self, index, field, value):
        if 0 <= index < len(self.tasks):
            self.tasks[index][field] = value

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

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


todo = ToDoList()


def menu():
    ex = False
    while ex != True:
        menu_nav = input(
            "Welcome!\n1.Create task\n2.Show tasks\n3.Edit task\n4.Delete task\n0.Exit\n: ")
        if menu_nav == "1":
            todo.tasks.clear()
            task_name = input("Enter name of task: ")
            description = input("Enter description of task: ")
            priority = input(
                "Enter priority of task\n1-high;\n2-medium;\n3-low\n: ")
            print("Enter date of task:")
            day = int(input("Enter day:"))
            month = int(input("Enter month:"))
            year = int(input("Enter year:"))
            print("Enter time of task:")
            hour = int(input("Enter hour:"))
            min = int(input("Enter minutes:"))

            todo.add_task(task_name, description, priority,
                          datetime(year, month, day, hour, min))
            todo.save_to_csv(filename)
        elif menu_nav == "2":
            todo.load_from_csv(filename)
            while True:
                choise = input(
                    "Choose the period by wich wodl you like to show tasks:\n1-Month\n2-Week\n3-Day\n:")
                if choise == "1":
                    todo.show_tasks("month")
                    break
                elif choise == "2":
                    todo.show_tasks("week")
                    break
                elif choise == "3":
                    todo.show_tasks("day")
                    break
                else:
                    print("Wrong choise")

            os.system("pause")
        elif menu_nav == "3":
            search_task = input("Enter name or priority of wanted task:\n")
            todo.search_index(search_task)
        # elif menu_nav=="4":
        #     #anther action
        # elif menu_nav=="5":
        #     #anther action
        elif menu_nav == "0":
            # exit program
            ex = True
        else:
            print("You make wrong choise, try again.")
