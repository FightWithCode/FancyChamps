from django.db import models


# contest_prize_dict = {"hund_players_65_winners": {1: 60, 2: 45, 3: 35, 4: 25, 5: 25, 6: 20, 7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20, 19: 20,
#                            20: 20, 21: 20, 22: 20, 23: 20, 24: 20, 25: 20, 26: 14, 27: 14, 28: 14, 29: 14, 30: 14, 31: 14, 32: 14, 33: 14, 34: 14, 35: 14, 36: 14,
#                            37: 14, 38: 14, 39: 14, 40: 14, 41: 8, 42: 8, 43: 8, 44: 8, 45: 8, 46: 8, 47: 8, 48: 8, 49: 8, 50: 8, 51: 8, 52: 8, 53: 8, 54: 8, 55: 8,
#                            56: 8, 57: 8, 58: 8, 59: 8, 60: 8, 61: 8, 62: 8, 63: 8, 64: 8, 65: 8,
#     }
# }
class Winners1To3OutOf10Fee53(models.Model):
    Rank1To3   = models.IntegerField(default=167)


class Winners65OutOf100Fee12(models.Model):
    Rank1      = models.IntegerField(default=60)
    Rank2      = models.IntegerField(default=45)
    Rank3      = models.IntegerField(default=35)
    Rank4To5   = models.IntegerField(default=25)
    Rank6To25  = models.IntegerField(default=20)
    Rank26To40 = models.IntegerField(default=14)
    Rank41To65 = models.IntegerField(default=8)


class Winners25OutOf100Fee12(models.Model):
    Rank1      = models.IntegerField(default=200)
    Rank2      = models.IntegerField(default=100)
    Rank3      = models.IntegerField(default=75)
    Rank4To5   = models.IntegerField(default=50)
    Rank6To10  = models.IntegerField(default=35)
    Rank11To20 = models.IntegerField(default=25)
    Rank21To25 = models.IntegerField(default=20)


class Winners40OutOf100Fee12(models.Model):
    Rank1      = models.IntegerField(default=150)
    Rank2      = models.IntegerField(default=100)
    Rank3      = models.IntegerField(default=60)
    Rank4To5   = models.IntegerField(default=40)
    Rank6To10  = models.IntegerField(default=30)
    Rank11To20 = models.IntegerField(default=20)
    Rank21To40 = models.IntegerField(default=13)


class Winners25OutOf40Fee31(models.Model):
    Rank1      = models.IntegerField(default=250)
    Rank2      = models.IntegerField(default=125)
    Rank3      = models.IntegerField(default=80)
    Rank4To5   = models.IntegerField(default=50)
    Rank6To10  = models.IntegerField(default=40)
    Rank11To25 = models.IntegerField(default=23)


class Winners20OutOf35Fee49(models.Model):
    Rank1      = models.IntegerField(default=400)
    Rank2      = models.IntegerField(default=200)
    Rank3      = models.IntegerField(default=100)
    Rank4To5   = models.IntegerField(default=75)
    Rank6To10  = models.IntegerField(default=50)
    Rank11To20 = models.IntegerField(default=40)


class Winners3OutOf10Fee53(models.Model):
    Rank1      = models.IntegerField(default=250)
    Rank2      = models.IntegerField(default=150)
    Rank3      = models.IntegerField(default=100)


class Winners2OutOf5Fee23(models.Model):
    Rank1      = models.IntegerField(default=60)
    Rank2      = models.IntegerField(default=40)


class Free100To10(models.Model):
    Rank1To10      = models.IntegerField(default=10)
