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
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20 , choices=state)
    REQUIRED_FIELDS = ['role' , 'email']

    def __str__(self):
        return '({})'.format(self.username)

    class Meta:
        verbose_name = 'user'

class Presenter(models.Model):
    presenter = models.OneToOneField(User ,related_name="PresenterUSer" , on_delete=models.CASCADE )
    supervisor = models.ForeignKey(User , related_name="SupervisorOfPresenter", on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Presenter'



class RoleCoefficent(models.Model):
    state = (
        ('student', 'Student'),
        ('presenter', 'Presenter'),
        ('industry', 'Industry'),
        ('supervisor', 'Supervisor'),
        ('referee', 'Referee'),

    )
    role = models.CharField(max_length=20, choices=state)
    coefficent = models.IntegerField()
