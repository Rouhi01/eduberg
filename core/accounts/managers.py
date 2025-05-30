from django.contrib.auth.models import BaseUserManager


class Usermanager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('ایمیل نمی‌تواند خالی باشد'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError(_('ابرکاربر باید دارای مقدار is_staff=True باشد.'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('ابرکاربر باید دارای مقدار is_superuser=True باشد.'))
        return self.create_user(email, password, **extra_fields)