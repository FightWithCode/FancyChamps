from django.db import models
from .generators import MatchSlugGenerator, ContestSlugGenerator
from decimal import Decimal


class MatchDetail(models.Model):
    match_name = models.CharField(max_length=100)
    tournament_name = models.CharField(max_length=50)
    match_date = models.DateTimeField()
    match_tick = models.IntegerField(blank=True)
    match_slug = models.CharField(max_length=64, unique=True, default="Test")
    team_one = models.CharField(max_length=25)
    team_two = models.CharField(max_length=25)
    team_one_image = models.CharField(max_length=25)
    team_two_image = models.CharField(max_length=25)
    history_activate = models.BooleanField(default=False)
    live = models.BooleanField(default=False)
    short_team_one = models.CharField(default='IND', max_length=5)
    short_team_two = models.CharField(default='AUS', max_length=5)
    initial_contest_created = models.BooleanField(default=False)
    match_status = models.CharField(default="0/0 (0 Overs)", max_length=255)
    cancelled_called = models.BooleanField(default=False)
    refund_called = models.BooleanField(default=False)
    added_called = models.BooleanField(default=False)
    update_wins_called = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        print(self.match_date)
        print(self.match_date.timestamp())
        self.match_tick = self.match_date.timestamp()
        if self.match_slug == "Test" or "":
            self.match_slug = MatchSlugGenerator(self.match_name, self.team_one, self.team_two, self.match_date)
        super(MatchDetail, self).save(*args, **kwargs)
        if(self.initial_contest_created == False):
            # contest_obj_1 = ContestDetail(
            #                     contest_of_match=self,
            #                     contest_name="₹1000 Winnnings",
            #                     contest_slug="Test",
            #                     contest_prize=1000,
            #                     contest_fee = 13,
            #                     contest_size = 100,
            #                     contest_winners = 40,
            #                     total_player_joined = 0,
            #                     joined_percentage = 0,
            #                     contest_category = "Great and Grand Winning",
            #                     multiple_entry = True,
            #                     filled_status = False,
            #                     bonus_contest = True,
            #                     free_contest = False,
            #                     confirmed = False,
            #                     prize_dist_type = "Winners40OutOf100Fee12",
            #                     bonus_percent = 30
            #                 )
            # contest_obj_1.save()
            # contest_obj_2 = ContestDetail(
            #                     contest_of_match=self,
            #                     contest_name="₹1500 Winnnings",
            #                     contest_slug="Test",
            #                     contest_prize=1500,
            #                     contest_fee = 49,
            #                     contest_size = 40,
            #                     contest_winners = 20,
            #                     total_player_joined = 0,
            #                     joined_percentage = 0,
            #                     contest_category = "Great and Grand Winning",
            #                     multiple_entry = True,
            #                     filled_status = False,
            #                     bonus_contest = True,
            #                     free_contest = False,
            #                     confirmed = False,
            #                     prize_dist_type = "Winners20OutOf35Fee49",
            #                     bonus_percent = 10
            #                 )
            # contest_obj_2.save()
            contest_obj_3 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹100 Winnnings",
                                contest_slug="Test",
                                contest_prize=100,
                                contest_fee = 29,
                                contest_size = 4,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "4 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0
                            )
            contest_obj_3.save()
            contest_obj_4 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹50 Winnnings",
                                contest_slug="Test",
                                contest_prize=50,
                                contest_fee = 29,
                                contest_size = 2,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Head to Head",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = False,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0
                            )
            contest_obj_4.save()
            contest_obj_5 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹400 Winnnings",
                                contest_slug="Test",
                                contest_prize=400,
                                contest_fee = 111,
                                contest_size = 4,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "4 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0
                            )
            contest_obj_5.save()
            contest_obj_6 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹100 Winnnings",
                                contest_slug="Test",
                                contest_prize=100,
                                contest_fee = 57,
                                contest_size = 2,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Head to Head",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = False,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0
                            )
            contest_obj_6.save()
            contest_obj_7 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹500 Winnnings",
                                contest_slug="Test",
                                contest_prize=500,
                                contest_fee = 55,
                                contest_size = 10,
                                contest_winners = 3,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Great and Grand Winning",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "Winners3OutOf10Fee53",
                                bonus_percent = 0
                            )
            contest_obj_7.save()
            contest_obj_8 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹300 Winnnings",
                                contest_slug="Test",
                                contest_prize=300,
                                contest_fee = 111,
                                contest_size = 3,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "3 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0
                            )
            contest_obj_8.save()
            contest_obj_9 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹100 Winnnings",
                                contest_slug="Test",
                                contest_prize=100,
                                contest_fee = 0,
                                contest_size = 1000,
                                contest_winners = 10,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Free Roll",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = True,
                                confirmed = True,
                                prize_dist_type = "Free100To10",
                                bonus_percent = 0
                            )
            contest_obj_9.save()
            contest_obj_10 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹300 Winnnings",
                                contest_slug="Test",
                                contest_prize=300,
                                contest_fee = 57,
                                contest_size = 6,
                                contest_winners = 2,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Other",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "Winners2OutOf6Fee56",
                                bonus_percent = 0
                            )
            contest_obj_10.save()
            contest_obj_11 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹100 Winnnings",
                                contest_slug="Test",
                                contest_prize=100,
                                contest_fee = 56,
                                contest_size = 5,
                                contest_winners = 2,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Other",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "Winners2OutOf5Fee23",
                                bonus_percent = 0
                            )
            contest_obj_11.save()
            contest_obj_12 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹100 Winnnings",
                                contest_slug="Test",
                                contest_prize=100,
                                contest_fee = 24,
                                contest_size = 5,
                                contest_winners = 2,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Other",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "Winners2OutOf5Fee23",
                                bonus_percent = 0
                            )
            contest_obj_12.save()
            contest_obj_13 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹50 Winnnings",
                                contest_slug="Test",
                                contest_prize=50,
                                contest_fee = 13,
                                contest_size = 5,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "All Goes to Champion",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0
                            )
            contest_obj_13.save()
            contest_obj_14 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹50 Winnnings",
                                contest_slug="Test",
                                contest_prize=25,
                                contest_fee = 7,
                                contest_size = 5,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "All Goes to Champion",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = True,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 20,
                            )
            contest_obj_14.save()
            contest_obj_15 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹50 Winnnings",
                                contest_slug="Test",
                                contest_prize=50,
                                contest_fee = 6,
                                contest_size = 10,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "All Goes to Champion",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = True,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 20,
                            )
            contest_obj_15.save()
            # contest_obj_16 = ContestDetail(
            #                     contest_of_match=self,
            #                     contest_name="₹50 Winnnings",
            #                     contest_slug="Test",
            #                     contest_prize=50,
            #                     contest_fee = 1,
            #                     contest_size = 59,
            #                     contest_winners = 1,
            #                     total_player_joined = 0,
            #                     joined_percentage = 0,
            #                     contest_category = "All Goes to Champion",
            #                     multiple_entry = False,
            #                     filled_status = False,
            #                     bonus_contest = False,
            #                     free_contest = False,
            #                     confirmed = True,
            #                     prize_dist_type = "ToOne",
            #                     bonus_percent = 0,
            #                 )
            # contest_obj_16.save()
            # contest_obj_17 = ContestDetail(
            #                     contest_of_match=self,
            #                     contest_name="₹100 Winnnings",
            #                     contest_slug="Test",
            #                     contest_prize=100,
            #                     contest_fee = 2,
            #                     contest_size = 55,
            #                     contest_winners = 1,
            #                     total_player_joined = 0,
            #                     joined_percentage = 0,
            #                     contest_category = "All Goes to Champion",
            #                     multiple_entry = False,
            #                     filled_status = False,
            #                     bonus_contest = False,
            #                     free_contest = False,
            #                     confirmed = True,
            #                     prize_dist_type = "ToOne",
            #                     bonus_percent = 0,
            #                 )
            # contest_obj_17.save()
            contest_obj_18 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹50 Winnnings",
                                contest_slug="Test",
                                contest_prize=50,
                                contest_fee = 13,
                                contest_size = 5,
                                contest_winners = 2,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Equality is Priority",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "Winners2OutOf5Fee11Equal",
                                bonus_percent = 0,
                            )
            contest_obj_18.save()
            contest_obj_19 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹100 Winnnings",
                                contest_slug="Test",
                                contest_prize=100,
                                contest_fee = 23,
                                contest_size = 5,
                                contest_winners = 2,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Equality is Priority",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "Winners2OutOf5Fee21Equal",
                                bonus_percent = 0,
                            )
            contest_obj_19.save()
            contest_obj_20 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹200 Winnnings",
                                contest_slug="Test",
                                contest_prize=200,
                                contest_fee = 56,
                                contest_size = 4,
                                contest_winners = 2,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Equality is Priority",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "Winners2OutOf4Fee55Equal",
                                bonus_percent = 0,
                            )
            contest_obj_20.save()
            contest_obj_21 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹25 Winnnings",
                                contest_slug="Test",
                                contest_prize=25,
                                contest_fee = 14,
                                contest_size = 2,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Head to Head",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = False,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_21.save()
            contest_obj_22 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹30 Winnnings",
                                contest_slug="Test",
                                contest_prize=30,
                                contest_fee = 12,
                                contest_size = 3,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "3 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_22.save()
            contest_obj_23 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹20 Winnnings",
                                contest_slug="Test",
                                contest_prize=20,
                                contest_fee = 12,
                                contest_size = 2,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Head to Head",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = False,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_23.save()
            contest_obj_24 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹20 Winnnings",
                                contest_slug="Test",
                                contest_prize=20,
                                contest_fee = 8,
                                contest_size = 3,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "3 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_24.save()
            contest_obj_25 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹25 Winnnings",
                                contest_slug="Test",
                                contest_prize=25,
                                contest_fee = 8,
                                contest_size = 4,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "4 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_25.save()
            contest_obj_26 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹15 Winnnings",
                                contest_slug="Test",
                                contest_prize=15,
                                contest_fee = 6,
                                contest_size = 3,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "3 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_26.save()
            contest_obj_27 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹40 Winnnings",
                                contest_slug="Test",
                                contest_prize=40,
                                contest_fee = 12,
                                contest_size = 4,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "4 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_27.save()
            contest_obj_28 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹35 Winnnings",
                                contest_slug="Test",
                                contest_prize=35,
                                contest_fee = 20,
                                contest_size = 2,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Head to Head",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = False,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_28.save()
            contest_obj_29 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹80 Winnnings",
                                contest_slug="Test",
                                contest_prize=80,
                                contest_fee = 45,
                                contest_size = 2,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Head to Head",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = False,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_29.save()
            contest_obj_30 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹200 Winnnings",
                                contest_slug="Test",
                                contest_prize=200,
                                contest_fee = 111,
                                contest_size = 2,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "Head to Head",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = False,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_30.save()
            contest_obj_31 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹200 Winnnings",
                                contest_slug="Test",
                                contest_prize=200,
                                contest_fee = 75,
                                contest_size = 3,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "3 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_31.save()
            contest_obj_32 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹45 Winnnings",
                                contest_slug="Test",
                                contest_prize=45,
                                contest_fee = 17,
                                contest_size = 3,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "3 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_32.save()
            contest_obj_33 = ContestDetail(
                                contest_of_match=self,
                                contest_name="₹75 Winnnings",
                                contest_slug="Test",
                                contest_prize=75,
                                contest_fee = 29,
                                contest_size = 3,
                                contest_winners = 1,
                                total_player_joined = 0,
                                joined_percentage = 0,
                                contest_category = "3 On 1",
                                multiple_entry = False,
                                filled_status = False,
                                bonus_contest = False,
                                free_contest = False,
                                confirmed = True,
                                prize_dist_type = "ToOne",
                                bonus_percent = 0,
                            )
            contest_obj_33.save()
    def __str__(self):
        return self.match_name


