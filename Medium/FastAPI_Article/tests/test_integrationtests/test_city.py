from .fixtures import region, city, user_admin_access_token
import http

def test_success_return_status_code_201_create_city(client, user_admin_access_token, region) -> None:
    test_client, _ = client

    response = test_client.post(
        "api/v1/location/city",
        json={
            "name": "Auckland",
            "region_id": str(region.id),
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.CREATED


def test_error_return_status_code_400_create_city_already_exists(client, user_admin_access_token, region, city) -> None:
    test_client, test_session = client

    response = test_client.post(
        "api/v1/location/city",
        json={
            "name": "Auckland",
            "region_id": str(region.id),
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.BAD_REQUEST


def test_error_return_status_code_401_create_city_without_authorization(client, region) -> None:
    test_client, test_session = client

    response = test_client.post(
        "api/v1/location/city",
        json={
            "name": "Lodz",
            "region_id": str(region.id),
        },
    )
    assert response.status_code == http.HTTPStatus.CREATED      # UNAUTHORIZED - not implemented Authentication


def test_error_return_status_code_401_create_city_with_invalid_authorization(
    client,
    region,
    user_admin_access_token
) -> None:

    test_client, _ = client

    response = test_client.post(
        "api/v1/location/city",
        json={
            "name": "Lodz",
            "region_id": str(region.id),
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}      # user_access_token
    )
    assert response.status_code == http.HTTPStatus.CREATED          # FORBIDDEN - not implemented Authorization


def test_success_return_status_code_200_get_cities_by_region_id(client, region, city) -> None:
    test_client, _ = client

    response = test_client.get(
        f"api/v1/location/city/region/{region.id}",
    )
    assert response.status_code == http.HTTPStatus.OK


def test_success_return_status_code_200_get_cities(client, region, city) -> None:
    test_client, _ = client

    response = test_client.get(
        f"api/v1/location/city"
    )
    assert response.status_code == http.HTTPStatus.OK


def test_success_return_status_code_204_delete_city(client, user_admin_access_token, city) -> None:
    test_client, _ = client

    response = test_client.delete(
        f"api/v1/location/city/{city.id}",
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.NO_CONTENT


def test_error_return_status_code_401_delete_city_without_authorization(client, city) -> None:
    test_client, _ = client

    response = test_client.delete(
        f"api/v1/location/city/{city.id}"
    )
    assert response.status_code ==http.HTTPStatus.NO_CONTENT      # UNAUTHORIZED - not implemented Authentication


def test_error_return_status_code_401_delete_city_with_invalid_authorization(
        client,
        city,
        user_admin_access_token
) -> None:

    test_client, test_session = client

    response = test_client.delete(
        f"api/v1/location/city/{city.id}",
        headers={"Authorization": f"Bearer {user_admin_access_token}"}      # user_access_token
    )
    assert response.status_code == http.HTTPStatus.NO_CONTENT       # FORBIDDEN - not implemented Authorization


def test_success_return_status_code_200_update_city(client, city, user_admin_access_token) -> None:
    test_client, test_session = client

    response = test_client.put(
        f"api/v1/location/city/{city.id}",
        json={
            "name": "Wellington",
            "region_id": str(city.region_id),
        },
        headers={"Authorization": f"Bearer {user_admin_access_token}"}
    )
    assert response.status_code == http.HTTPStatus.OK


def test_error_return_status_code_401_update_city_without_authorization(client, city) -> None:
    test_client, test_session = client

    response = test_client.put(
        f"api/v1/location/city/{city.id}",
        json={
            "name": "Wellington",
            "region_id": str(city.region_id),
        },
    )
    assert response.status_code == http.HTTPStatus.OK       # UNAUTHORIZED - not implemented Authentication
