def add_dispaly(message):
    print(f"Expense added successfully (ID:{message})")

def update_display(message):
    print(message)

def delete_display(message):
    print(message)

def display_list(rows):    
    print("\n"+"="*50)
    print(f"{'ID':<5} {'Date':<12} {'Description':<15} {'Amount':>10}")
    print("="*50)

    for row in rows:
        id, date, description, amount = row
        print(f"{id:<5} {date:<12} {description:<15} ${amount:>9.2f}")

def display_summary(total):
    print(f"Total expenses : ${total}")

def display_summary_month(message):
    print(message)
