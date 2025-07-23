"""
Comparator: Class that compares two tables with the same structure.
"""

# Currently it is not in use or under development, it is only in draft form.
from .db_connector import DBConnector

class Comparator:
    def __init__(self, db: DBConnector, logger=None):
        """
        Initializes the Comparator with a DBConnector instance and optional Logger.
        Catches and prints user-friendly error messages if initialization fails.
        """
        try:
            self.db = db
            self.logger = logger
        except Exception as e:
            print(f"Comparator init error: {e}")
            if logger:
                logger.log_action('INIT ERROR', f'Comparator init error: {e}')

    def compare_tables(self, *tables, key_column: str = 'id'):
        """
        Compares 2 or more tables by the key column and returns the differences for all.
        Returns a dict with keys:
            - only_in_<table>: rows only in that table
            - different_rows: list of dicts with key and values from all tables where rows differ
        """
        if len(tables) < 2:
            raise ValueError("At least two table names must be provided.")
        try:
            if self.logger:
                self.logger.log_action('COMPARE TABLES', f'Started comparing tables {tables} by key {key_column}')
            # Read all tables and convert to dict by key_column
            table_data = {}
            columns_set = set()
            columns_list = []
            for t in tables:
                sql = f"SELECT * FROM {t}"
                data = self.db.execute_query(sql)
                table_data[t] = {row[key_column]: row for row in data}
                if data:
                    cols = set(data[0].keys())
                    columns_set.update(cols)
                    columns_list.append((t, cols))
            # Check for column mismatches
            mismatch = False
            if columns_list:
                ref_cols = columns_list[0][1]
                for t, cols in columns_list[1:]:
                    if cols != ref_cols:
                        mismatch = True
                        warn_msg = f"WARNING: Column mismatch between tables: {columns_list[0][0]} and {t}. Columns: {sorted(ref_cols)} vs {sorted(cols)}"
                        print(warn_msg)
                        if self.logger:
                            self.logger.log_action('COLUMN MISMATCH WARNING', warn_msg)
            # Continue even if mismatch, but warn

            # Union of all keys
            all_keys = set()
            for d in table_data.values():
                all_keys.update(d.keys())

            # Only in one table
            only_in = {}
            for t in tables:
                others = set().union(*(table_data[ot].keys() for ot in tables if ot != t))
                only_in[t] = [v for k, v in table_data[t].items() if k not in others]

            # Rows that are different (present in at least 2 tables, but values differ)
            different_rows = []
            for k in all_keys:
                present = [t for t in tables if k in table_data[t]]
                if len(present) >= 2:
                    values = [table_data[t][k] for t in tables if k in table_data[t]]
                    if not all(v == values[0] for v in values):
                        row_diff = {'key': k}
                        for t in tables:
                            row_diff[t] = table_data[t].get(k)
                        different_rows.append(row_diff)

            result = {f'only_in_{t}': only_in[t] for t in tables}
            result['different_rows'] = different_rows
            if self.logger:
                self.logger.log_action('COMPARE TABLES', f'Compared tables {tables} by key {key_column}')
            return result
        except Exception as e:
            print(f"Comparator error while comparing tables {tables}: {e}")
            if self.logger:
                self.logger.log_action('COMPARE TABLES ERROR', f'Error comparing tables {tables}: {e}')
            return None
