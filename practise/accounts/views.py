from django.shortcuts import render

def login(request):
	return render(request,'accounts/base.html');

def prof(request):
	return render(request,'accounts/hello.html');
	