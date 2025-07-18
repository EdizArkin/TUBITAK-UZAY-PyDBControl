import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector

def main():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit2"
    table_manager = TableManager(db, table_name)
    row_id = 35

    # Example of updating a row with new values 
    # row_id = 35 --- IGNORE --- Since the row id can no longer be changed, the remaining changes are applied to row id:35.
    new_values = {"id": 53, "op_mode":0, "shift_key_mode":5}
    table_manager.update_row(row_id, new_values)
    db.disconnect()

if __name__ == "__main__":
    main()
