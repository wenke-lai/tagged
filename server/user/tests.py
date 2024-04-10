from django.contrib.auth import get_user_model

import pytest
from faker import Faker
from user.models import User

faker = Faker()


def test_user_model():
    user_model = get_user_model()

    assert user_model == User, "`AUTH_USER_MODEL` should be setted in settings.py"


@pytest.mark.django_db
def test_create_superuser():
    email = faker.email()
    password = faker.password()

    user = User.objects.create_superuser(email=email, password=password)

    assert User.objects.count() == 1
    assert user.email == email
    assert user.is_superuser
    assert user.is_staff
    assert user.is_active

    assert str(user) == email.split("@", maxsplit=1)[0]


@pytest.mark.django_db
def test_create_user():
    email = faker.email()
    password = faker.password()

    user = User.objects.create_user(email=email, password=password)

    assert User.objects.count() == 1
    assert user.email == email
    assert not user.is_superuser
    assert not user.is_staff
    assert user.is_active

    assert str(user) == email.split("@", maxsplit=1)[0]
