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


    def save(self, *args, **kwargs):
        print(self.match_date)
        print(self.match_date.timestamp())
        self.match_tick = self.match_date.timestamp()
        if self.match_slug == "Test":
            self.match_slug = MatchSlugGenerator(self.match_name, self.team_one, self.team_two, self.match_date)
        super(MatchDetail, self).save(*args, **kwargs)

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
    contest_of_match = models.ForeignKey(MatchDetail)
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
    filled_status = models.BooleanField(default=False)
    bonus_contest = models.BooleanField(default=False)
    free_contest = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    prize_dist_type = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        joined = JoiningDetail.objects.filter(joined_contest_slug__exact=self.contest_slug)
        self.total_player_joined = joined.count()
        self.joined_percentage = (self.total_player_joined * 100) / self.contest_size
        if self.contest_slug == "Test":
            self.contest_slug = ContestSlugGenerator(self.contest_name, self.contest_category, self.contest_prize, self.contest_fee)
        if self.contest_size == self.total_player_joined:
            self.filled_status = True
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
    main_deduction = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.joined_contest_slug + "[" + self.joined_user_team + "]"


class INDNZTeam(models.Model):
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
        super(INDNZTeam, self).save(*args, **kwargs)

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def update_total_team_points(self, user, team_no, match_slug):
        self.total_team_points = 100
        self.save()


class ENGAFGTeam(models.Model):
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
        super(ENGAFGTeam, self).save(*args, **kwargs)

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def update_total_team_points(self, user, team_no, match_slug):
        self.total_team_points = 100
        self.save()








# class WIBANTeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")

#     Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(WIBANTeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


# class AFGSCOTeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")

#     Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(AFGSCOTeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


# class CSKDCTeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")

#     Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(CSKDCTeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


# class ENGPAKTeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")

#     Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(ENGPAKTeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


# class MICSKTeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")

#     Keeper_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player2_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player3_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player4_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player5_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player6_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player7_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player8_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player9_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player10_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Player11_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     Vice_Captain_Points = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(MICSKTeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


# class CSKMITeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")
#     # total_team_points = models.DecimalField(max_digits=3, decimal_places=2, default=0)
#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(CSKMITeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


# class SRHDCTeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")
#     # total_team_points = models.DecimalField(max_digits=3, decimal_places=2, default=0)
#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(SRHDCTeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


# class BANIRETeam(models.Model):
#     Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11 = models.CharField(max_length=255, default="")
#     Captain = models.CharField(max_length=255, default=" ")
#     Vice_Captain = models.CharField(max_length=255, default=" ")
#     # total_team_points = models.DecimalField(max_digits=3, decimal_places=2, default=0)
#     total_batsmen = models.IntegerField(default=4)
#     total_allrounders = models.IntegerField(default=3)
#     total_bowlers = models.IntegerField(default=3)
#     team_no = models.IntegerField(default=1)
#     username_of_player = models.CharField(max_length=64)
#     # total_credits_used = models.IntegerField(default=100)
#     total_credits_used = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
#     match_slug = models.CharField(max_length=100)
#     full_team_name = models.CharField(max_length=255, default="Something")

#     def save(self, *args, **kwargs):
#         self.full_team_name = self.username_of_player + "[" + str(self.team_no) + "]" + self.match_slug
#         super(BANIRETeam, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def __unicode__(self):
#         return self.username_of_player + "[" + str(self.team_no) + "]"

#     def update_total_team_points(self, user, team_no, match_slug):
#         self.total_team_points = 100
#         self.save()


class JoiningTransactionDetail(models.Model):
    transaction_id = models.CharField(max_length=255)
    transaction_amt = models.IntegerField(default=0)
    transact_user = models.CharField(max_length=64)
    transaction_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_id
