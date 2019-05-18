from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
#from models import *

def home_page(request):
	#return HttpResponse("Hello World")
	return render(request, "home_page.html", {})


def login_page(request):
	#return HttpResponse("Hello World")
	return render(request, "login_page.html", {})

def custom_404(request):
    return render(request, 'auth/404.html', {})

"""def results(request):
	m = Movie()
	if request.GET.get('q') is not None:
		searchname = request.GET.get('q')
		movieData = m.getMovieData(searchname)
		return render(request, 'home_page.html', {'movieData': movieData, 'search': True})
	else:
		return render(request, 'home_page.html')
	#print (searchname)"""


"""def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
	    "form": form
	}
	print("user logged in")
	#print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
			#print(request.user.is_authenticated())
			login(request, user)
			return redirect("/login")
            #Redirect to success
            #context['form'] = LoginForm()
        else:
            #invalid login
        	print("Error")

	return render(request,"auth/login.html", context)"""

"""def register_page(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)

	return render(request,"auth/register.html", {})"""


