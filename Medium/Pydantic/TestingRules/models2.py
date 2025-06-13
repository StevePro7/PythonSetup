from pydantic import BaseModel
from typing import Optional

class TestingDataModel(BaseModel):
    Postgres: Optional[bool] = False
    Snowflake: Optional[bool] = False
    RabbitMQ: Optional[bool] = False
    GCPbucketList: Optional[bool] = False
    GCPbucketRead: Optional[bool] = False
    GCPbucketFile: Optional[str] = None
    LoggerTest: Optional[str] = None

class TestingWrapModel(BaseModel):
    process_id: Optional[str] = "NULL"
    testing: Optional[TestingDataModel] = {}


testingWrapDict = {
    "process_id": "adriana",
    "testing": {
        "Postgres": False,
        "Snowflake": False,
        "RabbitMQ": False,
        "GCPbucketList": True,
        "GCPbucketRead": False,
        "LoggerTest": "Quick brown fox",
    }
}


testingWrapModel: TestingWrapModel = TestingWrapModel(**testingWrapDict)


print(testingWrapModel.testing.GCPbucketList)
print(testingWrapModel.testing.LoggerTest)