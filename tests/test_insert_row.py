import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector

def test_insert_row():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit2"
    table_manager = TableManager(db, table_name)
    data = {"id": 2001, "command": "TEST_INSERT", "value": 123}
    table_manager.insert_row(data)
    result = table_manager.get_data(filters={"id": 2001}, limit=1)
    assert result and result[0]["command"] == "TEST_INSERT"
    # Clean up
    table_manager.delete_row(2001)
    db.disconnect()
