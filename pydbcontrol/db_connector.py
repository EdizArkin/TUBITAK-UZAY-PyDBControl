"""
DBConnector: Class that manages PostgreSQL database connections and query execution.
"""
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

class DBConnector:
    def __init__(self, host=None, database=None, user=None, password=None, port=None):
        """
        The database retrieves connection parameters from the .env file or directly.
        The .env file must contain the following keys:
        DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT
        """
        load_dotenv()
        self.host = host or os.getenv("DB_HOST", "localhost")
        self.database = database or os.getenv("DB_NAME", "postgres")
        self.user = user or os.getenv("DB_USER", "postgres")
        self.password = password or os.getenv("DB_PASSWORD", "")
        self.port = int(port or os.getenv("DB_PORT", 5432))
        self.conn = None

    def connect(self):
        """        
        Connects to the database.
        """
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port
        )
        return self.conn

    def disconnect(self):
        """
        Disconnects from the database.
        """
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query, params=None, fetch=True):
        """
        Executes a SQL query on the connected database.
        """
        if not self.conn:
            self.connect()
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            else:
                self.conn.commit()
                return None
