

import sqlite3
conn = sqlite3.connect("aquarium.db")


cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS aquarium (
    fish_name TEXT PRIMARY KEY,
    quantity INTEGER
)
""")

conn.commit()


def add_fish_to_db(fish_name):

    cursor.execute(
        "SELECT quantity FROM aquarium WHERE fish_name=?",
        (fish_name,)
    )

    result = cursor.fetchone()

   
    if result:

        quantity = result[0] + 1

        cursor.execute(
            "UPDATE aquarium SET quantity=? WHERE fish_name=?",
            (quantity, fish_name)
        )

    else:

        cursor.execute(
            "INSERT INTO aquarium VALUES (?, ?)",
            (fish_name, 1)
        )

    conn.commit()



def view_inventory():

    cursor.execute("SELECT * FROM aquarium")

    rows = cursor.fetchall()

    print("\n===== AQUARIUM INVENTORY =====")

    if not rows:
        print("No fish available.")

    else:
        for row in rows:
            print(f"{row[0]}: {row[1]}")