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
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile_imgs/', blank=True, null=True, default='')
    background_img = models.ImageField(upload_to='background_imgs/', blank=True, null=True, default='')
    bio = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
