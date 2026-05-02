import mysql.connector
from mysql.connector import Error

def setup_database():
    try:
        # Connect to MySQL server (without specifying a database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Default password sang mysql
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print("[Database]: Successfully connected to MySQL server.")
            
            # The exact SQL provided, formatted as a multi-statement string
            sql_schema = """
            CREATE DATABASE IF NOT EXISTS tech_store;
            USE tech_store;

            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                stock INT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                product_id INT,
                quantity INT,
                total_price DECIMAL(10, 2),
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
            );
            """
            
            print("[Databse]: Executing schema setup...")
            # Execute the schema setup using multi=True to handle multiple statements
            for _ in cursor.execute(sql_schema, multi=True):
                pass 
            print("[Database]: Database and tables created or verified successfully!")

            # Check if data already exists to prevent duplicates on multiple runs
            cursor.execute("SELECT COUNT(*) FROM products")
            if cursor.fetchone()[0] == 0:
                print("[Database]: Inserting dummy data...")
                dummy_data_sql = """
                INSERT INTO products (name, price, stock) VALUES ('Mechanical Keyboard', 50.00, 10), ('Wireless Mouse', 25.00, 20);
                INSERT INTO customers (name) VALUES ('Siana'), ('Ashlyn');
                """
                for _ in cursor.execute(dummy_data_sql, multi=True):
                    pass
                connection.commit()
                print("[Database]: Dummy data inserted!")
            else:
                print("[Database]: Dummy data already exists. Skipping insertion.")

            print("[Database]: Auto-setup complete! Your environment is ready.")

    except Error as e:
        print(f"[Database]: Error while connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("[Database]: MySQL connection closed.")

if __name__ == "__main__":
    setup_database()