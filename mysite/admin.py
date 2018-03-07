from django.contrib import admin
from .models import Clj

# Register your models here.

class CljAdmin(admin.ModelAdmin):
    list_display=('name','addres')

admin.site.register(Clj,CljAdmin)
