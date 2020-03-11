from django.contrib import admin
from .models import Utterance, Utterance1, KR_MainAction
# Register your models here.

@admin.register(Utterance)
class PostAdmin(admin.ModelAdmin):
    list_display = ['date', 'language', 'mainAction', 'utterance']
    list_display_links = ['date']
    search_fields = ['utterance']
    list_filter = ['mainAction']
    

@admin.register(Utterance1)
class PostAdmin(admin.ModelAdmin):
    list_display = ['date', 'language', 'mainAction', 'utterance']
    list_display_links = ['date']
    search_fields = ['utterance']
    list_filter = ['mainAction']
    

@admin.register(KR_MainAction)
class PostAdmin(admin.ModelAdmin):
    list_display = ['date', 'language', 'mainAction', 'count', 'rate']
    list_display_links = ['date']
    search_fields = ['mainAction']
    list_filter = ['mainAction']
    