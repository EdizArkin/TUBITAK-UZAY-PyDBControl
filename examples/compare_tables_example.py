import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
compare_tables_example.py: Example usage of Comparator to compare multiple tables
"""
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.comparator import Comparator
from pydbcontrol.logger import Logger

def print_diff(title, diff):
    print(f"\n=== {title} ===")
    for k, v in diff.items():
        print(f"{k}:")
        for row in v:
            print(row)

if __name__ == "__main__":
    logger = Logger('pydbcontrol.log')
    db = DBConnector(logger=logger)
    db.connect()
    comp = Comparator(db, logger=logger)

    # 1. Compare ifr_1 and ifr_2
    diff_ifr = comp.compare_tables("ifr_1", "ifr_2", key_column="ifr_id")
    print_diff("IFR_1 vs IFR_2", diff_ifr)

    # 2. Compare tmu_a, tmu_b, tmu_c
    diff_tmu = comp.compare_tables("tmu_a", "tmu_b", "tmu_c", key_column="tmu_id")
    print_diff("TMU_A vs TMU_B vs TMU_C", diff_tmu)

    # 3. Compare global_cortex and tcu_2
    diff_gc_tcu = comp.compare_tables("global_cortex", "tcu_2", key_column="gcu_id")
    print_diff("Global Cortex vs TCU_2", diff_gc_tcu)

    db.disconnect()