class ContestMessages(models.Model):
    contest_slug = models.CharField(max_length=512)
    message = models.CharField(max_length=512)
    user = models.CharField(max_length=64)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user+":"+self.contest_slug+str(self.time)


class PlayerDetail(models.Model):
    player_name = models.CharField(max_length=255, default="")
    player_current_team = models.CharField(max_length=25, default="")
    player_type = models.CharField(max_length=25, default="Keeper/Batsman/Allrounder/Bowler")
    total_points = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    player_credit_points = models.DecimalField(max_digits=3, decimal_places=1, default=7.5)
    current_points = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.player_name


class ContestDetail(models.Model):
    contest_of_match = models.ForeignKey(MatchDetail, on_delete=models.CASCADE)
    contest_name = models.CharField(max_length=100)
    contest_slug = models.CharField(max_length=64, unique=True, default="Test")
    contest_prize = models.IntegerField()
    contest_fee = models.IntegerField()
    contest_size = models.IntegerField()
    contest_winners = models.IntegerField(default=1)
    total_player_joined = models.IntegerField()
    joined_percentage = models.IntegerField(default=0)
    contest_category = models.CharField(max_length=100)
    multiple_entry = models.BooleanField(default=False)
    multiple_entry_text = models.CharField(max_length=5,default="",blank=True)
    filled_status = models.BooleanField(default=False)
    bonus_contest = models.BooleanField(default=False)
    bonus_contest_text = models.CharField(max_length=5,default="", blank=True)
    free_contest = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    confirmed_text = models.CharField(max_length=5,default="", blank=True)
    prize_dist_type = models.CharField(max_length=100)
    bonus_percent = models.IntegerField(default = 0)
    cancelled = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        joined = JoiningDetail.objects.filter(joined_contest_slug__exact=self.contest_slug)
        self.total_player_joined = joined.count()
        self.joined_percentage = (self.total_player_joined * 100) / self.contest_size
        if self.contest_slug == "Test" or "":
            self.contest_slug = ContestSlugGenerator(self.contest_name, self.contest_category, self.contest_prize, self.contest_fee)
        if self.contest_size == self.total_player_joined:
            self.filled_status = True
        if self.multiple_entry == True:
            self.multiple_entry_text = "M"
        if self.bonus_contest == True:
            self.bonus_contest_text = "B"
        if self.confirmed == True:
            self.confirmed_text = "C"
        super(ContestDetail, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.contest_of_match) + '|' + self.contest_name + '|' + self.contest_slug + '|' + self.prize_dist_type



