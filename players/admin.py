from django.contrib import admin
from .models import Player, Staff, Team, Match, TrainingSession, PlayerStats, Injury, Position
# Register your models here.

class PlayerAdmin(admin.ModelAdmin): 
    list_display = ("firstname", "lastname", "joined_date")
admin.site.register(Player, PlayerAdmin)

class StaffAdmin(admin.ModelAdmin): 
    list_display = ("firstname", "lastname", "occupation", "team")

admin.site.register(Staff, StaffAdmin)


class TeamAdmin(admin.ModelAdmin): 
    list_display = ("name", "city", "state", "coach")
admin.site.register(Team, TeamAdmin)



admin.site.register(Match)
admin.site.register(TrainingSession)
admin.site.register(PlayerStats)
admin.site.register(Injury)
admin.site.register(Position)