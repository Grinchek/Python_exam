import todo_class
from datetime import datetime
import os

todo = todo_class.ToDoList()

filename = "tasks.csv"


def menu():
    ex = False
    while ex != True:
        os.system('cls')
        menu_nav = input(
            "Welcome!\n1.Create task\n2.Show tasks\n3.Delete task\n4.Edit task\n0.Exit\n: ")
        if menu_nav == "1":
            os.system('cls')
            todo.tasks.clear()
            task_name = input("Enter name of task: ")
            description = input("Enter description of task: ")
            while True:
                priority = input(
                    "Enter priority of task\n1-high;\n2-medium;\n3-low\n: ")
                if priority == '1':
                    break
                elif priority == '2':
                    break
                elif priority == '3':
                    break
                else:
                    print("Priority might be in range between 1 and 3 only.")
            print("Enter date of task:")
            day = int(input("Enter day:"))
            month = int(input("Enter month:"))
            year = int(input("Enter year:"))
            print("Enter time of task:")
            hour = int(input("Enter hour:"))
            min = int(input("Enter minutes:"))
            try:
                todo.add_task(task_name, description, priority,
                              datetime(year, month, day, hour, min))
            except (ValueError):
                print("You entered incorrect date or time.")
                os.system('pause')
            todo.save_to_csv(filename)
        elif menu_nav == "2":
            os.system('cls')
            todo.load_from_csv(filename)
            while True:
                choice = input(
                    "Select the period for which you want to see the tasks:\n1-Month\n2-Week\n3-Day\n4-All\n:")
                if choice == "1":
                    todo.show_tasks("month")
                    break
                elif choice == "2":
                    todo.show_tasks("week")
                    break
                elif choice == "3":
                    todo.show_tasks("day")
                    break
                elif choice == "4":
                    while True:
                        field = input(
                            "By which parameter you want to sort tasks?\n1-Name\n2-Priority\n: ")
                        if field == '1':
                            todo.sort_by_name()
                            break
                        elif field == '2':
                            todo.sort_by_priority()
                            break
                        else:
                            print("Wrong choice.")
                    todo.show_tasks("all")
                    break
                else:
                    print("Wrong choice")

            os.system("pause")
        elif menu_nav == "3":
            os.system('cls')
            todo.load_from_csv(filename)
            task_name_to_delete = input("Enter name of task to delete: ")
            todo.delete_task_by_name(task_name_to_delete)
            todo.clear_csv(filename)
            todo.save_to_csv(filename)

        elif menu_nav == "4":
            os.system('cls')
            todo.load_from_csv(filename)
            index = todo.search_index()
            while True:
                field = input(
                    "Select the field you want to edit:\n1-Name\n2-Description\n3-Priority\n4-Date and time\n:")
                if field == "1":
                    field = 'name'
                    value = input("Enter new value\n: ")
                    todo.edit_task(index, field, value)
                    break
                elif field == '2':
                    field = 'description'
                    value = input("Enter new value\n: ")
                    todo.edit_task(index, field, value)
                    break
                elif field == '3':
                    field = 'priority'
                    value = input("Enter new value\n: ")
                    todo.edit_task(index, field, value)
                    break
                elif field == '4':
                    field = 'datetime'
                    print("Enter date of task:")
                    day = int(input("Enter day:"))
                    month = int(input("Enter month:"))
                    year = int(input("Enter year:"))
                    print("Enter time of task:")
                    hour = int(input("Enter hour:"))
                    min = int(input("Enter minutes:"))
                    try:
                        value = datetime(
                            year, month, day, hour, min)
                        todo.edit_task(index, field, value)
                    except (ValueError):
                        print("You entered incorrect date or time.")
                        os.system('pause')
                    break
                else:
                    print("Wrong choice.")
            # value = input("Enter new value\n: ")
            # todo.edit_task(index, field, value)
            todo.clear_csv(filename)
            todo.save_to_csv(filename)
        elif menu_nav == "0":
            ex = True
        else:
            print("You make wrong choice, try again.")
