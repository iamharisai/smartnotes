from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home/home.html',{})

@login_required(login_url='/admin')
def authorised(request):
    return render(request,'home/authorised.html')
#if you are logged in then only you will see the authorised.html otherwise you will see login_url or 404 