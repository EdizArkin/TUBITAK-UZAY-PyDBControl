"""
test_db_connector.py: DBConnector birim testi
"""
import pytest
from pydbcontrol.db_connector import DBConnector

def test_connect_disconnect():
    db = DBConnector(host="localhost", database="test_db", user="test", password="test")
    conn = db.connect()
    assert conn is not None
    db.disconnect()
    assert db.conn is None
