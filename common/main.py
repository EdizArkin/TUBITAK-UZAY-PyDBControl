from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel, Field, create_model
from typing import Optional, List, Dict, Any
import psycopg2
from psycopg2.extras import RealDictCursor
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

TABLE_NAME = "telecommand_unit2"

class RecordIn(BaseModel):
    bit_rate: Optional[float] = Field(None, description="Bit Rate of the telecommand unit")
    tctone_f1_hz: Optional[float] = Field(None, description="TC Tone Frequency 1 in Hz")
    tctone_f2_hz: Optional[float] = Field(None, description="TC Tone Frequency 2 in Hz")
    tctone_f3_hz: Optional[float] = Field(None, description="TC Tone Frequency 3 in Hz")
    tctone_f4: Optional[float] = Field(None, description="TC Tone Frequency 4")
    rf_set_time: Optional[float] = Field(None, description="RF Set Time")
    execution_date_wait2: Optional[float] = Field(None, description="Execution Date Wait 2")
    validation_tone: Optional[float] = Field(None, description="Validation Tone")
    rf_fall_time: Optional[float] = Field(None, description="RF Fall Time")
    op_mode: Optional[int] = Field(None, description="Operational Mode")
    tc_demod_check: Optional[int] = Field(None, description="TC Demodulation Check")
    shift_key_mode: Optional[int] = Field(None, description="Shift Key Mode")
    amplitude_ratio: Optional[float] = Field(None, description="Amplitude Ratio")
   
    pcm_mode: Optional[int] = Field(None, description="PCM Mode")
    idle_pattern: Optional[int] = Field(None, description="Idle Pattern")
    idle_pattern_length: Optional[int] = Field(None, description="Idle Pattern Length")
    preamble_length: Optional[int] = Field(None, description="Preamble Length")
    cmm1_clcw: Optional[int] = Field(None, description="CMM1 CLCW")
    cmm2_clcw: Optional[int] = Field(None, description="CMM2 CLCW")
    telemetry_flow_clcw: Optional[int] = Field(None, description="Telemetry Flow CLCW")
    cmm1_offset: Optional[int] = Field(None, description="CMM1 Offset")
    cmm1_mask: Optional[int] = Field(None, description="CMM1 Mask")
    cmm1_expected_value: Optional[int] = Field(None, description="CMM1 Expected Value")
    cmm2_offset: Optional[int] = Field(None, description="CMM2 Offset")
    cmm2_mask: Optional[int] = Field(None, description="CMM2 Mask")
    cmm2_expected_value: Optional[int] = Field(None, description="CMM2 Expected Value")

    telemetry_flow_tc: Optional[int] = Field(None, description="Telemetry Flow TC")
    tc_rng_priority: Optional[int] = Field(None, description="TC Ranging Priority")
    reserved: Optional[int] = Field(None, description="Reserved Field")
    
    pcm_modulation_signal: Optional[int] = Field(None, description="PCM Modulation Signal")
    pcm_clock: Optional[int] = Field(None, description="PCM Clock")
    convolutional_encoding: Optional[int] = Field(None, description="Convolutional Encoding")
    doppler_compensation: Optional[int] = Field(None, description="Doppler Compensation")
    scrambler: Optional[int] = Field(None, description="Scrambler")
    frame_encoding_selection: Optional[int] = Field(None, description="Frame Encoding Selection")
    frame_encoding_size: Optional[int] = Field(None, description="Frame Encoding Size")
    frame_encoding_format: Optional[int] = Field(None, description="Frame Encoding Format")
    tcu_status: Optional[int] = Field(None, description="TCU Status")
    tcu_encoder_status: Optional[int] = Field(None, description="TCU Encoder Status")
    commandstill_expected: Optional[int] = Field(None, description="Commands Still Expected")
    progress_wait: Optional[int] = Field(None, description="Progress Wait")
    lockedout_status: Optional[int] = Field(None, description="Locked Out Status")
    exucition_date_command: Optional[int] = Field(None, description="Execution Date Command")
    tcu_factory_setting_licences: Optional[int] = Field(None, description="TCU Factory Setting Licenses")
    active_set_testpoints: Optional[int] = Field(None, description="Active Set Testpoints")
    doppler_compensation_status: Optional[int] = Field(None, description="Doppler Compensation Status")
    sampling_rate: Optional[int] = Field(None, description="Sampling Rate")
    tcdataexecute_counter: Optional[int] = Field(None, description="TC Data Execute Counter")
    tcstillwait_modulation: Optional[int] = Field(None, description="TC Still Wait Modulation")

COLUMN_MAPPING = {}
for field_name, field_info in RecordIn.model_fields.items():
    python_type = field_info.annotation
    if hasattr(python_type, '__origin__') and python_type.__origin__ is Optional:
        base_type = python_type.__args__[0]
    else:
        base_type = python_type
    type_str = str(base_type).replace("<class '", "").replace("'>", "")
    COLUMN_MAPPING[field_name] = {
        "type": type_str,
        "description": field_info.description if field_info.description else f"No description for {field_name}"
    }

