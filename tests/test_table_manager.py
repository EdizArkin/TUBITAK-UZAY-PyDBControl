"""
test_table_manager.py: TableManager birim testi
"""
import pytest
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager

def test_get_data():
    db = DBConnector(host="localhost", database="test_db", user="test", password="test")
    db.connect()
    tm = TableManager(db, "test_table")
    result = tm.get_data(limit=1)
    assert isinstance(result, list)
    db.disconnect()
