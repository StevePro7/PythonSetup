from pydantic import BaseModel

class ImpactRulesDataModel(BaseModel):
    rule_id: str
    execution_id: str
    concept_id: str
    rule_level: str

class ImpactRulesWrapModel(BaseModel):
    client_id: str
    data: ImpactRulesDataModel


impactRulesWrapDict = {
    "data": {
        "rule_id": "1520",
        "execution_id": "1234567890",
        "concept_id": "X25-4422-55-X-45",
        "rule_level": "Global",
    },
    "client_id": "87",
}


impactRulesWrapModel: ImpactRulesWrapModel = ImpactRulesWrapModel(**impactRulesWrapDict)


print(impactRulesWrapModel.data.rule_id)
print(impactRulesWrapModel.client_id)