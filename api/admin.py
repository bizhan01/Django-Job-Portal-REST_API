from django.contrib import admin
from .models import * 
from accounts.models import * 

# Register your models here.
admin.site.register(application)
admin.site.register(candidate)
admin.site.register(UserProfile)
# admin.site.register(HrUserProfile)
