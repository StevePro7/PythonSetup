from pydantic_models05_validate_funcs import send_invoice

email_str: str = send_invoice(
    client_name="Andrew Johnson",
    client_email="ajolawson@fakedomain.com",
    items_purchased=["pie", "cookie", 17],
    amount_owed=20,
)

print(email_str)