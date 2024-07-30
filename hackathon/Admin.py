from django,contrib import admin
from hackathon.models import MiUser
class MiUserAdmin(admin.ModelAdmin):
    list_display = '__all__'
    admin.site.register(MiUser, MiUserAdmin)