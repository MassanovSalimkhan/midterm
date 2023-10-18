from django.db import models 
class contacts(models.Model) :
    First_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)

    def __str__(self): 
        return f"{self.First_name} {self.last_name}"