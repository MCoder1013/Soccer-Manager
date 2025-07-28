from django.template import loader
from django.http import HttpResponse
from .models import Player, Staff, Team
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
