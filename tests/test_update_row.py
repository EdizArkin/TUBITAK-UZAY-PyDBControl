import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pydbcontrol.table_manager import TableManager
from pydbcontrol.db_connector import DBConnector

def test_update_row():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit2"
    table_manager = TableManager(db, table_name)
    # Insert a row to update
    data = {"id": 2002, "command": "TO_UPDATE", "value": 1}
    table_manager.insert_row(data)
    # Update the row
    new_values = {"command": "UPDATED_ROW", "value": 2}
    table_manager.update_row(2002, new_values)
    result = table_manager.get_data(filters={"id": 2002}, limit=1)
    assert result and result[0]["command"] == "UPDATED_ROW"
    # Clean up
    table_manager.delete_row(2002)
    db.disconnect()
