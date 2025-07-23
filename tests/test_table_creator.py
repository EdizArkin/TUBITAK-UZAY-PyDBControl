"""
test_table_creator.py: TableManager.table_creator function unit testing
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager

def test_table_creator():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit2"
    tm = TableManager(db, table_name)
    model_sql_path = os.path.join("model", "telecommand_unit2.sql")
    result = tm.table_creator(model_sql_path)
    assert "Created succesfully" in result
    print(f"{table_name} table created successfully.")
    db.disconnect()

