from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from blog.models import post



def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)	
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f'Account created for {username}! You can now log in.')
			return redirect('login')
	else:
		form=UserRegisterForm()
	return render(request, 'users/register.html', {'form':form} )
# Create your views here.

@login_required
def profile(request):
	logged_in_posts = post.objects.all()
	return render(request, 'users/profile.html', {'posts':logged_in_posts},)