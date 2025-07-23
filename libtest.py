from mylib import DBConnector, TableManager

db = DBConnector()
db.connect()

tm = TableManager(db, "telecommand_unit1")
print(tm.table_creator("schema.sql"))

db.disconnect()
