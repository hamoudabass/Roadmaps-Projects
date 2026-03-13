from controllers.tasks_controllers import TaskController

def main():
    """Menu of Task Tracker CLI"""
    while True:
        print("\n" + "=" * 80)
        print("TASK TRACKER")
        print("=" * 80)
        print("1. Add a Task")
        print("2. Update a Task")
        print("3. Delete a Task")
        print("4. Mark a Task")
        print("5. List all Tasks")
        print("6. List all Tasks todo")
        print("7. List all Tasks in progress")
        print("8. List all Tasks done")
        print("9. Quit")
        print("=" * 80)

        choice = input("Choose an option(1-9): ").strip()

        if choice == "1":
            name_task = input("Name of task: ").strip()
            TaskController.add_task(name_task)

        elif choice == "2":
            try :
                id_task = input("Id of task: ").strip()
                name_task = input("Name of new task: ").strip()
                TaskController.update_task(id_task, name_task)
            except ValueError:
                print("✗ Enter a valid number !")

        elif choice == "3":
            try :
                id_task = input("Id of task: ").strip()
                TaskController.delete_task(id_task)
            except ValueError:
                print("✗ Enter a valid number !")

        elif choice == "4":
            try:
                id_task = input("Id of task: ").strip()
                new_status = input("New status: ").strip()
                TaskController.mark_task(id_task,new_status)
            except ValueError:
                print("✗ Enter a valid number !")

        elif choice == "5":
            TaskController.list_all_task()

        elif choice == "6":
            TaskController.list_all_task_todo()

        elif choice == "7":
            TaskController.list_all_task_in_progress()

        elif choice == "8":
            TaskController.list_all_task_done()

        elif choice == "9":
            print('\nAu revoir! 👋')
            break

        else:
            print("✗ Invalid Number, Please Retry")

if __name__ == '__main__':
    main()


