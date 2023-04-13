from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


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