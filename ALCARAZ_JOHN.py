task_list =[]

user_acc = {}

def register():
    print("Register")
    while True:
        try:
            username = input("Enter a new username: ")
            password = input("Enter a password (at least 8 characters): ")
            if not username:
                main()
            if username in user_acc:
                print("Username already exist!")
                continue
            while True:
                try:
                    if len(password) < 8:
                        print("Password must contain 8 characters")
                        return
                    if len(password) >= 8:
                        user_acc[username] = {"password": password}
                        print("Registered Successfully!")
                        main()
                    else:
                        print("Invalid username or password")
                        continue
                except ValueError as e:
                    print(e)
                    register()
        except ValueError as e:
            print(e)
            register()

def log_in():
    print("Log-In")
    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password (at least 8 characters): ")
            if not username:
                main()
            if user_acc.get(username) and user_acc[username]['password'] == password:
                print("Log-In Successfully!")
                to_do(username)
            else:
                print("Invalid Inputs. Account doesn't exist!")
        except ValueError as e:
            print(e)
            main()

def add_task(username):
    task = input("Enter your task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    task_list.append((task, False, due_date))
    print(f"Task {task} added to the list with the due date of {due_date}")
    to_do(username)

def view_task(username):
    if not task_list:
        print("There's no tasks found!")
    else:
        print("Current Tasks: ")
        for i, (task, completed, due_date) in enumerate(task_list):
            status = "Completed" if completed else "Pending"
            print(f"{i+1}. {task} - {status} - Due Date: {due_date}")        
    to_do(username)

def mark_as_done(username):
    print("MARK AS DONE")
    if not task_list:
        print("There's no tasks found!")
        return
    try:
        task_num = int(input("Enter the task number you want to mark as done: "))
        if task_num <= 0 or task_num > len(task_list):
            print("Invalid Tasks number!")
            return
        task_list[task_num -1 ] = (task_list[task_num -1][0], True, task_list[task_num -1][2])
        print("Task marked as done!")
    except ValueError:
        print("Invalid input! Pleas put another valid number.")
    to_do(username)

def delete_task(username):
    print("DELETE TASK")
    while True:
        try:
            if not task_list:
                print("There's no tasks found!")
                return
            
            task_num = int(input("Enter the task number you want to delete: "))
            if task_num <= 0 or task_num > len(task_list):
                print("Invalid task number!")
                return
            del task_list[task_num -1]
            print("Task deleted successfully!")
        except ValueError as e:
            print("Invalid input! Pleas put another valid number.")
        to_do(username)
    
def main():
    print("-------WELCOME TO YOUR DAILY TO-DO LIST--------")
    print("1. Register")
    print("2. Log-In")
    print("3. Exit")
    choice = int(input("Select your choice: "))

    while True:
        try:
            if choice == 1:
                register()
            if choice == 2:
                log_in()
            if choice == 3:
                print("Exitiingggg......")
                break
            else:
                print("Invalid Output!")
        except ValueError as e:
            print(e)

def to_do(username):
    while True:
        print("------To Do List Menu-------")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                add_task(username)
            elif choice == 2:
                view_task(username)
            elif choice == 3:
                mark_as_done(username)
            elif choice == 4:
                delete_task(username)
            elif choice == 5:
                main()
            elif choice >= 6:
                print("Invalid Input!")
                continue
            else:
                print("Input a number: ")
        except ValueError as e:
            print(e)        

main()