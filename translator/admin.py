from django.contrib import admin
from .models import Dictionary

class DictionaryAdmin(admin.ModelAdmin):

    list_display = ['english', 'uzbek']

admin.site.register(Dictionary, DictionaryAdmin)
