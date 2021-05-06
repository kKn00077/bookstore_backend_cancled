from django.contrib import admin
from .models import File, FileGroup

# Register your models here.
admin.site.register(FileGroup)
admin.site.register(File)