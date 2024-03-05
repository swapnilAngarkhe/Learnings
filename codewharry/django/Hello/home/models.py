from django.db import models

# Create your models here.
class About(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=132)
    phone=models.IntegerField()
    desc = models.TextField(default="", blank=True)
    date=models.DateField()
    
    def __str__(self):
        return self.name