"""
create_full_table.py: RecordIn yapısındaki tüm alanlarla tablo oluşturur
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pydbcontrol.db_connector import DBConnector

columns = [
    "id SERIAL PRIMARY KEY",
    "bit_rate FLOAT",
    "tctone_f1_hz FLOAT",
    "tctone_f2_hz FLOAT",
    "tctone_f3_hz FLOAT",
    "tctone_f4 FLOAT",
    "rf_set_time FLOAT",
    "execution_date_wait2 FLOAT",
    "validation_tone FLOAT",
    "rf_fall_time FLOAT",
    "op_mode INT",
    "tc_demod_check INT",
    "shift_key_mode INT",
    "amplitude_ratio FLOAT",
    "pcm_mode INT",
    "idle_pattern INT",
    "idle_pattern_length INT",
    "preamble_length INT",
    "cmm1_clcw INT",
    "cmm2_clcw INT",
    "telemetry_flow_clcw INT",
    "cmm1_offset INT",
    "cmm1_mask INT",
    "cmm1_expected_value INT",
    "cmm2_offset INT",
    "cmm2_mask INT",
    "cmm2_expected_value INT",
    "telemetry_flow_tc INT",
    "tc_rng_priority INT",
    "reserved INT",
    "pcm_modulation_signal INT",
    "pcm_clock INT",
    "convolutional_encoding INT",
    "doppler_compensation INT",
    "scrambler INT",
    "frame_encoding_selection INT",
    "frame_encoding_size INT",
    "frame_encoding_format INT",
    "tcu_status INT",
    "tcu_encoder_status INT",
    "commandstill_expected INT",
    "progress_wait INT",
    "lockedout_status INT",
    "exucition_date_command INT",
    "tcu_factory_setting_licences INT",
    "active_set_testpoints INT",
    "doppler_compensation_status INT",
    "sampling_rate INT",
    "tcdataexecute_counter INT",
    "tcstillwait_modulation INT"
]

table_name = "telecommand_unit2"
create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n  " + ",\n  ".join(columns) + "\n);"

db = DBConnector()
db.connect()
db.execute_query(create_sql, fetch=False)
db.disconnect()
print(f"{table_name} tablosu başarıyla oluşturuldu.")

