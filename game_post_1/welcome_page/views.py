from django.shortcuts import render


def index(request):
    template = 'welcome_page/index.html'
    return render(request, template)
