import random

# from captcha import fields, widgets
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField
# from outlay.choices import PAYMENT_TYPE_CHOICES
from `user.choices` import USER_TYPE_CHOICES
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.user_type = 'user'
        user.save()
        return user

    def _create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.user_type = 'user'
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('Имя'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=255, null=True, blank=True)
    email = models.EmailField(_('Почта'), unique=False, null=True, blank=True)
    username = models.CharField(_('username'), max_length=255, unique=True)
    phone = models.CharField(_('Телефон'), max_length=13)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    user_type = models.CharField(_('Тип пользователя'),
                                 max_length=25,
                                 choices=USER_TYPE_CHOICES,
                                 default='user')
    # date_joined = models.DateTimeField(auto_now_add=False,
    #                                    null=True,
    #                                    blank=True)
    # status = models.CharField(max_length=255,
    #                           verbose_name='Статус',
    #                           choices=STATUS_TYPE_CHOICES,
    #                           default='none')
    # birthday = models.DateField(verbose_name='День рождения',
    #                             null=True, blank=True)
    # order = models.ForeignKey('order.Order',
    #                           on_delete=models.SET_NULL,
    #                           null=True, blank=True,
    #                           verbose_name='Заказ')
    # firm = models.ForeignKey('contr_agent.Firm',
    #                          on_delete=models.CASCADE,
    #                          verbose_name='Фирма',
    #                          null=True, blank=True)
    # stack = MultiSelectField(choices=STACK_CHOICES,
    #                          max_choices=7,
    #                          max_length=7,
    #                          blank=True, null=True)
    # salary_type = models.CharField(max_length=255,
    #                                verbose_name='Тип зарплаты',
    #                                choices=PAYMENT_TYPE_CHOICES,
    #                                default='none')

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return str(self.first_name) + " " + str(self.last_name)

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
