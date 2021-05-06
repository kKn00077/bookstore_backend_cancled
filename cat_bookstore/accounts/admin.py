from django.contrib import admin
from .models import UserAccount, UserProfile, OwnerUserProfile, UserCertification

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(UserProfile)
admin.site.register(OwnerUserProfile)
admin.site.register(UserCertification)