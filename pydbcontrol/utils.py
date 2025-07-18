"""
Utils: Helper functions and schema validation operations.
Stores initial table schemas and validates current schema against the original.
"""

import psycopg2
import json
import os

class Utils:

    # Store schemas.json in a 'schemas' directory at the same level as pydbcontrol
    _schemas_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'schemas'))
    if not os.path.exists(_schemas_dir):
        try:
            os.makedirs(_schemas_dir)
        except Exception as e:
            print(f"Utils warning: Could not create schemas directory: {e}")
    _schema_file = os.path.join(_schemas_dir, 'schemas.json')
    _initial_schemas = {}

    # Load schemas from file if exists
    if os.path.exists(_schema_file):
        try:
            with open(_schema_file, 'r', encoding='utf-8') as f:
                _initial_schemas = {k: set(v) for k, v in json.load(f).items()}
        except Exception as e:
            print(f"Utils warning: Could not load schema file: {e}")

    @classmethod
    def store_initial_schema(cls, db, table_name: str):
        """
        Fetches and stores the initial column list for a table from the database (all lowercase).
        Persists the schema to a JSON file for use across script runs.
        """
        try:
            sql = f"SELECT column_name FROM information_schema.columns WHERE table_name = %s ORDER BY ordinal_position"
            columns = [row['column_name'].lower() for row in db.execute_query(sql, [table_name])]
            cls._initial_schemas[table_name] = set(columns)
            # Save to file
            try:
                with open(cls._schema_file, 'w', encoding='utf-8') as f:
                    json.dump({k: list(v) for k, v in cls._initial_schemas.items()}, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Utils warning: Could not save schema file: {e}")
            # For debugging purposes, you can uncomment the next line
            #print(f"Initial schema stored for table '{table_name}': {columns}")
        except Exception as e:
            print(f"Utils error while storing initial schema for '{table_name}': {e}")

    @classmethod
    def validate_schema(cls, db, table_name: str) -> bool:
        """
        Fetches current columns from the database and compares to the initially stored schema (all lowercase).
        Prints warnings if columns are missing or extra.
        Returns True if schemas match, False otherwise.
        """
        try:
            if table_name not in cls._initial_schemas:
                print(f"No initial schema stored for table '{table_name}'. Please store it first.")
                return False
            # Fetch current columns from DB
            sql = f"SELECT column_name FROM information_schema.columns WHERE table_name = %s ORDER BY ordinal_position"
            current_columns = [row['column_name'].lower() for row in db.execute_query(sql, [table_name])]
            initial = cls._initial_schemas[table_name]
            current = set(current_columns)

            # For debugging purposes, you can uncomment the next line
            #print(f"Initial schema stored for table '{table_name}': {current_columns}")

            missing = initial - current
            extra = current - initial
            if not missing and not extra:
                print(f"Schema validation passed for table '{table_name}'.")
                return True
            if missing:
                print(f"Schema validation warning: Missing columns in '{table_name}': {sorted(missing)}")
            if extra:
                print(f"Schema validation warning: Extra columns in '{table_name}': {sorted(extra)}")
            return False
        except Exception as e:
            print(f"Utils error during schema validation: {e}")
            return False
