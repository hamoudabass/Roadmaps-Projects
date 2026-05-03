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

def add(description:str, amount:int, date:str):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses(Date, Description, Amount) VALUES (?,?,?)",
                (date,description,amount))
    conn.commit()
    conn.close()

