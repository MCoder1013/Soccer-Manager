from django.db import models



# Create your models here.
class Player(models.Model): 
    firstname = models.CharField(max_length=255)
    lasname = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    joined_date = models.DateField(null = True)
    position = models.CharField(null = True, max_length=255)


    def __str__(self): 
        return f"{self.firstname} {self.lasname}"
    

class Staff(models.Model): 
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length = 255)
    phone = models.CharField(max_length=255)
    joined_date = models.DateField(max_length=255)
    occupation = models.CharField(max_length=255)
    team = models.CharField(max_length = 255)

    def __str__(self): 
        return f"{self.firstname} {self.lastname} {self.occupation} {self.team}"
    

class Team(models.Model): 
    name= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    coach = models.CharField(max_length=255)
    
