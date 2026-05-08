import sqlite3


def create_db():

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
        ID      INTEGER PRIMARY KEY AUTOINCREMENT,
        Date    TEXT NOT NULL, 
        Description TEXT NOT NULL,
        Amount  REAL NOT NULL)
        """)

    conn.commit()
    conn.close()


def add(description: str, amount: int, date: str):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(Date, Description, Amount) VALUES (?,?,?)",
        (date, description, amount),
    )

    cursor.execute("SELECT MAX(id) FROM expenses")
    last_id = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return last_id


def update(id_expense: int, description: str, amount: int):

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE expenses SET Description = ?, Amount = ? WHERE ID = ?",
        (description, amount, id_expense),
    )

    if cursor.rowcount == 0:
        return "❌ No expenses found with this ID"

    conn.commit()
    conn.close()

    return "Expense updated successfully"


def delete(id_expenses: int) -> str:

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE ID= ?", (id_expenses,))
    conn.commit()
    conn.close()

    return "Expense deleted successfully"


def list():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return rows


def summary():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Amount FROM expenses")
    results = cursor.fetchall()  # liste de tuples
    total = 0

    for row in results:
        total += row[0]

    conn.close()

    return total


def summary_month(id_month: int):
    MONTHS = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    id_month_str = str(id_month).zfill(2)  # 1 → "01", 12 → "12"

    if id_month_str not in MONTHS:
        print("❌ Mois invalide, entrez un nombre entre 01 et 12")
        return 0

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT Amount FROM expenses WHERE Date LIKE ?", (f"2026-{id_month_str}-%",)
    )

    results = cursor.fetchall()
    total_month = 0

    for row in results:
        total_month += row[0]

    month = MONTHS.get(id_month_str)

    conn.close()

    return f"Total expenses for {month}: ${total_month}"