class SetParamInput(BaseModel):
    param_name: str = Field(..., description="Name of the parameter to set (e.g., 'bit_rate')")
    param_value: Any = Field(..., description="Value to set for the parameter")

class SetParamOutput(BaseModel):
    success: bool = Field(..., description="True if the parameter was successfully set, False otherwise")

class GetParamOutput(BaseModel):
    value: Optional[Any] = Field(None, description="The value of the requested parameter")
    column_mapping: Dict[str, Dict[str, str]] = Field(..., description="A dictionary mapping column names to their types and descriptions")
#burda veritabanı ayarları değiştirlcek
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="cortex_veritabani",
        user="seydanur",
        password="211905",
        port=5432
    )

@app.get("/records/", response_model=List[RecordIn])
def get_records(limit: Optional[int] = 10):
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                sql = f"SELECT * FROM {TABLE_NAME} LIMIT %s"
                cursor.execute(sql, (limit,))
                rows = cursor.fetchall()
                return rows
    except Exception as e:
        logger.error(f"Get records error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.post("/records/", response_model=dict)
def insert_record(record: RecordIn):
    try:
        fields = []
        values = []
        placeholders = []
        for k, v in record.dict(exclude_unset=True).items():
            fields.append(k)
            values.append(v)
            placeholders.append("%s")
        
        if not fields:
            raise HTTPException(status_code=400, detail="No fields provided")
        
        with get_connection() as conn:
            with conn.cursor() as cursor:
                sql = f"INSERT INTO {TABLE_NAME} ({', '.join(fields)}) VALUES ({', '.join(placeholders)}) RETURNING id"
                cursor.execute(sql, values)
                new_id = cursor.fetchone()[0]
                conn.commit()
                return {"id": new_id}
    except Exception as e:
        logger.error(f"Insert record error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.put("/records/{record_id}", response_model=dict)
def update_record(record_id: int, record: RecordIn):
    try:
        update_data = record.dict(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields provided for update")
        
        set_clause = ", ".join([f"{k} = %s" for k in update_data.keys()])
        values = list(update_data.values())
        values.append(record_id)
        
        with get_connection() as conn:
            with conn.cursor() as cursor:
                sql = f"UPDATE {TABLE_NAME} SET {set_clause} WHERE id = %s RETURNING id"
                cursor.execute(sql, values)
                updated = cursor.fetchone()
                if updated is None:
                    raise HTTPException(status_code=404, detail="Record not found")
                conn.commit()
                return {"updated_id": updated[0]}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Update record error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.put("/records/{record_id}/param", response_model=SetParamOutput)
def set_param_tcu(record_id: int, param_input: SetParamInput):
    """
    Sets a specific parameter (column) value for a given TCU record by its ID.
    Returns True if the parameter was successfully set, False otherwise.
    """
    param_name = param_input.param_name
    param_value = param_input.param_value

    if param_name not in COLUMN_MAPPING:
        raise HTTPException(status_code=400, detail=f"Invalid parameter name: '{param_name}'. Must be one of: {', '.join(COLUMN_MAPPING.keys())}")

    try:
        field_type_annotation = RecordIn.model_fields[param_name].annotation
        DynamicValidationModel = create_model(
            'DynamicValidationModel',
            value=(field_type_annotation, ...)
        )
        DynamicValidationModel(value=param_value)
    except Exception as e:
        logger.error(f"Parameter value validation failed for {param_name} with value '{param_value}': {e}")
        raise HTTPException(status_code=422, detail=f"Invalid value type for parameter '{param_name}': {e}")

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                sql = f"UPDATE {TABLE_NAME} SET {param_name} = %s WHERE id = %s"
                cursor.execute(sql, (param_value, record_id))
                rows_affected = cursor.rowcount
                conn.commit()
                if rows_affected > 0:
                    return SetParamOutput(success=True)
                else:
                    return SetParamOutput(success=False)
    except Exception as e:
        logger.error(f"set_param_tcu error: {e}")
        return SetParamOutput(success=False)

@app.get("/records/{record_id}/param/{param_name}", response_model=GetParamOutput)
def get_param_tcu(record_id: int, param_name: str):
    """
    Retrieves the value of a specific parameter for a given TCU record by its ID.
    Also returns a dictionary mapping all column names to their types and descriptions.
    """
    if param_name not in COLUMN_MAPPING:
        raise HTTPException(status_code=400, detail=f"Invalid parameter name: '{param_name}'. Must be one of: {', '.join(COLUMN_MAPPING.keys())}")

    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                sql = f"SELECT {param_name} FROM {TABLE_NAME} WHERE id = %s"
                cursor.execute(sql, (record_id,))
                record = cursor.fetchone()

                if record is None:
                    raise HTTPException(status_code=404, detail="Record not found")

                param_value = record.get(param_name)
                
                return GetParamOutput(value=param_value, column_mapping=COLUMN_MAPPING)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"get_param_tcu error: {e}")
        raise HTTPException(status_code=500, detail="Database error")


