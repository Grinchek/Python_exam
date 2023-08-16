


def my_hello():
    ex = False
    while ex == False:
        try:
            choise = int(input("enter: "))
            if choise == 1:
                print(f"You choise is {choise}")
            elif choise == 2:
                print(f"You choise is {choise}")
        except ValueError:
            print("Error!")
            
