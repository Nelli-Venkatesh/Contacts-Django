from django.contrib import admin
from .models import contact_details,UserProfile,messages

admin.site.register(contact_details)
admin.site.register(UserProfile)
admin.site.register(messages)