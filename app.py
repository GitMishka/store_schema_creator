import sqlite3

def create_merch_schema():
    # Connect to database (will create merch_store.db if not exists)
    conn = sqlite3.connect('merch_store.db')
    cursor = conn.cursor()

    # Create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
    ''')

    # Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        address TEXT
    )
    ''')

    # Create orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER NOT NULL,
        order_date DATE NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    ''')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print("Merch Store Schema Created Successfully!")

if __name__ == "__main__":
    input("Press Enter to create the Merch Store Database Schema...")
    create_merch_schema()
