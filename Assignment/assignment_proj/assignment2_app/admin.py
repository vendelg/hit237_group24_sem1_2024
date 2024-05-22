from django.contrib import admin
from assignment2_app.models import Project
from django.contrib.auth.admin import UserAdmin

from assignment2_app.models import Accounts
# Register your models here.








#CREATING THE ADMIN CLASS

class AccountAdmin(UserAdmin):
    list_display = ('email','username', 'is_admin', 'is_staff' )
    search_fields = ('email', 'username' )
    readonly_fields = ('id', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets= ()





admin.site.register(Accounts, AccountAdmin)





admin.site.register(Project) # Step 1