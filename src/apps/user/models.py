from django.contrib.auth.models import AbstractUser
from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel


class User(LifecycleModelMixin, UUIDModel, AbstractUser):
    class Meta(AbstractUser.Meta):
        pass
