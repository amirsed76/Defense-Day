from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, email=None, password=None):
        user = self.model(
            username=username,
            # email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True )
    USERNAME_FIELD = 'username'
    objects = UserManager()
    phone_number=models.CharField(max_length=11 , null=True , blank=True)
    # state = (
    #     ('student', 'Student'),
    #     ('industry', 'Industry'),
    #     ('supervisor', 'Supervisor'),
    #     ('referee', 'Referee'),
    #     ('admin','Admin')
    #
    # )
    # job=models.CharField(max_length=11,choices=state,default="student" , null=True , blank=True)
    REQUIRED_FIELDS = []
    def __str__(self):
        return '({})'.format(self.username)

    class Meta:
        verbose_name = 'user'


class Professor(User):
    class Meta:
        verbose_name = 'Professor'


class Student(User):
    class Meta:
        verbose_name = 'Student'


class Presenter(User):
    supervisor = models.ForeignKey(Professor , related_name="SupervisorProfessor", on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Presenter'


class RoleCoefficent(models.Model):
    state = (
        ('student', 'Student'),
        ('industry', 'Industry'),
        ('supervisor', 'Supervisor'),
        ('referee', 'Referee'),

    )
    job = models.CharField(max_length=20, choices=state)
    coefficent = models.IntegerField()


class Document(models.Model):
    presenter = models.OneToOneField(Presenter , on_delete=models.CASCADE)
    file1=models.FileField(upload_to="document/",null=True , blank=True)
    file2=models.FileField(upload_to="document/",null=True , blank=True)

class Score(models.Model):
    presenter = models.OneToOneField(Presenter , on_delete=models.CASCADE ,null=True , blank=True)
    score = models.DecimalField(max_digits=4 , decimal_places=2)
