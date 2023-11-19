from django.contrib import admin

from .models import Request, ContactInfo


admin.site.register(ContactInfo)
admin.site.register(Request)
