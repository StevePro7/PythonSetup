from app.config.constants import LOG_RULES_ENGINE
from app.rules_process.rules_validate import rules_validate
from tests.rules_preprocess.conftest import get_input_file, init_logger, get_extra_logger_data, set_output_file

def test_rules_validate():
    # Test specific inputs.
    app_env: str = "UAT"
    process_id: str = "test_01"
    trace_id: str = '0eddf3b3-55e0-4ed7-8798-bdf3baa857a0'

    # Arrange.
    init_logger(app_env)

    inp_obj = get_input_file('test_step_01_inp_obj.json')
    extra_logger_data = get_extra_logger_data(process_id, trace_id)

    # Act.
    context, out_obj = rules_validate(inp_obj, LOG_RULES_ENGINE, extra_logger_data)
    assert out_obj is not None

    # Assert.
    set_output_file('test_step_02_context.json', context)
    set_output_file('test_step_02_inp_obj.json', out_obj)
