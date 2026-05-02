from dataclasses import dataclass
from typing import List, Tuple
from database import DatabaseProvider

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

class StoreModel:
    """Handles CRUD and Transactions. Dependency Injection used here."""
    def __init__(self, db_provider: DatabaseProvider):
        self._db_provider = db_provider

    def get_all_products(self) -> List[Product]:
        conn = self._db_provider.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return [Product(**row) for row in rows]

    def add_product(self, name: str, price: float, stock: int):
        conn = self._db_provider.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
        conn.commit()
        conn.close()

    def process_transaction(self, customer_id: int, product_id: int, qty: int) -> str:
        """Fulfills the 'Transaction Processing' requirement."""
        conn = self._db_provider.get_connection()
        cursor = conn.cursor()
        
        try:
            conn.start_transaction()
            
            # Fetch product price and check stock
            cursor.execute("SELECT price, stock FROM products WHERE id = %s FOR UPDATE", (product_id,))
            result = cursor.fetchone()
            
            if not result:
                raise ValueError("Product not found.")
            
            price, current_stock = result[0], result[1]
            
            if current_stock < qty:
                raise ValueError("Insufficient stock!")

            # Deduct stock
            cursor.execute("UPDATE products SET stock = stock - %s WHERE id = %s", (qty, product_id))
            
            # Record transaction
            total_price = float(price) * qty
            cursor.execute(
                "INSERT INTO transactions (customer_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)",
                (customer_id, product_id, qty, total_price)
            )

            conn.commit()
            return f"Success! Total: ${total_price:.2f}"

        except Exception as e:
            conn.rollback() # Crucial for atomicity
            raise e
        finally:
            conn.close()