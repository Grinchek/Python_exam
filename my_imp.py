import os
import csv


def my_menu():
    print("Welcome!!!")
    header = ['name', 'description', 'priority', 'data']
    filename="tasks.csv"

    with open('tasks.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
    ex = False
    while ex == False:
        try:
            choise = int(input("1.Add new task.\n2.Show existing tasks.\n3.Delete task.\n4.Search a task.\n5.Edit task.\n0.Exit "))
            os.system('cls')
            if choise == 1:
                t_name= ["","","",""]
                t_name[0]=input("Enter name: ")
                t_name[1]=input("Enter description: ")
                t_name[2]=input("Enter priority(high,medium,low): ")
                t_name[3]=input("Enter date: ")
                with open('tasks.csv', '+a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(t_name)
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
            
