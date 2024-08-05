from typing import List, Optional
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from repository.region_repository import RegionRepository
from schemas.region_schema import RegionInput, RegionOutput
import http


class RegionService:
    def __init__(self, session: Session):
        self.repository: RegionRepository = RegionRepository(session)

    def create(self, data: RegionInput) -> RegionOutput:
        if self.repository.region_exists_by_name(data.name):
            raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST, detail=f"Region '{data.name}' already exists")
        return self.repository.create(data)

    def get_all(self) -> List[Optional[RegionOutput]]:
        return self.repository.get_all()

    def delete(self, _id: UUID4) -> bool:
        if not self.repository.region_exists_by_id(_id):
            raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail=f"Region '{_id}' not found")
        region = self.repository.get_by_id(_id)
        return self.repository.delete(region)

    def update(self, _id: UUID4, data: RegionInput) -> RegionInput:
        if not self.repository.region_exists_by_id(_id):
            raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail=f"Region '{_id}' not found")
        region = self.repository.get_by_id(_id)
        return self.repository.update(region, data)
