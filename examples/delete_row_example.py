import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector

def main():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit_2"
    table_manager = TableManager(db, table_name)
    row_id = 10
    table_manager.delete_row(row_id)
    db.disconnect()

if __name__ == "__main__":
    main()
