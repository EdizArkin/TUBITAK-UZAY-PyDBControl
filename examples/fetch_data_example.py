"""
fetch_data_example.py: Example script to fetch data from a specific table with filters
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager
from pydbcontrol.logger import Logger

# Connection parameters
logger = Logger('pydbcontrol.log')
db = DBConnector(logger=logger)
db.connect()

# Table manager
tm = TableManager(db, "tcu_2", logger=logger)

# Filtered data retrieval
filters = {"op_mode": 2,
           "shift_key_mode": 5}
data = tm.get_data(filters=filters, limit=5)
print(f'Requested data: ', data)

db.disconnect()
