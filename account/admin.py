from django.contrib import admin
from account.models import *


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
