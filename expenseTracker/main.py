from argparse import ArgumentParser,Namespace
from db_models import create_db
from controllers import add_expense, delete_expense, view_list, view_summary, view_summary_month, update_expense
from datetime import date

def main():
    parser = ArgumentParser()
    subparses = parser.add_subparsers(dest='command')

    add_parser = subparses.add_parser("add", help="add an expense")
    add_parser.add_argument("--description", type=str, required= True)
    add_parser.add_argument("--amount", type=float, required= True)

    delete_parser = subparses.add_parser("delete", help="delete an expense")
    delete_parser.add_argument("--id", type=int, required= True)

    update_parser = subparses.add_parser("update", help="update an expense")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description", type=str, required=True)
    update_parser.add_argument("--amount", type=int, required=True)


    subparses.add_parser("list", help="view all expenses")

    summary_parser = subparses.add_parser("summary", help="view total expenses")
    summary_parser.add_argument("--month", type=int, required=False)

    args: Namespace = parser.parse_args()
    
    create_db()

    if args.command == "add":
        add_expense(args.description, args.amount, date.today().isoformat())

    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)


    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == 'list':
        view_list()

    elif args.command == 'summary':
        if args.month:
           view_summary_month()
        else:
            view_summary()


if __name__ == "__main__":
    main()
