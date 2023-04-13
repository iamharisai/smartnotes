from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'


#def home(request):
#    return render(request,'home/home.html',{})


class AuthorisedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorised.html'
    login_url='/admin'


#@login_required(login_url='/admin')
#def authorised(request):
#    return render(request,'home/authorised.html')
#if you are logged in then only you will see the authorised.html otherwise you will see login_url or 404 