from django.db import models

# Create your models here.
class Venue(models.Model):
    name =models.CharField( max_length=120)
    address = models.CharField(max_length=300)
    phone = models.IntegerField(max_length=25)
    email_address = models.EmailField(max_length=100)
    image = models.ImageField(upload_to="photos/", blank=True, null = True)

    def __str__(self):
        return self.name
class Event(models.Model):
    name =models.CharField( max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank = True, null =True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name