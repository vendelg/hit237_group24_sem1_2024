from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Project(models.Model):
  tid = models.CharField(max_length=3, primary_key=True)
  title = models.CharField(max_length=100)
  desc = models.CharField(max_length=1500)
  supName = models.CharField(max_length=30)
  
  def __str__(self):
    return self.tid + " : " + self.title
  

#AccountModel

class MyAccount_Manager(BaseUserManager):
    def create_user (self, email, username, password= None):
        if not email:
            raise ValueError("Email missing")
        if not username:
            raise ValueError("Username missing")
        if not password:
            raise ValueError("Password missing")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )   

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user (
            email = self.normalize_email(email),
            username=username,
            password=password,
        ) 
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    email= models.EmailField(verbose_name="email", max_length = 60, unique = True)
    username = models.CharField (max_length=30, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = MyAccount_Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__ (self):
        return self.username

    def has_perm (self, perm, obj = None):
        return self.is_admin

    def has_module_perms (self, app_label):
        return True