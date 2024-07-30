from pydantic_models import Employee
import pprint

obj: dict= Employee.model_json_schema()
pprint.pp(obj)
