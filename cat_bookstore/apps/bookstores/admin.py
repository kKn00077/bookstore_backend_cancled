from django.contrib import admin
from .models import (
    Bookstore,
    BookstoreCategory,
    Category,
    UserLikedBookstore, 
    SubscribeInfo
)


admin.site.register(Bookstore)
admin.site.register(BookstoreCategory)
admin.site.register(Category)
admin.site.register(UserLikedBookstore)
admin.site.register(SubscribeInfo)