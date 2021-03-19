from django.contrib import admin

from .models import helloWorld

# Register your models here.

@admin.register(helloWorld)
class helloWorldAdmin(admin.ModelAdmin):
    search_fields = ("simple_text",)