import os
import sys
from typing import Generator, Any

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import region, city
from config.database import get_db
#from routers.api import router
from utils.init_db import create_tables

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)


def test_init_db() -> None:
    region.Region.metadata.create_all(bind=engine)
    city.City.metadata.create_all(bind=engine)
