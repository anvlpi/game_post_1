from django.shortcuts import render
from game_window.models import GameTheme


def index(request):
    template = 'welcome_page/index.html'
    # game_themes = GameTheme.objects.all()
    game_themes = GameTheme.objects.filter(active=True)
    context = {
        'themes': game_themes
    }

    return render(request, template, context)
