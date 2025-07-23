"""
test_comparator.py: The table comparison Test is not currently in development and testing phase
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
