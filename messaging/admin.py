from django.contrib import admin
from django.contrib.admin import register

from messaging.models import Email


# Register your models here.
@register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'sender', 'recipient', 'attach',
                  'sent_at')