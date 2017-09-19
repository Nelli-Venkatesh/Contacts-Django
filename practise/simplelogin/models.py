from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
# from django.dispatch import receiver


class contact_details(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	contact_name = models.CharField(max_length = 140)
	contact_number = models.IntegerField(default=0,validators=[MaxValueValidator(999999999999999)])
	contact_image = models.ImageField(upload_to='images/contact_images',blank=True)

	def __str__(self):
		return self.contact_name


class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length = 64,default=None)
	last_name = models.CharField(max_length = 64,default=None)
	email = models.EmailField(blank = False,default=None)
	mobile_number = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

def create_profile(sender,instance,created, **kwargs):  
    if created:  
       user_profile = UserProfile.objects.create(user=instance)  

post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class messages(models.Model):
	user = models.ForeignKey(User)
	reciever = models.ForeignKey(User,related_name='reciever')
	message_data = models.CharField(max_length = 140)

	def __str__(self):
		return self.message_data



