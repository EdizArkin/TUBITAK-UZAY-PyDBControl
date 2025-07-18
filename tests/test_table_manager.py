"""
test_table_manager.py: Unit test for TableManager class
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager

def test_get_data():
    db = DBConnector()
    db.connect()
    tm = TableManager(db, "telecommand_unit2")
    result = tm.get_data(limit=1)
    assert isinstance(result, list)
    db.disconnect()
