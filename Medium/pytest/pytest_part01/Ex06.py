class FakeSystemClock:
    def __init__(self) -> None:
        self.now = datetime.now()

    def get_now(self) -> datetime:
        return self.now


def test_credit_card_validator() -> None:
    fake_system_clock = FakeSystemClock()
    credit_card_validator = CreditCardValidator(fake_system_clock)
    # Test the validator using the fake system clock