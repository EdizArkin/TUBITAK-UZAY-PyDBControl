import pytest
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.utils import Utils

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_schema_validation():
    db = DBConnector()
    db.connect()
    table_name = "telecommand_unit2"
    # Store initial schema
    Utils.store_initial_schema(db, table_name)
    # Should pass if schema unchanged
    assert Utils.validate_schema(db, table_name) is True
    # Simulate schema change by removing a column from initial_schemas
    if table_name in Utils._initial_schemas:
        Utils._initial_schemas[table_name] = set(list(Utils._initial_schemas[table_name])[1:])
        assert Utils.validate_schema(db, table_name) is False
    db.disconnect()
