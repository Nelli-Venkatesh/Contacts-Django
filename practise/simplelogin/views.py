from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from simplelogin.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from simplelogin.models import contact_details,UserProfile
from simplelogin.forms import add_contact_form
from django.contrib.auth.models import User


@login_required(login_url='/simplelogin/login_simple/')
def home_simple(request):
	object_list = contact_details.objects.filter(user=request.user)
	return render(request,"simplelogin/home.html",{'object_list': object_list})

def login_simple(request):
	return render(request, "simplelogin/login.html")

def add_contact(request):
	if request.method == 'POST':
		form = add_contact_form(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			form = add_contact_form()
			return redirect('/simplelogin/home_simple')
		return redirect('/simplelogin/home_simple')

def delete_contact(request):
	if request.method == 'POST':
		contact_id = contact_details.objects.get(pk=request.POST['id_contact'])
		contact_id.delete()
		return redirect('/simplelogin/home_simple')
	return redirect('/simplelogin/home_simple')

def edit_contact(request):
	if request.method == 'POST':
		contact_id = contact_details.objects.get(pk=request.POST['id_contact'])
		contact_id.contact_name = request.POST['contact_name']
		contact_id.contact_number = request.POST['contact_number']			
		# bypasses imageField if no image selected
		try:
			if request.FILES['contact_image']:			
				contact_id.contact_image = request.FILES['contact_image']
		except Exception as e:
			pass
		contact_id.save()
		return redirect('/simplelogin/home_simple')
	return redirect('/simplelogin/home_simple') 

@login_required(login_url='/simplelogin/login_simple/')
def edit_user_profile(request):
	if request.method == 'POST':
		# user=request.user
		# UserProfile.first_name = request.POST['first_name']
		# UserProfile.last_name = request.POST['last_name']
		# UserProfile.email = request.POST['email']
		# UserProfile.mobile_number = request.POST['mobile_number']

		#UserProfile.save()
		return redirect('/simplelogin/user_profile')
	return redirect('/simplelogin/user_profile') 



def reg_simple(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			reg_success_text = "Successfully Registered Login Here"
			return render(request, 'simplelogin/login.html', {'reg_success_text': reg_success_text})
		else:
			invalid_credentials = " you have entered invalid_credentials"
			return render(request, 'simplelogin/reg_simple.html', {'invalid_credentials': invalid_credentials})
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'simplelogin/reg_simple.html', args)



def my_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		#object_list = contact_details.objects.filter(user=request.user)
		#return render(request, "simplelogin/home.html", {'object_list': object_list})
		return redirect('/simplelogin/home_simple')
	else:
		return HttpResponse("Invalid User")

def logout_simple(request):
	logout(request)
	return render(request, 'simplelogin/login.html')

def user_profile(request):
	return render(request,'simplelogin/user_profile.html')
