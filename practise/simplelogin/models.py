from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save


class contact_details(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	contact_name = models.CharField(max_length = 140)
	contact_number = models.IntegerField(default=0,validators=[MaxValueValidator(9999999999)])
	contact_image = models.ImageField(upload_to='images/contact_images',blank=True)

	def __str__(self):
		return self.contact_name


class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length = 64,default='',blank = True)
	last_name = models.CharField(max_length = 64,default='',blank = True)
	email = models.EmailField(blank = True,default='')
	mobile_number = models.IntegerField(default=0,validators=[MaxValueValidator(9999999999)])

	def __str__(self):
		return self.user.username

def create_profile(sender,instance,created, **kwargs):  
    if created:  
       user_profile = UserProfile.objects.create(user=instance)
 
post_save.connect(create_profile, sender=User)

class messages(models.Model):

	message_sender = models.ForeignKey(User,related_name ='message_sender')
	message_reciever = models.ForeignKey(User,related_name='reciever')
	message_data = models.CharField(max_length = 140)
	#message_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message_data





