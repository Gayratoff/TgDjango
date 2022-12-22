from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminMenu(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Menu,AdminMenu)

class AdminMaxsulot(admin.ModelAdmin):
    list_display = ['id','name','tur','money','date']
admin.site.register(Maxsulot,AdminMaxsulot)

class MessageId(admin.ModelAdmin):
    list_display = ['id','user_id','full_name']
admin.site.register(Message,MessageId)
