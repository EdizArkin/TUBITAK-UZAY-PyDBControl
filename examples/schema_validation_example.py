import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
schema_validation_example.py: Example script to demonstrate schema storage and validation for a table.
"""
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.utils import Utils
from pydbcontrol.logger import Logger

def main():
    logger = Logger('pydbcontrol.log')
    db = DBConnector(logger=logger)
    db.connect()
    table_name1 = "tcu_2"
    table_name2 = "ifm"

    # Validate schema (should print 'passed' if unchanged, warnings if changed)
    Utils.validate_schema(db, table_name1, logger=logger)
    Utils.validate_schema(db, table_name2, logger=logger)

    db.disconnect()

if __name__ == "__main__":
    main()
