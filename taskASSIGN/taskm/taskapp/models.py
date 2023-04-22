from django.db import models
from django.conf import settings
from django.utils.timezone import now
# Create your models here.

User=settings.AUTH_USER_MODEL
class Workers(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class Managers(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    workers=models.ManyToManyField(Workers)
    def __str__(self):
        return self.user.username
    
class resolutiondocs(models.Model):
    file=models.FileField(upload_to='resdoc/')
class instructions(models.Model):
    file=models.FileField(upload_to='instructions/')
    
    
class tasks(models.Model):
    name=models.CharField(max_length=100)
    detailsres=models.TextField(null=True,blank=True)
    resolutiondocs=models.ManyToManyField(resolutiondocs,blank=True)
    description=models.TextField()
    workers=models.ManyToManyField(Workers)
    manager=models.ManyToManyField(Managers)
    date_assigned=models.DateTimeField(default=now)
    deadline=models.DateTimeField(null=True, blank=True)
    completness=models.BooleanField(default=False)
    completion_date=models.DateTimeField(blank=True,null=True)
    confirmation=models.BooleanField(null=True,blank=True)
    confirmation_date=models.DateTimeField(null=True,blank=True)
    expected_date=models.DateTimeField(blank=True,null=True)
    instructions=models.ManyToManyField(instructions,blank=True)
    

