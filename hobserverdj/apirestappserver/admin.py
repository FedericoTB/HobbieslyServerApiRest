from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(UsersGroups)
admin.site.register(Categories)
admin.site.register(Classification)
admin.site.register(Membership)
admin.site.register(Rooms)
admin.site.register(Messages)