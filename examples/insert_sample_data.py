"""
insert_sample_data.py: Example inserts 10 rows of data into the telecommand_unit2 table
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import random
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager

db = DBConnector()
db.connect()
tm = TableManager(db, "telecommand_unit2")

for i in range(10):
    data = {
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
    tm.insert_row(data)
    print(f"{i+1}. row added.")

db.disconnect()
print("10 rows of data were added successfully.")
