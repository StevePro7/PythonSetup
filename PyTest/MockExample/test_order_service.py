import pytest
from unittest.mock import MagicMock
from order_service import OrderService
from order import Order
from customer import Customer
from payment_gateway import PaymentGateway


# Mock the external gateway
@pytest.fixture
def mock_payment_gateway():
    mock_gateway = MagicMock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = True     # Simulate successful payment
    return mock_gateway


# Test Case: Process an order successfully
def test_process_order_success(mock_payment_gateway):
    customer = Customer(customer_id=1, name="steven")
    order = Order(order_id=1001, customer=customer, amount=150)

    order_service = OrderService(payment_gateway=mock_payment_gateway)

    processed_order = order_service.process_order(order)

    assert processed_order.status == "Processed"
    mock_payment_gateway.process_payment.assert_called_once_with(150)


# Test Case: Payment fails
def test_process_order_failure(mock_payment_gateway):
    # Simulate payment failure by returning False
    mock_payment_gateway.process_payment.return_value = False

    customer = Customer(customer_id=2, name="suzanne")
    order = Order(order_id=1002, customer=customer, amount=200)

    order_service = OrderService(payment_gateway=mock_payment_gateway)

    with pytest.raises(ValueError, match="Payment failed."):
        order_service.process_order(order)

    mock_payment_gateway.process_payment.assert_called_once_with(200)
