from django.contrib import admin
from .models import User

# Register your models here.
class TableUser(admin.ModelAdmin):
    list_display = ('name','age')
    exclude = ('cash',)
    search_fields = ('name',)

admin.site.register(User,TableUser)