class JoiningDetail(models.Model):
    joined_user = models.CharField(max_length=255)
    joined_contest_slug = models.CharField(max_length=255)
    joined_user_team = models.CharField(max_length=255)
    match_slug = models.CharField(max_length=255, default="")
    total_team_points = models.FloatField(default=0.0)
    winnings = models.FloatField(default=0.0)
    rank = models.PositiveIntegerField(default=1)
    bonus_deduction = models.PositiveIntegerField(default=0)
    balance_deduction = models.PositiveIntegerField(default=0)
    winnings_deduction = models.PositiveIntegerField(default=0)
    last_rank = models.PositiveIntegerField(default=0)
    refunded = models.BooleanField(default=False)
    added_to_wallet = models.BooleanField(default=False)

    def __str__(self):
        return self.joined_contest_slug + "[" + self.joined_user + self.joined_user_team + "]"


class JoiningTransactionDetail(models.Model):
    transaction_id = models.CharField(max_length=255)
    transaction_amt = models.IntegerField(default=0)
    transact_user = models.CharField(max_length=64)
    transaction_time = models.DateTimeField(auto_now=True)
    transaction_message = models.CharField(max_length=255, default="")
    transaction_type = models.CharField(max_length=16,default="added")
    refund_for_contest = models.CharField(max_length=255, default="")
    transaction_for_contest = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.transaction_id + ' | ' + self.transact_user + ' | ' + str(self.transaction_amt) + ' | ' + self.transaction_for_contest


