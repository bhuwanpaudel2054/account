from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account_module.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_join','last_login','is_admin','is_staff','is_active')
    search_fields = ('email','username')
    readonly_fields = ('id','date_join','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)