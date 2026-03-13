
from controllers.controllers import GithubActivityController

def main():
    #GitHub Activity CLI — v1.0.0

    is_on = True
    is_off = False
    username = 'hamoudabass'

    while is_on:
        print("=" * 25, 'GitHub User Activity', "=" * 25)
        print("1. Fetch user activity")
        print("2. Show event details")
        print("3. Change GitHub user")
        print("4. Exit")

        choice = input("\nSelect an option : ")
        print("="*50)
        if choice == "1":

            result = GithubActivityController.get_github_activity(username)
            oldest_event = result[-1]['created_at']
            print(f"Username : {username}")
            print(f"Events   : {len(result)}")
            print(f"Since    : {oldest_event[0:10]}")
            print(f"Types    :")

            GithubActivityController.get_events_types(result)

            input("\nPress Enter to continue...")

        elif choice == "2":
            type_event = input("\nEnter event type: ")
            result = GithubActivityController.get_github_activity(username)
            GithubActivityController.get_events_detail(result, type_event)

            input("\nPress Enter to continue...")

        elif choice =="3":
            username = input("\nEnter new GitHub username : ")
            print(f"\n✓ User changed to {username}")

        elif choice == "4":
            print("\nThank you for using GitHub Activity CLI. Goodbye! 👋")
            is_on = False

        else:
            print("\n✗ Invalid option, please try again.")


if __name__ == '__main__':
    main()
