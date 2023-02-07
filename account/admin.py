from django.contrib import admin

from account.models import CustomUser, Spam_Contacts

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Spam_Contacts)
