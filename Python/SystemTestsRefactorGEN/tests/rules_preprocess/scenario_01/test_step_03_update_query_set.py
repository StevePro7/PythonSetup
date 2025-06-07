from app.config.constants import LOG_RULES_ENGINE
from app.rules_process.update_query_set import update_query_set
from tests.rules_preprocess.conftest import get_input_file, init_logger, get_extra_logger_data, set_output_file

def test_update_query_set():
    # Test specific inputs.
    app_env: str = "UAT"
    process_id: str = "test_03"
    trace_id: str = 'fb498b32-521a-4743-9fdd-4de952b4b6c9'

    # Arrange.
    init_logger(app_env)

    request_data = get_input_file('test_step_03_inp_obj.json')
    context_file = get_input_file('test_step_03_context.json')
    extra_logger_data = get_extra_logger_data(process_id, trace_id)

    # Act.
    context, out_obj = update_query_set(context_file, request_data, LOG_RULES_ENGINE, extra_logger_data)
    assert out_obj is not None

    # Assert.
    set_output_file('test_step_04_context.json', context)
    set_output_file('test_step_04_inp_obj.json', out_obj)
