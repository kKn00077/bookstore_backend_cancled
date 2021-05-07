from django.contrib import admin
from .models import UserAccount, UserCertification

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(UserCertification)