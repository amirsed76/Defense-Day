from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'username'
    state = (
        ('student', 'Student'),
        ('presenter', 'Presenter'),
        ('industry', 'Industry'),
        ('supervisor', 'Supervisor'),
        ('referee', 'Referee'),

    )
    role = models.CharField(max_length=20 , choices=state)
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return '({})'.format(self.username)

    class Meta:
        verbose_name = 'user'