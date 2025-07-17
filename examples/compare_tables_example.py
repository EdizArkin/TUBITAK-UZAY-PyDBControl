"""
compare_tables_example.py: The table comparison example is not currently in development and testing phase
"""
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.comparator import Comparator

db = DBConnector()
db.connect()

cmp = Comparator(db)
diff = cmp.compare_tables("table_a", "table_b", key_column="id")
print(diff)

db.disconnect()
