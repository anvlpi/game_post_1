from django.shortcuts import render
from .models import Employee


def about(request):
    staff = Employee.objects.all()
    context = {'staff': staff}

    return render(request, 'other_pages/about.html', context)


def contacts(request):
    return render(request, 'other_pages/contacts.html')
