"""
create_full_table.py: Example script to create a full table from an SQL model file
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.logger import Logger

# Initialize database connection
logger = Logger('pydbcontrol.log')
db = DBConnector(logger=logger)

db.connect()

# Initialize TableManager
table_manager = TableManager(db, "tcu_2", logger=logger)

# Path to your SQL model file
sql_model_path = "model/tcu_2.sql"

# Create table from SQL model
result = table_manager.table_creator(sql_model_path)
print(result)

# Disconnect from database
db.disconnect()
