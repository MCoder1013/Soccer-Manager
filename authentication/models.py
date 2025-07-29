from django.db import models
from django.contrib.auth.models import User
from players.models import Team
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # Not null

    def __str__(self):
        return f"{self.user.username} ({self.team.name})"
