# from accounts.models import blogs
from django.contrib import auth
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView

# views  updated on 7/10/21

def registerPage(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully ' )
            return redirect('login')
    else:
        f = CustomUserCreationForm()
	
    return render(request, 'registerer.html', {'form': f})


def logoutn(request):
    logout(request)
    return redirect('home')
	

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		
		user = authenticate(request, username=username)
            
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username  is incorrect or does not exists')

	context = {}
	return render(request, 'logger.html', context)



def index(request):
	return render(request,'index.html')



def aboutpage(request):
    return render(request,'about.html')