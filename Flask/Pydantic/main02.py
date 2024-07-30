from pydantic_models import Employee
import pprint

new_employee_dict = {
    "name": "Chris DeTuma",
    "email": "cdetuma@example.com",
    "date_of_birth": "1998-04-02",
    "salary": 123_000.00,
    "department": "IT",
    "elected_benefits": True,
}

emp: Employee = Employee.model_validate(new_employee_dict)
print(emp.name)


new_employee_json = """
	{"employee_id":"d2e7b773-926b-49df-939a-5e98cbb9c9eb",
	"name":"Eric Slogrenta",
	"email":"eslogrenta@example.com",
	"date_of_birth":"1990-01-02",
	"salary":125000.0,
	"department":"HR",
	"elected_benefits":false}
"""
new_employee = Employee.model_validate_json(new_employee_json)
print(new_employee.name)


new_emp2: dict = new_employee.model_dump()
pprint.pp(new_emp2)