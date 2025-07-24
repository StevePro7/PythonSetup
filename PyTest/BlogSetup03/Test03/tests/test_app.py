import http
from src.app import get_user_name

def test_get_user_name(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = http.HTTPStatus.OK
    mock_response.json.return_value = {'name': 'Test'}
    #mocker.patch('app.requests.get', return_value=mock_response)
    mocker.patch('src.app.requests.get', return_value=mock_response)
    result = get_user_name(1)
    assert result == 'Test'