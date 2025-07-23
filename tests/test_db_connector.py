"""
test_db_connector.py: DBConnector unit testing
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pydbcontrol.db_connector import DBConnector
def test_connect_disconnect():
    db = DBConnector()
    conn = db.connect()
    print(f"Connection status: {conn is not None}")
    assert conn is not None
    db.disconnect()
    print("Disconnected successfully.")
    assert db.conn is None
