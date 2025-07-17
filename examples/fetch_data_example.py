"""
fetch_data_example.py: Tablo verisi çekme örneği
"""
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager

# Bağlantı parametreleri
conn = DBConnector(host="localhost", database="cortex_veritabani", user="seydanur", password="211905")
conn.connect()

# Tablo yöneticisi
tm = TableManager(conn, "telecommand_unit2")

# Filtreli veri çekme
filters = {"op_mode": 1}
data = tm.get_data(filters=filters, limit=5)
print(data)

conn.disconnect()
