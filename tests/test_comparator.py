"""
test_comparator.py: Comparator birim testi
"""
import pytest
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.comparator import Comparator

def test_compare_tables():
    db = DBConnector(host="localhost", database="test_db", user="test", password="test")
    db.connect()
    cmp = Comparator(db)
    diff = cmp.compare_tables("table_a", "table_b", key_column="id")
    assert isinstance(diff, dict)
    db.disconnect()