class WIINDTeam(models.Model):
    Keeper = models.CharField(max_length=255, default="")
    Player2 = models.CharField(max_length=255, default="")
    Player3 = models.CharField(max_length=255, default="")
    Player4 = models.CharField(max_length=255, default="")
    Player5 = models.CharField(max_length=255, default="")
    Player6 = models.CharField(max_length=255, default="")
    Player7 = models.CharField(max_length=255, default="")
    Player8 = models.CharField(max_length=255, default="")
    Player9 = models.CharField(max_length=255, default="")
    Player10 = models.CharField(max_length=255, default="")
    Player11 = models.CharField(max_length=255, default="")
    Captain = models.CharField(max_length=255, default=" ")
    Vice_Captain = models.CharField(max_length=255, default=" ")

    Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    total_batsmen = models.IntegerField(default=4)
    total_allrounders = models.IntegerField(default=3)
    total_bowlers = models.IntegerField(default=3)
    team_no = models.IntegerField(default=1)
    username_of_player = models.CharField(max_length=64)
    # total_credits_used = models.IntegerField(default=100)
    total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    match_slug = models.CharField(max_length=100)
    full_team_name = models.CharField(max_length=255, default="Something")

    def save(self, *args, **kwargs):
        self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
        super(WIINDTeam, self).save(*args, **kwargs)

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def update_total_team_points(self, user, team_no, match_slug):
        self.total_team_points = 100
        self.save()


