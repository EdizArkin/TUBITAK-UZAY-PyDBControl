import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
logger_db_example.py: Example script to demonstrate logging of real database operations using Logger and SQL model file.
"""
from pydbcontrol.logger import Logger
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager
import os
import random

logger = Logger('pydbcontrol.log')
db = DBConnector()
db.connect()
table_name = "telecommand_unit_2"
table_manager = TableManager(db, table_name, logger=logger)


# 1. Create table from SQL model file
try:
    sql_model_path = "model/telecommand_unit_2.sql"
    result = table_manager.table_creator(sql_model_path)
except Exception as e:
    pass  # Already logged by TableManager

# 2. Insert row
for i in range(2):
    row_data = {
        "bit_rate": random.uniform(10, 5000000),
        "tctone_f1_hz": random.uniform(100, 100000),
        "tctone_f2_hz": random.uniform(100, 100000),
        "tctone_f3_hz": random.uniform(100, 100000),
        "tctone_f4": random.uniform(0, 2000000),
        "op_mode": random.choice([0, 2]),
        "tc_demod_check": random.choice([0, 1]),
        "shift_key_mode": random.choice([0, 1, 2, 3, 4, 5, 6]),
        "validation_tone": random.uniform(0, 360),
        "pcm_mode": random.choice([0, 1, 2, 3, 4, 5, 6]),
        "idle_pattern": random.randint(0, 1000),
        "idle_pattern_length": random.choice([0, 1, 8192, 16352, 32832]),
        "preamble_length": random.randint(2, 16777214),
        "rf_set_time": random.uniform(0, 9999.99),
        "CMM1_CLCW": random.choice([0, 1]),
        "CMM2_CLCW": random.choice([0, 1]),
        "telemetry_flow_clcw": random.choice([0, 1, 2, 3, 4, 5, 6, 7]),
        "CMM1_OFFSET": random.randint(0, 2043),
        "CMM1_mask": random.choice([1, 3735928559]),
        "CMM1_expected_value": random.choice([1, 3735928559]),
        "CMM2_offset": random.randint(0, 2043),
        "CMM2_MASK": random.choice([1, 3735928559]),
        "CMM2_expected_value": random.choice([1, 3735928559]),
        "RF_fall_time": random.uniform(0, 9999.99),
        "telemetry_flow_TC": random.choice([0, 1, 2, 3, 4, 5, 6, 7]),
        "TC_RNG_priority": random.choice([0, 1]),
        "reserved": random.randint(0, 1000),
        "amplitude_ratio": random.uniform(0, 1),
        "PCM_modulation_signal": random.choice([0, 1]),
        "PCM_clock": random.choice([0, 1]),
        "convolutional_encoding": random.choice([0, 1, 2, 3, 4, 5, 6, 7]),
        "doppler_compensation": random.choice([0, 1]),
        "scrambler": random.choice([0, 1]),
        "FRAME_encoding_selection": random.randint(0, 255),
        "FRAME_encoding_size": random.randint(0, 16384),
        "FRAME_encoding_format": random.choice([0, 1]),
        "TCU_status": random.choice([0, 1]),
        "TCU_encoder_status": random.choice([0, 1, 2, 3, 4, 5, 6, 7]),
        "commandstill_expected": random.randint(0, 32),
        "progress_wait": random.choice([0, 1]),
        "lockedout_status": random.choice([0, 1]),
        "exucition_date_command": random.randint(0, 10000),
        "execution_date_wait2": random.uniform(0, 9999.99),
        "TCU_factory_setting_licences": random.randint(0, 1000),
        "active_set_testpoints": random.choice([0, 1, 2, 3, 4]),
        "doppler_compensation_status": random.choice([0, 1, 2, 3]),
        "sampling_rate": random.choice([0, 1, 2]),
        "tcdataexecute_counter": random.randint(0, 1000),
        "tcstillwait_modulation": random.randint(0, 1000)
    }
    try:
        table_manager.insert_row(row_data)
    except Exception as e:
        pass  # Already logged by TableManager

# 3. Update row
try:
    table_manager.update_row(1, {"op_mode": 0})
except Exception as e:
    pass  # Already logged by TableManager

# 4. Select row
try:
    table_manager.get_data(filters={"op_mode": 0}, limit=1)
except Exception as e:
    pass  # Already logged by TableManager

# 5. Delete row
try:
    table_manager.delete_row(1)
except Exception as e:
    pass  # Already logged by TableManager

# Print the log
#logger.print_log()

# Get the log directly
logs = logger.get_log()
print("Logs retrieved from logger:", logs)

# Clear the log file.
#logger.clear_log()

db.disconnect()
print("Logger DB example completed. Check pydbcontrol.log for output.")
