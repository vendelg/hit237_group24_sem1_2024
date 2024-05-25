from django.contrib import admin
from assignment2_app.models import Project, ThesisApplication, Student
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


    #I just used this to test stuff out: (JP)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        print("DELETE MODEL DETECTED")


admin.site.register(Accounts, AccountAdmin)

admin.site.register(ThesisApplication)

admin.site.register(Student)

admin.site.register(Project) # Step 1