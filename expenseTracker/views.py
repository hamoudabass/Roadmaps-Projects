import sqlite3

def display():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\n"+"="*50)
    print(f"{'ID':<5} {'Date':<12} {'Description':<15} {'Amount':>10}")
    print("="*50)

    for row in rows:
        id, date, description, amount = row
        print(f"{id:<5} {date:<12} {description:<15} ${amount:>9.2f}")

    conn.commit()
    conn.close()