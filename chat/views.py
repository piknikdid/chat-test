# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render,redirect
from .models import Chat
from  .forms import HomeForm, RegForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'


    def get(self, request):
        if request.user.is_authenticated:
            form = HomeForm()
            messages = Chat.objects.all()
            return render(request, self.template_name,{'form': form, 'messages':messages})
        else:

            return redirect('/login')

    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            pst = form.save(commit=False)
            pst.user = request.user
            pst.save()


            form = HomeForm()
            return redirect('/')

        return render(request, self.template_name,{'form': form,'text':text})

class LoginView(generic.TemplateView):
    template_name = 'chat/login.html'


    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, self.template_name, {"a":"a"})

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login')



class RegView(generic.TemplateView):
    template_name = 'chat/registration.html'
    def get(self, request):
        form = RegForm()
        return render(request, self.template_name,{'form': form})

    def post (self, request):
        form = RegForm(request.POST)


        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(request, username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('/')


        return render(request, self.template_name,{'form': form})
