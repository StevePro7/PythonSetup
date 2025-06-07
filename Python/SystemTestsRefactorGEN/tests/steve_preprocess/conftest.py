import json
from loggers.singleton_logger import SingletonLogger


def get_input_file(file_name: str) -> dict:
    file_path = f'payloads/{file_name}'
    with open(file_path, 'r') as file:
        input_file = json.load(file)

    return input_file


def init_logger(app_env: str) -> None:
    log_level: str = "INFO"
    SingletonLogger.instance(log_level, app_env)


def get_extra_logger_data(process_id, trace_id: str) -> dict:
    return {
        'process_id': process_id,
        'trace_id': trace_id
    }

def set_output_file(file_name: str, output_file: dict) -> None:
    file_path = f'payloads/{file_name}'
    with open(file_path, 'w') as file:
        json.dump(output_file, file, indent=2)