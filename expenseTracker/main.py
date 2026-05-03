from argparse import ArgumentParser,Namespace
from db_models import create_db, add
from datetime import date
from views import display

def main():
    parser = ArgumentParser()
    subparses = parser.add_subparsers(dest='command')

    add_parser = subparses.add_parser("add", help="add a an expense")
    add_parser.add_argument("--description", type=str, required= True)
    add_parser.add_argument("--amount", type=float, required= True)

    subparses.add_parser("view", help="view all expenses")

    args: Namespace = parser.parse_args()

    if args.command == "add":
        create_db()
        add(args.description, args.amount, date.today().isoformat())

    elif args.command == 'view':
        display()


if __name__ == "__main__":
    main()
