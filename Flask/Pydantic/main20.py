from pydantic_models02 import Employee
import pprint

incorrect_employee_data = {
    "name": "",
    "email": "cdetuma@fakedomain.com",
    "birth_date": "1998-04-02",
    "salary": -10,
    "department": "IT",
    "elected_benefits": True,
}

Employee.model_validate(incorrect_employee_data)