from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):

    username = models.CharField(
        max_length=150,
        unique=True
    )
    email = models.EmailField(max_length=1000, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    objects = UserManager()
