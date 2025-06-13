from pydantic import BaseModel
from typing import Optional
import json

class RulesDataModel(BaseModel):
    process_id: Optional[str] = "NULL"
    EXECTN_ID: int
    CNCPT_ID: str
    CNCPT_VRSN_ID: Optional[str] = None
    CLNT_ID: int
    SEND_IND: str
    TNNT_ID: int
    ANLTYC_PROD_ID: int
    INV_TYPE_ID: int
    EXECTN_DT: str
    ANLTYC_ST_DESC: Optional[str] = None


file_name = "models4.json"
with open(file_name, 'r') as file:
    input_file = json.load(file)

#print(input_file)

rulesDataModel: RulesDataModel = RulesDataModel(**input_file)


print(rulesDataModel.process_id)
print(rulesDataModel.ANLTYC_ST_DESC)
