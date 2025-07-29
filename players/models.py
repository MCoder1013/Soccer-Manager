from django.db import models

class Team(models.Model): 
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    # Coach can be null to avoid circular reference issues
    coach = models.ForeignKey('Staff', null=True, blank=True, on_delete=models.SET_NULL, related_name='coached_teams')

    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})"

class Player(models.Model): 
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)  # fixed typo
    phone = models.CharField(max_length=20, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self): 
        return f"{self.firstname} {self.lastname}"

class Staff(models.Model): 
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=255)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='staff_members')

    def __str__(self): 
        return f"{self.firstname} {self.lastname} ({self.occupation}) - {self.team.name if self.team else 'No Team'}"
