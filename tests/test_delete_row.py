import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector

def test_delete_row():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit2"
    table_manager = TableManager(db, table_name)
    # Insert a row to delete
    data = {"id": 2003, "command": "TO_DELETE", "value": 3}
    table_manager.insert_row(data)
    # Delete the row
    table_manager.delete_row(2003)
    result = table_manager.get_data(filters={"id": 2003}, limit=1)
    assert not result
    db.disconnect()
