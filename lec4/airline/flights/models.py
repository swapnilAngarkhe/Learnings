from django.db import models 

# Create your models ===are classes??=== here.


class Airport(models.Model):
    code=models.CharField(max_length=3)
    city = models.CharField(max_length=55)
    
    def __str__(self) -> str:
        return f"{self.city} ({self.code})"
    
class Flight (models.Model):
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departuers')
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duriation=models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    

class Passenger(models.Model):
    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)
    flights=models.ManyToManyField(Flight, blank=True, related_name="passengers" )
    
    def __str__(self):
        return f"{self.first} {self.last}"
        