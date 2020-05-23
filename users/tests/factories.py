import factory
from factory.django import DjangoModelFactory

from rest_framework_simplejwt.state import User


class StaffUserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username", "email", "is_staff", "password")

    username = "linnify"
    email = "linnify@email.com"
    password = "linnify123"
    is_staff = True


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username", "email", "password")

    username = factory.Sequence(lambda n: f"linnify{n}")
    email = factory.Sequence(lambda n: f"linnify{n}@com.")
    password = "linnify123"