from django.contrib import admin
from . import models
from django.apps import apps
# Register your models here.

app = apps.get_app_config('cricket_matches')

for model_name, model in app.models.items():
    admin.site.register(model)

# admin.site.register(models.Winners65OutOf100Fee12)
# admin.site.register(models.Winners25OutOf100Fee12)
# admin.site.register(models.Winners40OutOf100Fee12)
# admin.site.register(models.Winners25OutOf40Fee31)
# admin.site.register(models.Winners20OutOf35Fee49)
# admin.site.register(models.Winners3OutOf10Fee53)
# admin.site.register(models.Winners1To3OutOf10Fee53)
# admin.site.register(models.Winners2OutOf5Fee23)
# admin.site.register(models.Free100To10)