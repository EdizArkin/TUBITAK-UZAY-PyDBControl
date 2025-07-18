"""
TableManager: Class for managing read, insert, update, and delete operations on a table.
"""
from .db_connector import DBConnector

class TableManager:
    def __init__(self, db: DBConnector, table_name: str):
        """
        Initialize with table name and DBConnector instance.
        """
        self.db = db
        self.table_name = table_name

    def table_creator(self, model_sql_path: str):
        """
        Reads CREATE TABLE statement from the specified .sql file in the model folder and executes it.
        Catches and prints user-friendly error messages if the table already exists or other SQL errors occur.
        """
        try:
            with open(model_sql_path, "r", encoding="utf-8") as f:
                sql = f.read()
            self.db.execute_query(sql, fetch=False)
            return f"Created successfully: {self.table_name}"
        except Exception as e:
            if hasattr(e, 'pgcode') and e.pgcode == '42P07':  # DuplicateTable
                print(f"Error: Table '{self.table_name}' already exists.")
            else:
                print(f"SQL Error while creating table '{self.table_name}': {e}")
            return None

    def get_data(self, filters=None, limit=50):
        """
        Fetches data from the table with optional filters.
        Catches and prints user-friendly error messages if SQL errors occur.
        """
        try:
            sql = f"SELECT * FROM {self.table_name}"
            params = []
            if filters:
                where = " AND ".join([f"{k}=%s" for k in filters.keys()])
                sql += f" WHERE {where}"
                params = list(filters.values())
            sql += " LIMIT %s"
            params.append(limit)
            return self.db.execute_query(sql, params)
        except Exception as e:
            print(f"SQL Error while fetching data from '{self.table_name}': {e}")
            return None

    def insert_row(self, data: dict):
        """
        Inserts a new row into the table.
        If 'id' is not provided, assigns the next available id (max+1).
        Prints feedback: success with inserted data, or failure reason (e.g., duplicate id).
        Catches and prints user-friendly error messages if SQL errors occur.
        """
        try:
            row_id = data.get("id")
            if row_id is None:
                # Get max id from table
                max_id_sql = f"SELECT MAX(id) as max_id FROM {self.table_name}"
                result = self.db.execute_query(max_id_sql)
                max_id = result[0]["max_id"] if result and result[0]["max_id"] is not None else 0
                row_id = max_id + 1
                data["id"] = row_id
            else:
                check_sql = f"SELECT 1 FROM {self.table_name} WHERE id=%s"
                exists = self.db.execute_query(check_sql, [row_id])
                if exists:
                    print(f"Insert failed: Row with id {row_id} already exists in '{self.table_name}'.")
                    return
            fields = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({placeholders})"
            self.db.execute_query(sql, list(data.values()), fetch=False)
            print(f"Row inserted successfully into '{self.table_name}': {data}")
        except Exception as e:
            print(f"SQL Error while inserting row into '{self.table_name}': {e}")

    def update_row(self, row_id: int, new_values: dict):
        """
        Updates the specified row in the table.
        Does not allow updating the 'id' field (primary key).
        Prints feedback: success with row id and new values, or failure reason (e.g., row does not exist).
        Catches and prints user-friendly error messages if SQL errors occur.
        """
        try:
            # Prevent updating the primary key 'id'
            if 'id' in new_values:
                print("Update failed: Cannot update the primary key 'id'. It will be ignored.")
                new_values = {k: v for k, v in new_values.items() if k != 'id'}
                if not new_values:
                    print("No fields to update after removing 'id'.")
                    return
            # Check if row exists
            check_sql = f"SELECT 1 FROM {self.table_name} WHERE id=%s"
            exists = self.db.execute_query(check_sql, [row_id])
            if not exists:
                print(f"Update failed: Row with id {row_id} does not exist in '{self.table_name}'.")
                return
            set_clause = ', '.join([f"{k}=%s" for k in new_values.keys()])
            sql = f"UPDATE {self.table_name} SET {set_clause} WHERE id=%s"
            params = list(new_values.values()) + [row_id]
            self.db.execute_query(sql, params, fetch=False)
            print(f"Row with id {row_id} updated successfully in '{self.table_name}' with values: {new_values}")
        except Exception as e:
            print(f"SQL Error while updating row in '{self.table_name}': {e}")

    def delete_row(self, row_id: int):
        """
        Deletes the specified row from the table.
        Prints feedback: success with row id, or failure reason (e.g., row does not exist).
        Catches and prints user-friendly error messages if SQL errors occur.
        """
        try:
            # Check if row exists
            check_sql = f"SELECT 1 FROM {self.table_name} WHERE id=%s"
            exists = self.db.execute_query(check_sql, [row_id])
            if not exists:
                print(f"Delete failed: Row with id {row_id} does not exist in '{self.table_name}'.")
                return
            sql = f"DELETE FROM {self.table_name} WHERE id=%s"
            self.db.execute_query(sql, [row_id], fetch=False)
            print(f"Row with id {row_id} deleted successfully from '{self.table_name}'.")
        except Exception as e:
            print(f"SQL Error while deleting row from '{self.table_name}': {e}")
