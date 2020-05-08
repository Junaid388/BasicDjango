from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def about(request):
	#my_page = "Hello, This is my home page"
	return render(request, 'about.html', {"my_page": stuff})

def contact(request):
	return render(request, 'contact.html', {})

def stuff():
	return "This is the return message"