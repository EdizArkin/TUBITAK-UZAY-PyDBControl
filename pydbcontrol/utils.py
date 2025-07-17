"""
Utils: Yardımcı fonksiyonlar ve şema doğrulama işlemleri.
"""
class Utils:
    @staticmethod
    def validate_schema(table_columns: list, expected_columns: list) -> bool:
        """
        Tablo kolonlarının beklenen şemaya uyup uymadığını kontrol eder.
        """
        return set(table_columns) == set(expected_columns)
