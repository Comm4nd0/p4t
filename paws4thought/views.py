from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'home.html')

def about(requests):
    return render(requests, 'about.html')

def team(requests):
    return render(requests, 'team.html')