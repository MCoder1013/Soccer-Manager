from django.template import loader
from django.http import HttpResponse
from .models import Player, Staff, Team
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from authentication.models import UserProfile

@login_required
# Create your views here.
def players(request): 
    myplayers = Player.objects.all().values()
    template = loader.get_template("all_players.html")
    context = {
        'myplayers': myplayers, 
    }

    return HttpResponse(template.render(context, request))
@login_required
def details(request, id): 
    myplayer = Player.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myplayer' : myplayer,
    }
    return HttpResponse(template.render(context, request))

def main(request): 
    template = loader.get_template('main.html')
    context = {
        'user': request.user
    }
    return HttpResponse(template.render(context, request))

@login_required
def staff(request): 
    mystaff = Staff.objects.all().values()
    template = loader.get_template("all_staff.html")
    context = {
        'mystaff': mystaff,
    }
    return HttpResponse(template.render(context, request))

@login_required
def team(request): 
    myteams = Team.objects.all().values()
    template = loader.get_template('all_teams.html')
    context = {
        'myteams' : myteams,
    }

    return HttpResponse(template.render(context, request))


@login_required
def user_dropdown(request):
    return render(request, 'components/user_dropdown.html')

def landing_page(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.userprofile
            if profile.team:
                team = profile.team
                players = team.players.all()
                staff = team.staff_members.all()
                return render(request, "team_dashboard.html", {
                    "team": team,
                    "players": players,
                    "staff": staff,
                })
        except UserProfile.DoesNotExist:
            pass  # No profile, fall through to landing page
    # For guests or users without a team, show the public landing page
    return render(request, "landing.html")

@login_required
def team_dashboard(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.players.all()
    staff = team.staff_members.all()
    return render(request, "team_dashboard.html", {
        "team": team,
        "players": players,
        "staff": staff,
    })