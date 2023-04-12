from django.contrib import admin
from . import models
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display=('title','created','text')

admin.site.register(models.Notes,NotesAdmin)