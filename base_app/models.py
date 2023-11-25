from django.db import models

# Create your models here.
class employee(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Age = models.IntegerField()  # Assuming age is an integer
    PhoneNumber = models.CharField(max_length=15)  # Assuming a reasonable length for phone number
    Address = models.TextField()
    DateOfBirth = models.DateField()
    Email = models.EmailField()