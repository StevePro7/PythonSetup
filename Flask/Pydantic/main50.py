from pydantic_models05_validate_funcs import send_invoice

send_invoice(
    client_name="",
    client_email="ajolawsonfakedomain.com",
    items_purchased=["pie", "cookie", 17],
    amount_owed=0,
)

send_invoice
# pydantic_core._pydantic_core.ValidationError: 4 validation errors for
# client_name
# client_email
# items_purchased
# amount_owed
