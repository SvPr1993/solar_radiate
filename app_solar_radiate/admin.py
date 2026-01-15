from django.contrib import admin
from app_solar_radiate.models import Data

@admin.register(Data)
class ConstAdmin(admin.ModelAdmin):
    list_display = ("date", "activity")
