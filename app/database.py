import sqlite3
import os

DB_PATH = "data/supply_chain.db"


def create_database():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        warehouse TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    cursor.execute("DELETE FROM inventory")

    rows = [
        ("Tyres", "Pune", 120),
        ("Steel", "Mumbai", 75),
        ("Rubber", "Chennai", 210),
        ("Rims", "Delhi", 50)
    ]

    cursor.executemany(
        """
        INSERT INTO inventory(
            product,
            warehouse,
            quantity
        )
        VALUES(?,?,?)
        """,
        rows
    )

    conn.commit()

    conn.close()

    print("Database Created Successfully")


if __name__ == "__main__":
    create_database()