from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.utils.html import format_html

class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        # Set is_staff, is_superuser, and is_active to True as default
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_teacher', True)

        return self.create_user(email=email, password=password, **other_fields)

    def create_user(self, email=None, is_teacher=None, password=None, **other_fields):
        # Set the values to the variables for creating a user account
        email = self.normalize_email(email)
        user = self.model(is_teacher=is_teacher, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='ایمیل',
        max_length=255,
        unique=True,
    )
    fullname = models.CharField(max_length=270, verbose_name='نام کامل')
    image = models.ImageField(upload_to='User', blank=True, null=True, verbose_name='عکس')
    is_teacher = models.BooleanField(default=False, blank=True, null=True, verbose_name='ایا معلم است؟')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def user_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="50px" width="60px">')
        return format_html('<h3 style="color: red">تصویر موجود نیست</h3>')

    user_image.short_description = "عکس بند انگشتی"

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
