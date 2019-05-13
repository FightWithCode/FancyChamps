from django.contrib import admin
from . import models


admin.site.register(models.MatchDetail)
admin.site.register(models.CSKMITeam)
admin.site.register(models.MICSKTeam)
admin.site.register(models.SRHDCTeam)
admin.site.register(models.BANIRETeam)
admin.site.register(models.PlayerDetail)
admin.site.register(models.ContestDetail)
admin.site.register(models.JoiningDetail)
admin.site.register(models.JoiningTransactionDetail)
admin.site.register(models.ContestMessages)
