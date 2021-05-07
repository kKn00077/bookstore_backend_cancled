from django.contrib import admin
from .models import UserProfile, OwnerUserProfile

admin.site.register(UserProfile)
admin.site.register(OwnerUserProfile)