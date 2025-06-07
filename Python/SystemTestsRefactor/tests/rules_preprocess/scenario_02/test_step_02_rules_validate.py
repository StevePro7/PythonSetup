import json
import uuid
from app.config.constants import LOG_RULES_ENGINE
from app.rules_process.rules_validate import rules_validate
from loggers.singleton_logger import SingletonLogger

def test_rules_validate():


    file_path = 'payloads/test_step_01_inp_obj.json'
    with open(file_path, 'r') as file:
        inp_obj = json.load(file)

    trace_id: str = 'a82258ea-924c-462f-867d-cb55a417c91a'
    process_id: str = "test_02"

    log_level: str = "INFO"
    app_env: str = "SIT"
    SingletonLogger.instance(log_level, app_env)

    extra_logger_data = {
        'process_id': process_id,
        'trace_id': trace_id
    }

    context, out_obj = rules_validate(inp_obj, LOG_RULES_ENGINE, extra_logger_data)
    assert out_obj is not None

    # Save output
    with open('payloads/test_step_02_context.json', 'w') as file1:
        json.dump(context, file1, indent=2)

    with open('payloads/test_step_02_out_obj.json', 'w') as file2:
        json.dump(out_obj, file2, indent=2)
