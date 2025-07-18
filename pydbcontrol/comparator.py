"""
Comparator: Class that compares two tables with the same structure.
"""

# Currently it is not in use or under development, it is only in draft form.
from .db_connector import DBConnector

class Comparator:
    def __init__(self, db: DBConnector):
        """
        Initializes the Comparator with a DBConnector instance.
        Catches and prints user-friendly error messages if initialization fails.
        """
        try:
            self.db = db
        except Exception as e:
            print(f"Comparator init error: {e}")

    def compare_tables(self, table1: str, table2: str, key_column: str = 'id'):
        """
        Compares two tables by the key column and returns the differences.
        Catches and prints user-friendly error messages if SQL or comparison errors occur.
        """
        try:
            sql1 = f"SELECT * FROM {table1}"
            sql2 = f"SELECT * FROM {table2}"
            data1 = self.db.execute_query(sql1)
            data2 = self.db.execute_query(sql2)
            set1 = {row[key_column]: row for row in data1}
            set2 = {row[key_column]: row for row in data2}
            diff = {
                'only_in_table1': [v for k, v in set1.items() if k not in set2],
                'only_in_table2': [v for k, v in set2.items() if k not in set1],
                'different_rows': [
                    {'id': k, 'table1': set1[k], 'table2': set2[k]}
                    for k in set1.keys() & set2.keys() if set1[k] != set2[k]
                ]
            }
            return diff
        except Exception as e:
            print(f"Comparator error while comparing tables '{table1}' and '{table2}': {e}")
            return None