class NEDUAETeam(models.Model):
    Keeper = models.CharField(max_length=255, default="")
    Player2 = models.CharField(max_length=255, default="")
    Player3 = models.CharField(max_length=255, default="")
    Player4 = models.CharField(max_length=255, default="")
    Player5 = models.CharField(max_length=255, default="")
    Player6 = models.CharField(max_length=255, default="")
    Player7 = models.CharField(max_length=255, default="")
    Player8 = models.CharField(max_length=255, default="")
    Player9 = models.CharField(max_length=255, default="")
    Player10 = models.CharField(max_length=255, default="")
    Player11 = models.CharField(max_length=255, default="")
    Captain = models.CharField(max_length=255, default=" ")
    Vice_Captain = models.CharField(max_length=255, default=" ")

    Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    total_batsmen = models.IntegerField(default=4)
    total_allrounders = models.IntegerField(default=3)
    total_bowlers = models.IntegerField(default=3)
    team_no = models.IntegerField(default=1)
    username_of_player = models.CharField(max_length=64)
    # total_credits_used = models.IntegerField(default=100)
    total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    match_slug = models.CharField(max_length=100)
    full_team_name = models.CharField(max_length=255, default="Something")

    def save(self, *args, **kwargs):
        self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
        super(NEDUAETeam, self).save(*args, **kwargs)

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def update_total_team_points(self, user, team_no, match_slug):
        self.total_team_points = 100
        self.save()


