import sqlite3

from db_models import add, delete, list, summary, summary_month, update
from views import (
    add_dispaly,
    delete_display,
    display_list,
    display_summary,
    display_summary_month,
    update_display,
)


def add_expense(description: str, amount: int, date: str):
    try:
        result = add(description, amount, date)
        add_dispaly(result)

    except sqlite3.Error as e:
        print(e)


def update_expense(id_expense: int, description: str, amount: int):
    try:
        result = update(id_expense, description, amount)
        update_display(result)

    except sqlite3.Error as e:
        print(e)


def delete_expense(id_expense):
    try:
        result = delete(id_expense)
        delete_display(result)

    except sqlite3.Error as e:
        print(e)


def view_list():
    try:
        result = list()
        display_list(result)

    except sqlite3.Error as e:
        print(e)


def view_summary():
    try:
        result = summary()
        display_summary(result)

    except sqlite3.Error as e:
        print(e)


def view_summary_month(id_month: int):
    try:
        message = summary_month(id_month)
        display_summary_month(message)
    except sqlite3.Error as e:
        print(e)
