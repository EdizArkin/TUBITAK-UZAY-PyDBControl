"""
TableManager: Tablo üzerinde okuma, ekleme, güncelleme ve silme işlemlerini yöneten sınıf.
"""
from .db_connector import DBConnector

class TableManager:
    def __init__(self, db: DBConnector, table_name: str):
        """
        Tablo adı ve DBConnector nesnesi ile başlatılır.
        """
        self.db = db
        self.table_name = table_name

    def table_creator(self, model_sql_path: str):
        """
        Belirtilen model klasöründeki .sql dosyasından CREATE TABLE komutunu okuyup çalıştırır.
        """
        with open(model_sql_path, "r", encoding="utf-8") as f:
            sql = f.read()
        self.db.execute_query(sql, fetch=False)
        return f"Created succesfully: {self.table_name}"

    def get_data(self, filters=None, limit=10):
        """
        Tabloyu filtreleyerek veri çeker.
        """
        sql = f"SELECT * FROM {self.table_name}"
        params = []
        if filters:
            where = " AND ".join([f"{k}=%s" for k in filters.keys()])
            sql += f" WHERE {where}"
            params = list(filters.values())
        sql += " LIMIT %s"
        params.append(limit)
        return self.db.execute_query(sql, params)

    def insert_row(self, data: dict):
        """
        Yeni bir satır ekler.
        """
        fields = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({placeholders})"
        self.db.execute_query(sql, list(data.values()), fetch=False)

    def update_row(self, row_id: int, new_values: dict):
        """
        Belirtilen satırı günceller.
        """
        set_clause = ', '.join([f"{k}=%s" for k in new_values.keys()])
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE id=%s"
        params = list(new_values.values()) + [row_id]
        self.db.execute_query(sql, params, fetch=False)

    def delete_row(self, row_id: int):
        """
        Belirtilen satırı siler.
        """
        sql = f"DELETE FROM {self.table_name} WHERE id=%s"
        self.db.execute_query(sql, [row_id], fetch=False)
