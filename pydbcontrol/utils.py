"""
Utils: Helper functions and schema validation operations.
"""
class Utils:
    @staticmethod
    def validate_schema(table_columns: list, expected_columns: list) -> bool:
        """
        Checks whether the table columns conform to the expected schema.
        Catches and prints user-friendly error messages if validation fails.
        """
        try:
            return set(table_columns) == set(expected_columns)
        except Exception as e:
            print(f"Utils error during schema validation: {e}")
            return False
