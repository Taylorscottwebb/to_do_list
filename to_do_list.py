chores = []
completed = []
print("We got a lot to do today, we need to create a chores list")
def add_task(chores):
    task = input("What needs to be done? ").lower()
    if task not in chores:
        chores.append(task)
    else:
        print(f"{task} is already on the list!")

def remove_task(chores):
    task = input("What chore would you like to remove?").lower()
    try:
        chores.remove(task)
    except ValueError:
        print(f"{task} is not on the list of chores!")

def complete_chore(chores, completed):
    task = input("what chore did you complete?").lower()
    try:
        chores.remove(task)
        completed.append(task)
    except ValueError:
        print("That task is not on your list!")

def view_tasks(chores, completed):
    response = input("Would you like to check your chores left or completed? ").lower()
    if response == "chores left":
        print("This is what you have left!")
        for task in chores:
            print(task)
    elif response == "completed":
        print("This is what you've done so far!")
        for task in completed:
            print(task)
    else:
        print("please enter a valid list to view!")


def run(chores, completed):
    while True:
        response = input("What would you like to do? add/remove/complete/view/quit: ").lower()
        if response == "add":
            add_task(chores)
            print(chores)
        elif response == "remove":
            remove_task(chores)
            print(chores)
        elif response == "complete":
            complete_chore(chores, completed)
            print("Your completed chores")
            for task in completed:
                print(task)
        elif response == "view":
            view_tasks(chores, completed)
        
        elif response == "quit":
            for task in chores:
                print("these are the tasks you didn't finish:", task)
            for completed_chore in completed:
                print("You completed these chores:", completed_chore)
            break
        else:
            print("Please enter a valid response")
run(chores, completed)