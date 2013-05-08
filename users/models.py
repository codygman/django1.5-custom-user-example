from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, email, twitter_handle, password=None):
        """
        Creates and saves user with the given email, twitter handle,
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            twitter_handle=twitter_handle,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, twitter_handle, password):
        """
        Creates and saves a superuser with the given email, twitter handle,
        and password.
        """
        user = self.create_user(email,
            password=password,
            twitter_handle=twitter_handle,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    twitter_handle = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['twitter_handle']

    def get_full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.email

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.email

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin
