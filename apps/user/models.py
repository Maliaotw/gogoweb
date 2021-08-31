from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,AbstractUser
)


class UserProfile(AbstractUser):

    class Meta:
        verbose_name = '用戶'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username