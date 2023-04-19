from django.db import models

# Create your models here.

class Tasks(models.Model):
    name=models.CharField(max_length=100)
    deadline=models.DateTimeField()
    description=models.TextField()
    status=models.BooleanField(default=False)
    class Meta:
        ordering=['status','deadline']
    def __str__(self):
        return f"Task: {self.name}, due date: {self.deadline} ,status: {self.status} "
