from django.db import models
from django.utils import timezone

# Create your models here.
class Taskdb(models.Model):
    name=models.CharField(max_length=30)
    opinion=models.CharField(max_length=30)
    completed=models.BooleanField(default=False)
    time_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s"%(self.name,self.completed)
