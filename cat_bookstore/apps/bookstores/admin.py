from django.contrib import admin
from .models import Bookstore, UserLikedBookstore, SubscribeInfo


admin.site.register(Bookstore)
admin.site.register(UserLikedBookstore)
admin.site.register(SubscribeInfo)