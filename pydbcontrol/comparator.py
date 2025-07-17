"""
Comparator: Yapısı aynı olan iki tabloyu karşılaştıran sınıf.
"""
from .db_connector import DBConnector

class Comparator:
    def __init__(self, db: DBConnector):
        """
        DBConnector nesnesi ile başlatılır.
        """
        self.db = db

    def compare_tables(self, table1: str, table2: str, key_column: str = 'id'):
        """
        İki tabloyu anahtar kolona göre karşılaştırır, farkları döndürür.
        """
        sql1 = f"SELECT * FROM {table1}"
        sql2 = f"SELECT * FROM {table2}"
        data1 = self.db.execute_query(sql1)
        data2 = self.db.execute_query(sql2)
        set1 = {row[key_column]: row for row in data1}
        set2 = {row[key_column]: row for row in data2}
        diff = {
            'only_in_table1': [v for k, v in set1.items() if k not in set2],
            'only_in_table2': [v for k, v in set2.items() if k not in set1],
            'different_rows': [
                {'id': k, 'table1': set1[k], 'table2': set2[k]}
                for k in set1.keys() & set2.keys() if set1[k] != set2[k]
            ]
        }
        return diff
