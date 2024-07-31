from pydantic_models04 import Employee

new_employee = {
    "name": "Alexis Tau",
    "email": "ataue@example.com",
    "birth_date": "2001-04-012",
    "compensation": 100_000,
    "department": "IT",
    "elected_benefits": True,
}

Employee.model_validate(new_employee)

# Error
#   Value error, IT employees are contractors and don't qualify for benefits