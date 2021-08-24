from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import NullBooleanField


class MyUser(AbstractUser):
    Manager=1
    Employee=2

    ROLE_CHOICES=(
        (Manager,'Manager'),
        (Employee,'Employee')
    )

    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null=True)


class Skill(models.Model):
    ref = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    Sname=models.CharField(max_length=40)
    percentage=models.CharField(max_length=3)

    class Meta:
        db_table='skill'


class Manager(models.Model):
    ref=models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='man')

    class Meta:
        db_table='manager'
