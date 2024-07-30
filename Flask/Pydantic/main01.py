from pydantic_models import Employee

emp1: Employee = Employee(
    name="Chris DeTuma",
    email="cdetuma@example.com",
    date_of_birth="1998-04-02",
    salary=123_000.00,
    department="IT",
    elected_benefits=True,
)
print(emp1.name)

emp2: Employee = Employee(
    employee_id="123",
    name=False,
    email="cdetumaexamplecom",
    date_of_birth="1939804-02",
    salary="high paying",
    department="PRODUCT",
    elected_benefits=300,
)
print(emp2.name)
