from django.contrib import admin
from emailapp.models import *

class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')




admin.site.register(EmailLog)