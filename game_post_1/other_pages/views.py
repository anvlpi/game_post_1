from django.shortcuts import render


def about(request):
    return render(request, 'other_pages/about.html')


def contacts(request):
    return render(request, 'other_pages/contacts.html')
