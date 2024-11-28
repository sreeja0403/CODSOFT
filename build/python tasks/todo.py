# todo.py
from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            manager.add_task(title, description)

        elif choice == '2':
            manager.view_tasks()

        elif choice == '3':
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            manager.update_task(index, title if title else None, description if description else None)

        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)

        elif choice == '5':
            index = int(input("Enter task number to mark as completed: ")) - 1
            manager.mark_task_completed(index)

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
