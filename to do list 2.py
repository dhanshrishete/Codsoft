# Create an empty list to store the to-do items
todo_list = []

# Function to add an item to the to-do list
def add_item(item):
    todo_list.append(item)
    print(f"Added '{item}' to the to-do list.")

# Function to remove an item from the to-do list
def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
        print(f"Removed '{item}' from the to-do list.")
    else:
        print(f"'{item}' is not in the to-do list.")

# Function to display the to-do list
def display_list():
    print("To-Do List:")
    for item in todo_list:
        print(f"- {item}")

# Main program
while True:
    print("\n1. Add item to to-do list")
    print("2. Remove item from to-do list")
    print("3. Display to-do list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        display_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
