from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.TransactionDetail)
admin.site.register(models.TransactionFailedDetail)
admin.site.register(models.PreTransData)
admin.site.register(models.WidhdrawRequest)
