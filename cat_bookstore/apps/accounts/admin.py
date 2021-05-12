from django.contrib import admin
from .models import UserAccount, UserCertification


admin.site.register(UserAccount)
admin.site.register(UserCertification)