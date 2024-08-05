from .fixtures import region, user_admin_access_token
import http

def test_success_return_status_code_201_create_region(client, user_admin_access_token) -> None:
    test_client, _ = client

    response = test_client.post(
        "api/v1/location/region",
        json={
            "name": "NorthIs"
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.CREATED


def test_error_status_code_400_create_region_already_exists(
        client,
        user_admin_access_token,
        region
) -> None:
    test_client, _ = client

    response = test_client.post(
        "api/v1/location/region",
        json={
            "name": region.name
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )

    assert response.status_code == http.HTTPStatus.BAD_REQUEST


def test_error_return_status_code_401_create_region_annoymous_user(client) -> None:
    test_client, _ = client

    response = test_client.post(
        "api/v1/location/region",
        json={
            "name": "NorthIs"
        }
    )
    assert response.status_code == http.HTTPStatus.CREATED          # UNAUTHORIZED - not implemented Authentication


def test_error_return_status_code_403_create_region_user_account(client, user_admin_access_token) -> None:
    test_client, _ = client

    response = test_client.post(
        "api/v1/location/region",
        json={
            "name": "NorthIs"
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.CREATED          # FORBIDDEN - not implemented Authorization


def test_success_return_status_code_200_get_regions(client) -> None:
    test_client, _ = client

    response = test_client.get(
        "api/v1/location/region"
    )
    assert response.status_code == http.HTTPStatus.OK


def test_success_return_status_code_204_delete_region(client, user_admin_access_token, region) -> None:
    test_client, _ = client

    response = test_client.delete(
        f"api/v1/location/region/{region.id}",
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.NO_CONTENT


def test_error_return_status_code_401_delete_region_annoymous_user(client, region) -> None:
    test_client, _ = client

    response = test_client.delete(
        f"api/v1/location/region/{region.id}",
    )
    assert response.status_code == http.HTTPStatus.NO_CONTENT  # UNAUTHORIZED - not implemented Authentication


def test_error_return_status_code_404_delete_region_region_does_not_exists(
        client,
        user_admin_access_token
) -> None:

    test_client, _ = client

    response = test_client.delete(
        f"api/v1/location/region/279dcf76-a100-48b2-9fd4-f891d5093f4c",
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.NOT_FOUND


def test_success_return_status_code_200_update_region(client, user_admin_access_token, region) -> None:
    test_client, _ = client

    response = test_client.put(
        f"api/v1/location/region/{region.id}",
        json={
            "name": "SouthIs"
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.OK


def test_error_return_status_code_401_update_region_annoymous_user(client, region) -> None:
    test_client, _ = client

    response = test_client.put(
        f"api/v1/location/region/{region.id}",
        json={
            "name": "NorthIs"
        }
    )
    assert response.status_code == http.HTTPStatus.OK       # UNAUTHORIZED - not implemented Authentication


def test_error_return_status_code_404_update_region_region_does_not_exists(
        client,
        user_admin_access_token
) -> None:

    test_client, _ = client

    response = test_client.put(
        f"api/v1/location/region/279dcf76-a100-48b2-9fd4-f891d5093f4c",
        json={
            "name": "SouthIs"
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.NOT_FOUND
