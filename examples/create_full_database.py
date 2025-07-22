import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager
from pydbcontrol.logger import Logger
import re
import random

def get_table_name_from_sql(sql_path):
    with open(sql_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'create table' in line.lower():
                parts = line.strip().split()
                if len(parts) >= 3:
                    return parts[2].replace('(', '').strip().lower()
    return None

def get_columns_from_sql(sql_path):
    columns = []
    pk_col = None
    with open(sql_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    start = False
    for line in lines:
        if 'create table' in line.lower():
            start = True
            continue
        if start:
            if line.strip().startswith(')') or line.strip().endswith(');'):
                break
            if line.strip():
                parts = line.strip().replace(',', '').split()
                if len(parts) >= 2:
                    col_name = parts[0]
                    col_type = parts[1].lower()
                    constraints = line.strip()
                    # Find the CHECK ranges and IN list
                    check_between = re.search(r'between\s+([\-\d\.]+)\s+and\s+([\-\d\.]+)', constraints, re.IGNORECASE)
                    check_in = re.search(r'in\s*\(([^\)]+)\)', constraints, re.IGNORECASE)
                    constraint_info = {}
                    if check_between:
                        constraint_info['between'] = (float(check_between.group(1)), float(check_between.group(2)))
                    if check_in:
                        values = [v.strip() for v in check_in.group(1).split(',')]
                        # If numeric, float/int, otherwise string
                        try:
                            values = [float(v) if '.' in v else int(v) for v in values]
                        except:
                            pass
                        constraint_info['in'] = values
                    # Find the primary key
                    if 'primary key' in constraints.lower():
                        pk_col = col_name
                    columns.append((col_name, col_type, constraint_info))
    return columns, pk_col

def generate_row_data(columns, idx=1):
    # Generate data according to column type and constraints
    data = {}
    for col, col_type, constraint_info in columns:
        # id column
        if col == 'id' or col.endswith('_id'):
            data[col] = idx
        # IN constraint
        elif 'in' in constraint_info:
            values = constraint_info['in']
            data[col] = values[idx % len(values)]
        # BETWEEN constraint
        elif 'between' in constraint_info:
            min_v, max_v = constraint_info['between']
            if 'int' in col_type or 'serial' in col_type or 'bigint' in col_type:
                data[col] = int((min_v + max_v) // 2 + idx - 1)
                # Do not go out of range
                if data[col] < min_v: data[col] = int(min_v)
                if data[col] > max_v: data[col] = int(max_v)
            elif 'float' in col_type or 'double' in col_type or 'real' in col_type:
                data[col] = round((min_v + max_v) / 2 + (idx-1)*0.1, 3)
                if data[col] < min_v: data[col] = min_v
                if data[col] > max_v: data[col] = max_v
            else:
                data[col] = min_v
        # Type based default
        elif 'int' in col_type or 'serial' in col_type or 'bigint' in col_type:
            data[col] = idx
        elif 'float' in col_type or 'double' in col_type or 'real' in col_type:
            data[col] = round(0.5 + idx*0.1, 3)
        elif 'char' in col_type or 'text' in col_type or 'varchar' in col_type:
            data[col] = f"test_{idx}"
        elif 'boolean' in col_type:
            data[col] = True if idx % 2 == 0 else False
        else:
            data[col] = idx
    return data

def main():
    logger = Logger('pydbcontrol.log')
    db = DBConnector()
    db.connect()
    model_dir = os.path.join(os.path.dirname(__file__), '../model')
    sql_files = [os.path.join(model_dir, f) for f in os.listdir(model_dir) if f.endswith('.sql')]
    for sql_path in sql_files:
        table_name = get_table_name_from_sql(sql_path)
        if not table_name:
            print(f"Tablo adı bulunamadı: {sql_path}")
            continue
        print(f"Tablo oluşturuluyor: {table_name}")
        tm = TableManager(db, table_name, logger=logger)
        tm.table_creator(sql_path)
        columns, pk_col = get_columns_from_sql(sql_path)
        for i in range(1, 3):
            row = generate_row_data(columns, idx=i)
            # If the primary key is serial, add
            if pk_col and ('serial' in [col_type for col, col_type, _ in columns if col == pk_col]):
                row.pop(pk_col, None)
            tm.insert_row(row)
    db.disconnect()

if __name__ == "__main__":
    main()
