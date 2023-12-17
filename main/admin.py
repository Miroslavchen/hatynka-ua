from django.contrib import admin
from .models import Status, Buy

class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('Name',)}

admin.site.register(Status, StatusAdmin)
admin.site.register(Buy, StatusAdmin)




