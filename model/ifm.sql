-- 1040h: ifm
Create table ifm(
    ifm_id serial primary key not null,
    carrier_frequency_offset float Check(carrier_frequency_offset BETWEEN -1000 AND 1000),
    carrier_frequency float Check(carrier_frequency BETWEEN 0  and 1000000000000),
    frequency_pd_tcu float Check(frequency_pd_tcu BETWEEN 0 AND 500000 ),
    frequency_pd_rau float Check(frequency_pd_rau BETWEEN 0 AND 500000),
    frequency_pd_tms1 float  Check(frequency_pd_tms1 BETWEEN 0 AND 5000000),
    modindex_tcu float Check(modindex_tcu BETWEEN 0 AND 2.5),
    modindex_rau float Check(modindex_rau BETWEEN 0 AND 2.5),
    modindex_tms1 float Check(modindex_tms1 BETWEEN 0 AND 2.5),
    op_modeifm integer Check(op_modeifm In(0,1,2,3,4,5,6,7,8,9)),
    mod_signal integer Check(mod_signal In(0,1)),
    modulation integer Check(modulation In(0,1)),
    if_carrier integer,
    if_carrier_level float Check(if_carrier_level BETWEEN -80 AND 10),
    if_sweep integer Check(if_sweep IN(0,1,2,3,4,5,6)),
    sweep_rate float Check(sweep_rate BETWEEN 1000 AND 1000000),
    sweep_offset float Check( sweep_offset BETWEEN -1000000 AND 1000000 ),
    spectanalysis_span integer Check(spectanalysis_span BETWEEN 0 AND 18),
    frequency_pd_aux float Check(frequency_pd_aux  BETWEEN 0 AND 5000000),
    modindex_aux float Check(modindex_aux BETWEEN 0 AND 2.5 ),
    frequency_pd_pcm float Check(frequency_pd_pcm BETWEEN 0 AND 500000),
    modindex_pcm float Check(modindex_pcm BETWEEN 0 AND 2.5),
    reservedifm integer,
    matchedfilter0 integer Check(matchedfilter0 IN(0,1,2)),
    matchedfilter1 integer Check(matchedfilter1 IN(0,1,2,3)),
    roll_offactor0 float Check(roll_offactor0 BETWEEN 0.1 AND 1.0),
    bts float  Check(bts BETWEEN 0.1 AND 1.0),
    progressive_modindex integer Check(progressive_modindex IN(0,1)),
    sweep_stepsize float Check(sweep_stepsize BETWEEN 10 AND 100000),
    facton_dback float Check(facton_dback BETWEEN -8.0 AND 0.01),
    bpsk_scf float Check(bpsk_scf BETWEEN 0 AND 1200000),
    ifr_selectdback integer Check(ifr_selectdback IN(0,1,2,3,4,5)),
    frequency_pd_tms2 float Check(frequency_pd_tms2 BETWEEN 0 AND 5000000),
    modindex_tms2 float Check(modindex_tms2 BETWEEN 0 AND 2.5),
    iffilter_bandwith integer Check(iffilter_bandwith BETWEEN 0 AND 14),
    qpsk_encoding integer,
    psk_map8 integer,
    ıq_ratio float Check(ıq_ratio BETWEEN -20 AND 20),
    carrier_frequency_offset2 float,
    frequency_pd1 float,
    modindex1 float,
    hw_status1 integer,
    hw_status2 integer,
    spectanalysis_range integer,
    ifoutput_range integer Check(ifoutput_range IN(0,1,2)),
    carrier_status integer Check(carrier_status IN(0,1)),
    ifm_setting integer,
    ifm_model integer,
    doppler_compstatus integer Check(doppler_compstatus IN(0,1,2,3)),
    carrier_frequency_compensation float,
    mod_signaleffective integer
);

