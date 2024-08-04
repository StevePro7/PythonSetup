from typing import List
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from repository.city_repository import CityRepository
from repository.region_repository import RegionRepository
from schemas.city_schema import CityInput, CityOutput
import http


class CityService:
    """
    Service class for handling cities.
    """
    def __init__(self, session: Session):
        self.repository: CityRepository = CityRepository(session)
        self.region_repository: RegionRepository = RegionRepository(session)

    def create(self, data: CityInput) -> CityOutput:
        if self.repository.city_exists_by_name(data.name):
            raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST, detail=f"City '{data.name}' already exists")

        if not self.region_repository.region_exists_by_id(data.region_id):
            raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST, detail=f"Region '{data.name}' already exists")

        region = self.region_repository.get_region(data.region_id)
        city = self.repository.create(data)
        return CityOutput(**city.model_dump(exclude_none=True), region=region)

    def get_all_by_region(self, region_id: UUID4) -> List[CityOutput]:
        return self.repository.get_all_by_region(region_id)

    def delete(self, _id: UUID4) -> bool:
        if not self.repository.city_exists_by_id(_id):
            raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail=f"City '{_id}' not found")
        city = self.repository.get_by_id(_id)
        return self.repository.delete(city)

    def get_all(self) -> List[CityOutput]:
        return self.repository.get_all()

    def update(self, _id: UUID4, data: CityInput):
        if not self.repository.city_exists_by_id(_id):
            raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail=f"City '{_id}' not found")
        city = self.repository.get_by_id(_id)
        updated_city = self.repository.update(city, data)
        return updated_city
