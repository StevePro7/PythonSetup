def test_random_next_value(randomManager):
    randomManager.Initialize()

    value: int = randomManager.Next(10)
    assert value < 10

    value = randomManager.Next(5, 10)
    assert value >= 5 and value <= 10