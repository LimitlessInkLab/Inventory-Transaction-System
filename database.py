import mysql.connector
from mysql.connector import MySQLConnection

class DatabaseProvider:
    """Handles database connections."""
    def __init__(self, host: str, user: str, password: str, database: str):
        self._config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }

    def get_connection(self) -> MySQLConnection:
        """Returns a fresh database connection."""
        return mysql.connector.connect(**self._config)