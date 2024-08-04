from .fixtures import region, user_admin_access_token
import http

def test_success_return_status_code_201_create_region(client, user_admin_access_token) -> None:
    test_client, test_session = client

    response = test_client.post(
        "api/v1/location/region",
        json={
            "name": "Auckland"
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.CREATED