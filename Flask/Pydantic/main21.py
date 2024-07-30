from pydantic_models02 import Employee
import pprint

employee_data = {
    "name": "Clyde Harwell",
    "email": "charwell@example.com",
    "birth_date": "2000-06-12",
    "compensation": 100_000,
    "department": "ENGINEERING",
    "elected_benefits": True,
}

employee: Employee = Employee.model_validate(employee_data)
# compenation= salary
print(employee.salary)

print(employee.department)
employee.department = "HR"

# Next line will throw an error
# Field is frozen [type=frozen_field, input_value='stevepro', input_type=str]
# employee.name = "stevepro"
