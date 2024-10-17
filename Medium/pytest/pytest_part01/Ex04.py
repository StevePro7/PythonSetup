from unittest.mock import Mock


def test_transaction_validator() -> None:
    mock_payment_gateway = Mock()
    transaction_validator = TransactionValidator(mock_payment_gateway)
    transaction_validator.validate_transaction()
    mock_payment_gateway.charge.assert_called_once()