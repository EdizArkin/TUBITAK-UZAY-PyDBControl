-- 1010h: telecommand_unit_2
CREATE TABLE tcu_2(
    id serial PRIMARY KEY,
    bit_rate FLOAT  CHECK(bit_rate BETWEEN 10 AND 5000000),
    tctone_f1_hz FLOAT   CHECK(tctone_f1_hz BETWEEN 100 AND 100000),
    tctone_f2_hz FLOAT  CHECK(tctone_f1_hz BETWEEN 100 AND 100000),
    tctone_f3_hz FLOAT CHECK(tctone_f1_hz BETWEEN 100 AND 100000),
    tctone_f4  FLOAT   CHECK(tctone_f4 BETWEEN  0 and 2000000),
    op_mode INT CHECK(op_mode IN(0,2)),
    tc_demod_check INT  CHECK(tc_demod_check IN(0,1)),
    shift_key_mode INT  CHECK(shift_key_mode IN (0,1,2,3,4,5,6)),
    validation_tone FLOAT  CHECK(validation_tone BETWEEN 0 AND 360),
    pcm_mode INT  CHECK(pcm_mode IN(0,1,2,3,4,5,6)),
    IDLE_pattern  INT ,
    IDLE_pattern_length INT   CHECK(IDLE_pattern_length IN(0,1,8192,16352,32832)),
    preamble_length INT   CHECK(preamble_length BETWEEN 2 AND 16777214),
    rf_set_time FLOAT   CHECK (rf_set_time BETWEEN 0 AND 9999.99),
    CMM1_CLCW INT CHECK(CMM1_CLCW IN(0,1)),
    CMM2_CLCW INT   CHECK(CMM1_CLCW IN(0,1)),
    telemetry_flow_clcw INT  CHECK(telemetry_flow_clcw IN(0,1,2,3,4,5,6,7)),
    CMM1_OFFSET INT  CHECK(CMM1_OFFSET BETWEEN 0 AND 2043),
    CMM1_mask BIGINT  CHECK(CMM1_mask IN(1,3735928559)),
    CMM1_expected_value BIGINT CHECK(CMM1_expected_value IN(1,3735928559)),
    CMM2_offset INT  CHECK(CMM2_offset BETWEEN 0 AND 2043),
    CMM2_MASK  BIGINT  CHECK(CMM2_MASK IN(1,3735928559)),
    CMM2_expected_value BIGINT  CHECK(CMM2_expected_value IN (1,3735928559)),
    RF_fall_time FLOAT CHECK(RF_fall_time BETWEEN 0 AND 9999.99),
    telemetry_flow_TC INT CHECK(telemetry_flow_TC IN (0,1,2,3,4,5,6,7)),
    TC_RNG_priority INT CHECK(TC_RNG_priority IN (0,1)),
    reserved INT,
    amplitude_ratio FLOAT   CHECK(amplitude_ratio BETWEEN 0 AND 1),
    PCM_modulation_signal INT  CHECK(PCM_modulation_signal IN(0,1)),
    PCM_clock INT  CHECK(PCM_clock IN(0,1)),
    convolutional_encoding INT  CHECK(convolutional_encoding IN(0,1,2,3,4,5,6,7)),
    doppler_compensation INT  CHECK(doppler_compensation IN(0,1)),
    scrambler INT   CHECK(scrambler IN(0,1)),
    FRAME_encoding_selection INT CHECK(FRAME_encoding_selection BETWEEN 0 AND 255),
    FRAME_encoding_size INT  CHECK(FRAME_encoding_size BETWEEN 0 AND 16384),
    FRAME_encoding_format INT CHECK(FRAME_encoding_format IN(0,1)),
    TCU_status INT  CHECK(TCU_status IN(0,1)),
    TCU_encoder_status INT  CHECK(TCU_encoder_status IN(0,1,2,3,4,5,6,7)),
    commandstill_expected INT  CHECK(commandstill_expected BETWEEN 0 AND 32),
    progress_wait INT CHECK(progress_wait IN(0,1)),
    lockedout_status INT  CHECK(lockedout_status IN(0,1)),
    exucition_date_command INT ,
    execution_date_wait2 FLOAT ,
    TCU_factory_setting_licences INT ,
    active_set_testpoints INT   CHECK(active_set_testpoints IN(0,1,2,3,4)),
    doppler_compensation_status INT CHECK(doppler_compensation_status IN(0,1,2,3)),
    sampling_rate INT    CHECK(sampling_rate IN(0,1,2)),
    tcdataexecute_counter INT NULL,
    tcstillwait_modulation INT NULL
);
