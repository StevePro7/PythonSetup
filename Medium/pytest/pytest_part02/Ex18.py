from factory import Factory, Faker


class UserFactory(Factory):
    class Meta:
        model = dict

    name = Faker('name')
    email = Faker('email')


def test_user_factory() -> None:
    user = UserFactory()
    assert 'name' in user
    assert 'email' in user