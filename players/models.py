from django.db import models

class Team(models.Model): 
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    league = models.CharField(max_length=255, null =True , blank=True) # League can be null or blank
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

class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    score_home = models.IntegerField(null=True, blank=True)
    score_away = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date.strftime('%Y-%m-%d')}"

class TrainingSession(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateTimeField()
    focus = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.team.name} training on {self.date.strftime('%Y-%m-%d')}"

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player} stats for {self.match}"

class Injury(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date_reported = models.DateField()
    recovery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.player} injury: {self.description}"

class Position(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
