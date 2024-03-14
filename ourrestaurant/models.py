from django.db import models

# Create your models here.
class OurRestaurant(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to="ourrestaurant/")

#consider whether other models here to fill out restaurant history