class WSLLTeam(models.Model):
    Keeper = models.CharField(max_length=255, default="")
    Player2 = models.CharField(max_length=255, default="")
    Player3 = models.CharField(max_length=255, default="")
    Player4 = models.CharField(max_length=255, default="")
    Player5 = models.CharField(max_length=255, default="")
    Player6 = models.CharField(max_length=255, default="")
    Player7 = models.CharField(max_length=255, default="")
    Player8 = models.CharField(max_length=255, default="")
    Player9 = models.CharField(max_length=255, default="")
    Player10 = models.CharField(max_length=255, default="")
    Player11 = models.CharField(max_length=255, default="")
    Captain = models.CharField(max_length=255, default=" ")
    Vice_Captain = models.CharField(max_length=255, default=" ")

    Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    total_batsmen = models.IntegerField(default=4)
    total_allrounders = models.IntegerField(default=3)
    total_bowlers = models.IntegerField(default=3)
    team_no = models.IntegerField(default=1)
    username_of_player = models.CharField(max_length=64)
    # total_credits_used = models.IntegerField(default=100)
    total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    match_slug = models.CharField(max_length=100)
    full_team_name = models.CharField(max_length=255, default="Something")

    def save(self, *args, **kwargs):
        self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
        super(WSLLTeam, self).save(*args, **kwargs)

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def update_total_team_points(self, user, team_no, match_slug):
        self.total_team_points = 100
        self.save()


class WSLTTeam(models.Model):
    Keeper = models.CharField(max_length=255, default="")
    Player2 = models.CharField(max_length=255, default="")
    Player3 = models.CharField(max_length=255, default="")
    Player4 = models.CharField(max_length=255, default="")
    Player5 = models.CharField(max_length=255, default="")
    Player6 = models.CharField(max_length=255, default="")
    Player7 = models.CharField(max_length=255, default="")
    Player8 = models.CharField(max_length=255, default="")
    Player9 = models.CharField(max_length=255, default="")
    Player10 = models.CharField(max_length=255, default="")
    Player11 = models.CharField(max_length=255, default="")
    Captain = models.CharField(max_length=255, default=" ")
    Vice_Captain = models.CharField(max_length=255, default=" ")

    Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    total_batsmen = models.IntegerField(default=4)
    total_allrounders = models.IntegerField(default=3)
    total_bowlers = models.IntegerField(default=3)
    team_no = models.IntegerField(default=1)
    username_of_player = models.CharField(max_length=64)
    # total_credits_used = models.IntegerField(default=100)
    total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    match_slug = models.CharField(max_length=100)
    full_team_name = models.CharField(max_length=255, default="Something")

    def save(self, *args, **kwargs):
        self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
        super(WSLTTeam, self).save(*args, **kwargs)

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def update_total_team_points(self, user, team_no, match_slug):
        self.total_team_points = 100
        self.save()


class INDAUSTeam(models.Model):
    Keeper = models.CharField(max_length=255, default="")
    Player2 = models.CharField(max_length=255, default="")
    Player3 = models.CharField(max_length=255, default="")
    Player4 = models.CharField(max_length=255, default="")
    Player5 = models.CharField(max_length=255, default="")
    Player6 = models.CharField(max_length=255, default="")
    Player7 = models.CharField(max_length=255, default="")
    Player8 = models.CharField(max_length=255, default="")
    Player9 = models.CharField(max_length=255, default="")
    Player10 = models.CharField(max_length=255, default="")
    Player11 = models.CharField(max_length=255, default="")
    Captain = models.CharField(max_length=255, default=" ")
    Vice_Captain = models.CharField(max_length=255, default=" ")

    Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    total_batsmen = models.IntegerField(default=4)
    total_allrounders = models.IntegerField(default=3)
    total_bowlers = models.IntegerField(default=3)
    team_no = models.IntegerField(default=1)
    username_of_player = models.CharField(max_length=64)
    # total_credits_used = models.IntegerField(default=100)
    total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    match_slug = models.CharField(max_length=100)
    full_team_name = models.CharField(max_length=255, default="Something")

    def save(self, *args, **kwargs):
        self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
        super(INDAUSTeam, self).save(*args, **kwargs)

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def update_total_team_points(self, user, team_no, match_slug):
        self.total_team_points = 100
        self.save()
