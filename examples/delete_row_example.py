import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.logger import Logger

def main():
    logger = Logger('pydbcontrol.log')
    db = DBConnector(logger=logger)
    db.connect()
    table_name = "tcu_2"
    table_manager = TableManager(db, table_name, logger=logger)
    row_id = 10
    table_manager.delete_row(row_id)
    db.disconnect()

if __name__ == "__main__":
    main()
