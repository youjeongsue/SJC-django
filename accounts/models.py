from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, username, email, password, is_staff):
        
        if not email :
            raise ValueError('must have user email')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            is_staff = is_staff
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    objects = UserManager()