from django.db import models

# Create your models here.
class job(models.Model):
 title=models.CharField(max_length=50)
 description=models.TextField(max_length=250)
 published_at=models.DateTimeField(auto_now=True)
 vacancy=models.IntegerField(default=1)
 salary=models.IntegerField(default=0)

def __str__(self):
    return self.title