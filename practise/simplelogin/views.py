from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from simplelogin.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from simplelogin.models import contact_details,UserProfile,messages
from simplelogin.forms import add_contact_form
from django.contrib.auth.models import User
from itertools import chain


@login_required(login_url='/simplelogin/login_simple/')
def home_simple(request):
	object_list = contact_details.objects.filter(user=request.user)
	mobile_number_list = UserProfile.objects.values('mobile_number')
	# print(mobile_number_list)
	# print(object_list)
	return render(request,"simplelogin/home.html",{'object_list': object_list, 'mobile_number_list': mobile_number_list})

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
		print(request.POST['id_userprofile'])
		try:	
			profile = UserProfile.objects.get(pk=request.POST['id_userprofile'])
			profile.first_name = request.POST['first_name']
			profile.last_name = request.POST['last_name']
			profile.email = request.POST['email']
			profile.mobile_number = request.POST['mobile_number']
			#print(request.POST['first_name'])
			profile.save()
		except:
			pass
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
		message_invalid = "Invalid username/password"
		return render(request,'simplelogin/login.html',{'message_invalid':message_invalid})

def logout_simple(request):
	logout(request)
	return render(request, 'simplelogin/login.html')

@login_required(login_url='/simplelogin/login_simple/')
def user_profile(request):
	return render(request,'simplelogin/user_profile.html')


def send_message(request):
	if request.method == 'POST':
		sender_id = User.objects.get(pk = request.POST['id_user'])
		message_data = request.POST['message_data']
		reciever_id = User.objects.get(username = request.POST['message_reciever'])

		message = messages(message_data=message_data,message_sender=sender_id,message_reciever=reciever_id)
		message.save()


		return redirect('/simplelogin/home_simple')

		# print(sender_id) #prints sender username
		# print(message_data) #prints message
		# print(reciever_id) #prints reciever username

	return redirect('/simplelogin/home_simple') 

@login_required(login_url='/simplelogin/login_simple/')
def user_messages(request):
	message_objects_list = messages.objects.filter(message_reciever = request.user ).order_by('-message_date')
	
	
	single_user_list=[]
	for message_object in message_objects_list:
		if message_object.message_sender != request.user:
			if message_object.message_sender not in single_user_list:
				single_user_list.append(message_object.message_sender)

	user_list = []
	for user in single_user_list:
		if user not in user_list:
			user_list.append(user.id)

	user_objects_list = User.objects.filter(pk__in = user_list)

	
	
	print(message_objects_list)
	print('###########################################')
	print(single_user_list)
	print('###########################################')
	print(user_list)
	print('###########################################')
	print(user_objects_list)

	return render(request,'simplelogin/user_messages.html',{'message_objects_list': message_objects_list,'user_objects_list':user_objects_list})


def send_message_by_number(request):
	if request.method == 'POST':
		sender_id = User.objects.get(pk = request.POST['id_user'])
		message_data = request.POST['message_data']
		UserProfile_id = UserProfile.objects.get(mobile_number = request.POST['message_reciever'])
		reciever_id = User.objects.get(username = UserProfile_id)

		message = messages(message_data=message_data,message_sender=sender_id,message_reciever=reciever_id)
		message.save()

		return redirect('/simplelogin/home_simple')
		# print('sender : {} '.format(sender_id)) #prints sender username
		# print('message : {} '.format(message_data))#prints message
		# print('reciever : {} '.format(reciever_id)) #prints reciever user

	return redirect('/simplelogin/home_simple')

@login_required(login_url='/simplelogin/login_simple/')
def user_message_thread(request):
	if request.method == 'POST':
	
		sender_id = User.objects.get(pk = request.POST['message_sender'])
		sender_number = sender_id.userprofile.mobile_number
		#print(sender_id)
		#print(sender_number)
		reciever_message_objects_list = messages.objects.filter(message_reciever = request.user, message_sender = sender_id).order_by('message_date')
		sender_message_objects_list = messages.objects.filter(message_reciever = sender_id, message_sender = request.user).order_by('message_date')
		
		message_objects_list = sorted(chain(reciever_message_objects_list,sender_message_objects_list),
	    key=lambda instance: instance.message_date)
		
		#print(message_objects_list)
		return render(request,'simplelogin/user_message_thread.html',{'message_objects_list':message_objects_list,
			'sender_id':sender_id,
			'sender_number':sender_number})
	else:
		return redirect('/simplelogin/user_message_thread/')
	return render(request,'simplelogin/user_message_thread.html')


@login_required(login_url='/simplelogin/login_simple/')
def send_message_by_thread(request):
	if request.method == 'POST':
				
		user_id = User.objects.get(pk = request.POST['id_user'])
		message_data = request.POST['message_data']
		UserProfile_id = UserProfile.objects.get(mobile_number = request.POST['message_reciever'])
		reciever_id = User.objects.get(username = UserProfile_id)

		message = messages(message_data=message_data,message_sender=user_id,message_reciever=reciever_id)
		message.save()
		
		#This line is for when redirecting to same page passing nessecery sending person value
		sender_id = User.objects.get(username = UserProfile_id)
		sender_number = UserProfile_id.mobile_number
		#print(sender_id)
		#print(sender_number)
		reciever_message_objects_list = messages.objects.filter(message_reciever = request.user, message_sender = sender_id).order_by('message_date')
		sender_message_objects_list = messages.objects.filter(message_reciever = sender_id, message_sender = request.user).order_by('message_date')
		
		message_objects_list = sorted(chain(reciever_message_objects_list,sender_message_objects_list),
	    key=lambda instance: instance.message_date)
		
		#print(message_objects_list)
		return render(request,'simplelogin/user_message_thread.html',{'message_objects_list':message_objects_list,
			'sender_id':sender_id,
			'sender_number':sender_number})
