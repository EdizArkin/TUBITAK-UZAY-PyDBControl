"""
create_full_table.py: Example script to create a full table from an SQL model file
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector

# Initialize database connection
db = DBConnector()
    
db.connect()

# Initialize TableManager
table_manager = TableManager(db, "telecommand_unit_2")

# Path to your SQL model file
sql_model_path = "model/telecommand_unit_2.sql"

# Create table from SQL model
result = table_manager.table_creator(sql_model_path)
print(result)

# Disconnect from database
db.disconnect()
