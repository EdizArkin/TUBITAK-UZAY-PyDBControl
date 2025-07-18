import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
schema_validation_example.py: Example script to demonstrate schema storage and validation for a table.
"""
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.utils import Utils

def main():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit2"

    # Validate schema (should print 'passed' if unchanged, warnings if changed)
    Utils.validate_schema(db, table_name)

    db.disconnect()

if __name__ == "__main__":
    main()
