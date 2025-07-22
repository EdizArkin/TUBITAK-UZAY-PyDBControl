"""
TableManager: Class for managing read, insert, update, and delete operations on a table.
"""
from db_connector import DBConnector


class TableManager:
    def __init__(self, db:seyda, table_name: telecommand_unit1):
        """
        Initialize with table name and DBConnector instance.
        """
        self.db = db
        self.table_name = table_name

    def table_creator(self, model_sql_path: str):
        """
        Reads CREATE TABLE statement from the specified .sql file in the model folder and executes it.
        """
        with open(model_sql_path, "r", encoding="utf-8") as f:
            sql = f.read()
        self.db.execute_query(sql, fetch=False)
        return f"Created succesfully: {self.table_name}"

    def get_data(self, filters=None, limit=10):
        """
        Fetches data from the table with optional filters.
        """
        sql = f"SELECT * FROM {self.table_name}"
        params = []
        if filters:
            where = " AND ".join([f"{k}=%s" for k in filters.keys()])
            sql += f" WHERE {where}"
            params = list(filters.values())
        sql += " LIMIT %s"
        params.append(limit)
        return self.db.execute_query(sql, params)

    def insert_row(self, data: dict):
        """
        Inserts a new row into the table.
        """
        fields = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({placeholders})"
        self.db.execute_query(sql, list(data.values()), fetch=False)

    def update_row(self, row_id: int, new_values: dict):
        """
        Updates the specified row in the table.
        """
        set_clause = ', '.join([f"{k}=%s" for k in new_values.keys()])
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE id=%s"
        params = list(new_values.values()) + [row_id]
        self.db.execute_query(sql, params, fetch=False)

    def delete_row(self, row_id: int):
        """
        Deletes the specified row from the table.
        """
        sql = f"DELETE FROM {self.table_name} WHERE id=%s"
        self.db.execute_query(sql, [row_id], fetch=False)