from django.db import models
from Medium import settings

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager




class UserInfoManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an address email")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user



class UserInfo(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def full_name(self):
        return self.username

    def short_name(self):
        return self.username  

    def __str__(self):
        return self.email
    


class Category(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    claps = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    