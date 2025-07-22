from db_connector import DBConnector
from tablemanager import TableManager
from logger import Logger

def test_table_manager():
    logger = Logger()
    db = DBConnector()  
    db.connect()

    table_name = "telecommand_unit2" 
    tm = TableManager(db, table_name, logger)

    result = tm.get_data(limit=5)
    print(f"Tablodan çekilen veri: {result}")

    db.disconnect()

if __name__ == "__main__":
    test_table_manager()
