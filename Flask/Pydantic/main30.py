from pydantic_models03 import Employee
from datetime import date, timedelta

young_employee_data = {
    "name": "Jake Bar",
    "email": "jbar@example.com",
    "birth_date": date.today() - timedelta(days=365 * 17),
    "compensation": 90_000,
    "department": "SALES",
    "elected_benefits": True,
}

Employee.model_validate(young_employee_data)

# Error
# 1 validation error for Employee
# birth_date
#   Value error, Employees must be at least 18 years old.