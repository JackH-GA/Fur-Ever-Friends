from django.db import models
# from django.urls import reverse



# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    # size = models.CharField(max_length=100)
    age = models.IntegerField()
    # gender = models.CharField(max_length=100)
    shots_recieved = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
    fixed = models.BooleanField()

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'dog_id': self.id})