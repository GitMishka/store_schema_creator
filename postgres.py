import psycopg2

def create_merch_schema():

    conn = psycopg2.connect(
        dbname="mydbname",
        user="myuser",
        password="mypassword",
        host="mydatabase.postgres.database.azure.com", 
        port="5432",
        sslmode="require" 
    )
    
    cursor = conn.cursor()

    # Create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
    ''')

    # Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        address TEXT
    )
    ''')

    # Create orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        id SERIAL PRIMARY KEY,
        customer_id INTEGER REFERENCES customers(id),
        product_id INTEGER REFERENCES products(id),
        quantity INTEGER NOT NULL,
        order_date DATE NOT NULL
    )
    ''')

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Merch Store Schema Created Successfully!")

if __name__ == "__main__":
    input("Press Enter to create the Merch Store Database Schema...")
    create_merch_schema()
