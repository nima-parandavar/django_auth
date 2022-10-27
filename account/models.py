from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


# create your manager here

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("email must be set")
        user_email = self.normalize_email(email)
        user = self.model(email=user_email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email=email, password=password, **extra_fields)


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    is_active = models.BooleanField(default=True, verbose_name='Active status')
    is_staff = models.BooleanField(default=False, verbose_name='Staff status')

    # optional fields
    photo = models.ImageField(upload_to='users/photos/%Y/%M/%d', blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=11)

    objects = CustomUserManager()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
