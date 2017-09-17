from django.contrib import admin
from .models import contact_details,contact_messages

admin.site.register(contact_details)
admin.site.register(contact_messages)