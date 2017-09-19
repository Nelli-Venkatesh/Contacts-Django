from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from simplelogin.models import contact_details

class RegistrationForm(UserCreationForm):
	#email = forms.EmailField(required=True)
	#username = forms.CharField(required=True)
	#first_name = forms.CharField(required=True)
	#last_name = forms.CharField(required=True)
	#password1 = forms.CharField(required=True)
	#password2 = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ('username','password1','password2')
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['username']
		if commit:
			user.save()
		return user

class add_contact_form(forms.ModelForm):
	contact_name = forms.CharField(required=True)
	contact_number = forms.IntegerField(required=True)
	contact_image = forms.ImageField(required=False)
	class Meta:
		model = contact_details
		fields =('contact_name','contact_number','contact_image')#should be tuple if one element is there then add ',' at the end of it 

class edit_contact_form(forms.ModelForm):

	class Meta:
		model = contact_details
		fields =('contact_name','contact_number','contact_image')#should be tuple if one element is there then add ',' at the end of it
