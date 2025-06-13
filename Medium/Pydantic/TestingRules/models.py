from pydantic import BaseModel
from typing import Optional
#from typing_extensions import NotRequired

class TestingModel(BaseModel):
    #process_id: Optional[str] = "NULL"
    Postgres: Optional[bool] = False
    Snowflake: Optional[bool] = False

testingDict = {
}


testingModel: TestingModel = TestingModel(**testingDict)
test = testingModel.Postgres
print(testingModel.Postgres)
if testingModel.Postgres:
    print("yes")
else:
    print('no')


