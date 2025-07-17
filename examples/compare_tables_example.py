"""
compare_tables_example.py: Tablo karşılaştırma örneği
"""
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.comparator import Comparator

conn = DBConnector(host="localhost", database="cortex_veritabani", user="seydanur", password="211905")
conn.connect()

cmp = Comparator(conn)
diff = cmp.compare_tables("table_a", "table_b", key_column="id")
print(diff)

conn.disconnect()
