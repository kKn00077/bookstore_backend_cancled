from django.contrib import admin
from .models import UserProfile, OwnerUserProfile, CategorySubscribe

admin.site.register(UserProfile)
admin.site.register(OwnerUserProfile)
admin.site.register(CategorySubscribe)