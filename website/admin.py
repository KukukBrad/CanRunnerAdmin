from django.contrib import admin
from .models import User, Property

class UserAdmin(admin.ModelAdmin):
	search_fields = ('full_name', 'email')

class PropertyAdmin(admin.ModelAdmin):
	search_fields = ('street_address', 'route')

admin.site.register(User, UserAdmin)
admin.site.register(Property, PropertyAdmin)


# Register your models here.
