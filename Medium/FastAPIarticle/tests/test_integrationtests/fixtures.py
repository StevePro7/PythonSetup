import pytest
# from auth.security import get_password_hash
# from models.offer import CategoryEnum, SubCategoryEnum, BuildingTypeEnum
from repository.city_repository import CityRepository
# from repositories.offer_repository import OfferRepository
from repository.region_repository import RegionRepository
# from repositories.user_repository import UserRepository
from schemas.region_schema import RegionInput
from schemas.city_schema import CityInput
# from schemas.offer import OfferScraper
# from schemas.photo import PhotoInput
# from schemas.user import UserIn
# from schemas.favourite import FavouriteInput
# from repositories.favourite_repository import FavouriteRepository
# from repositories.notification_repository import NotificationRepository
# from repositories.notificationfilter_repository import NotificationFilterRepository
# from schemas.notification import NotificationInput
# from schemas.notification_filter import NotificationFilterInput


@pytest.fixture(scope="function")
def region(client):
    test_client, db_session = client

    region = RegionRepository(db_session).create(RegionInput(name="NorthIs"))
    return region


@pytest.fixture(scope="function")
def city(client, region):
    test_client, db_session = client

    city = CityRepository(db_session).create(CityInput(name="Auckland", region_id=region.id))
    return city


@pytest.fixture(scope="function")
def user_admin_access_token(client):
    test_client, _ = client

    #data = {'grant_type': '', 'username': 'XXXX', 'password': 'XXXX', 'scope': '', 'client_id': '', 'client_secret': ''}
    # access_token = test_client.post(
    #     "/api/v1/user/login",
    #     data=data,
    # ).json()["access_token"]
    #return access_token
    return "personal_access_token"