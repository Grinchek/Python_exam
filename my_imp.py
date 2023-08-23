import os
import csv

def header():
    print("Welcome!!!")
    header = ['name', 'description', 'priority', 'data']
    filename="tasks.csv"
    with open('tasks.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
def add_task():
    task= ["","","",""]
    task[0]=input("Enter name: ")
    task[1]=input("Enter description: ")
    task[2]=input("Enter priority(high,medium,low): ")
    task[3]=input("Enter date: ")
    return task
def write_to_file(obj):
    with open('tasks.csv', '+a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(obj)
def rewrite(edited_file):
    with open('tasks.csv', '+a',newline='') as edited_file:
        writer = csv.writer(edited_file)
        writer.writerow(edited_file)
def read_from_file():
    with open('tasks.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            if i[0]=="2":
                i.clear()
        write_to_file(reader)
        for i in reader:
            print(i)

  
def my_menu():
    ex = False
    while ex == False:
        try:
            choise = int(input("1.Add new task.\n2.Show existing tasks.\n3.Delete task.\n4.Search a task.\n5.Edit task.\n0.Exit "))
            os.system('cls')
            if choise == 1:
                write_to_file(add_task())
                
                os.system('cls')
            elif choise == 2:
                next_choise=int(input("1.Show all tasks.\n2.Show tsks by month.\n3.Show task by week.\n4.Show task by day.\n0.Back to menu."))
                os.system('cls')
            elif choise==3:
                next_choise=int(input("Choise by what parameter whold you like to delete the task:\n1.By the name.\n2.By the priority.\n3.By the date.\n0.Back."))
                os.system('cls')
            elif choise==4:
                next_choise=int(input("Search a task by:\n1.Name.\n2.Priority.\n3.Date.\n0.Back."))
                os.system('cls')
            elif choise==5:
                next_choise=int(input("Enter the task, which whold you like to edit: "))
                os.system('cls')
            elif choise==0:
                ex=True
        except ValueError:
            print("Error!")
            
