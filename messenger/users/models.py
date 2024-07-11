from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user (self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        if not email:
            raise ValueError('Email must be provided') #must be unvalidated
        if not self.validateEmail(email):
            raise ValueError('Email address must have a valid format')
        
        email = self.normalize_email(email)
        user = self.model (
            username=username,
            email=email,
            **extra_fields
        )
        
        user.password = make_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')

        return self.create_user(username, email, password, **extra_fields)
    
    def validateEmail(self, email):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
        
class MyUser(AbstractUser): 
    email = models.EmailField(_("email address"), unique=True, blank=False)
    objects = UserManager()
    
    def __str__(self) -> str:
        return self.username + ': ' + self.email