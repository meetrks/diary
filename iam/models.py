from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import BasicModel


class User(AbstractUser, BasicModel):
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    country_code = models.CharField(max_length=5, verbose_name='Country Code')
    mobile_number = models.CharField(max_length=15, db_index=True, verbose_name='Mobile No.', unique=True)
    first_name = None
    last_name = None
    name = models.CharField(max_length=100, verbose_name='Name')
    is_staff = models.BooleanField(
        default=False, verbose_name='Dashboard Access Status'
    )

    def __str__(self):
        return self.name or self.email or self.mobile_number

    def save(self, *args, **kwargs):
        if self.is_staff and self.mobile_number:
            self.username = self.mobile_number
        super().save(*args, **kwargs)
