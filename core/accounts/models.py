from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import Usermanager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Usermanager()

    def __str__(self):
        return self.email
    
# TODO creating Profile model
    
