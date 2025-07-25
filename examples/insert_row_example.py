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
    # data1 insertion example
    data1 = {"id": 50, "op_mode":2, "shift_key_mode":5}

    # data2 insertion example for testing the automatic id generation
    data2 = {"op_mode":0, "shift_key_mode":6}

    # data3 insertion example for testing the id reordering
    data3 = {"id":35, "op_mode":2, "shift_key_mode":3}

    for data in [data1, data2, data3]:
        table_manager.insert_row(data)

    db.disconnect()

if __name__ == "__main__":
    main()
