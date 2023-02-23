from django.db import models
from accounts.models import UserAccount
from django.contrib.auth import get_user_model
User = get_user_model()


class Projects(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Apps(models.Model):
    project = models.ForeignKey(
        Projects, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Tasks(models.Model):

    STATUS = [
        ('planned', 'Planned'),
        ('open', 'Open'),
        ('process', 'Process'),
        ('pending', 'Pending'),
        ('readyToTest', 'Ready To Test'),
        ('done', 'Done'),
    ]

    app = models.ForeignKey(
        Apps, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    pic = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=200, choices=STATUS, default='open')
    progress = models.IntegerField(default=0)
    note = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.app.project} : {self.app.name} : {self.name}"
