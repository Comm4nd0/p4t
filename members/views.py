from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from contact.models import ContactDetail

def register(request):
    contact_details = ContactDetail.objects.first()
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': 'Username has already been taken.',
                                                         'contact_detail': contact_details,})
            except User.DoesNotExist:
                User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], is_active=False)
                return render(request, 'post_register.html', {'contact_detail': contact_details,})
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.',
                                                     'contact_detail': contact_details,})
    else:
        return render(request, 'register.html', {'contact_detail': contact_details,})


def login(request):
    contact_details = ContactDetail.objects.first()
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or Password does not exist.',
                                                  'contact_detail': contact_details,})
    else:
        return render(request, 'login.html', {'contact_detail': contact_details,})


def logout(request):
    # TO DO neet to go to homepage and logout
    # if request.method == 'POST':
    auth.logout(request)
    return redirect('home')