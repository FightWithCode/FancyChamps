from cricket_center.models import PlayerDetail, JoiningDetail, MatchDetail, ContestDetail, JoiningTransactionDetail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from cricket_matches.models import Winners65OutOf100Fee12
from django.apps import apps
from django.forms.models import model_to_dict
from accounts.models import User, Profile
from decimal import Decimal
from django.apps import apps
import random, string

#         model_name = match_obj.team_one + match_obj.team_two + "Team"
#         model_is = apps.get_registered_model('cricket_center', model_name)
#         HeadToHead = []
#         GreatAndGrand = []
#         FourOnOne = []
#         for contest in match_obj.contestdetail_set.all():
#             if contest.contest_category == "4 On 1":
#                 FourOnOne.append(contest)
#             if contest.contest_category == "Head to Head":
#                 HeadToHead.append(contest)
#             if contest.contest_category == "Great and Grand Winning":
#                 GreatAndGrand.append(contest)
#         total_teams = model_is.objects.filter(username_of_player__exact=request.user.username)


def update_total_team_points(match_slug):
        match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug).first()
        model_name = match_obj.team_one + match_obj.team_two + "Team"
        model_is = apps.get_registered_model('cricket_center', model_name)
        print(model_is)
        player_points_dict = {}
        for player in PlayerDetail.objects.filter(Q(player_current_team__exact=match_obj.short_team_one) | Q(player_current_team__exact=match_obj.short_team_two)):
            player_points_dict[player.player_name] = player.current_points
        print("Player DICT")
        print(player_points_dict)
        for detail in JoiningDetail.objects.filter(match_slug__exact=match_slug):
            print("Joining Detail")
            print(detail)
            total_points = 0
            print(detail.joined_user + "[" + str(detail.joined_user_team) + "]")
            team = model_is.objects.filter(full_team_name__exact=detail.joined_user + "[" + str(detail.joined_user_team) + "]" + match_slug).first()
            print(team)
            total_points = total_points + player_points_dict[team.Keeper]
            team.Keeper_Points = player_points_dict[team.Keeper]
            total_points = total_points + player_points_dict[team.Player2]
            team.Player2_Points = player_points_dict[team.Player2]
            total_points = total_points + player_points_dict[team.Player3]
            team.Player3_Points = player_points_dict[team.Player3]
            total_points = total_points + player_points_dict[team.Player4]
            team.Player4_Points = player_points_dict[team.Player4]
            total_points = total_points + player_points_dict[team.Player5]
            team.Player5_Points = player_points_dict[team.Player5]
            total_points = total_points + player_points_dict[team.Player6]
            team.Player6_Points = player_points_dict[team.Player6]
            total_points = total_points + player_points_dict[team.Player7]
            team.Player7_Points = player_points_dict[team.Player7]
            total_points = total_points + player_points_dict[team.Player8]
            team.Player8_Points = player_points_dict[team.Player8]
            total_points = total_points + player_points_dict[team.Player9]
            team.Player9_Points = player_points_dict[team.Player9]
            total_points = total_points + player_points_dict[team.Player10]
            team.Player10_Points = player_points_dict[team.Player10]
            total_points = total_points + (player_points_dict[team.Player11])
            team.Player11_Points = player_points_dict[team.Player11]
            total_points = total_points + player_points_dict[team.Captain]
            team.Captain_Points = player_points_dict[team.Captain]*2
            total_points = total_points + player_points_dict[team.Vice_Captain] / 2
            team.Vice_Captain_Points = player_points_dict[team.Vice_Captain] + player_points_dict[team.Vice_Captain] / 2
            detail.total_team_points = total_points
            detail.save()
            print("Print")
            print(team.Vice_Captain_Points)
            print(team)
            team.save()
        contest_obj = ContestDetail.objects.filter(contest_of_match__exact=MatchDetail.objects.filter(match_slug__exact=match_slug).first())
        for contest in contest_obj:
            contest_slug = contest.contest_slug
            # print(contest_slug)
            all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points', 'pk')
            print(all_joined)
            # user_teams_list = []
            # print(request.user.username)
            joined_count = all_joined.count()
            if joined_count!=0 and (all_joined.first().total_team_points == 0):
                for i in all_joined:
                    print(i.joined_user)
                    i.rank = 1
                    i.save()
                    # if(i.joined_user==request.user.username):
                    #     user_teams_list.append(i)
                # return render(request, "cricket_center/rankings.html", context={"match_obj": match_obj, "all_joined_with_ranking": all_joined, "contest_obj": contest_obj, "user":request.user.username, "user_teams_list":user_teams_list})
            else:
                print("ELSSSSSS")
                for i in all_joined[0:1]:
                    print("ELSSSSSSFOR")
                    print(i.joined_user)
                    i.last_rank = i.rank
                    i.rank = 1
                    i.save()
                for i, ranker in enumerate(all_joined[1:]):
                    print("HelloWorld.....................>#########################################################################")
                    print(ranker.total_team_points)
                    print(ranker.rank)
                    print(ranker.joined_user)
                    print("i = " + str(i))
                    print(all_joined[i].joined_user + " Hee  " + str(all_joined[i].total_team_points))
                    if ranker.total_team_points == all_joined[i].total_team_points:
                        ranker.last_rank = ranker.rank
                        ranker.rank = all_joined[i].rank
                        ranker.save()
                        # if(ranker.joined_user==request.user.username):
                        #     user_teams_list.append(ranker)
                    else:
                        ranker.last_rank = ranker.rank
                        ranker.rank = i + 2
                        ranker.save()
                        # if(ranker.joined_user==request.user.username):
                        #     user_teams_list.append(ranker)

def CancellOrApproveContest(match_slug):
    contest_obj = ContestDetail.objects.filter(contest_of_match__exact=MatchDetail.objects.filter(match_slug__exact=match_slug).first())
    for contest in contest_obj:
        if ((not contest.filled_status) and contest.contest_size<=100 and contest.total_player_joined>1 and (contest.confirmed is True)):
            contest.contest_winners = 1
            contest.prize_dist_type = "ToOne"
            print(contest.contest_slug)
            contest.contest_prize = (contest.total_player_joined*contest.contest_fee*90)//100
            contest.contest_name = "₹" + str(contest.contest_prize) + " Winnings"
            contest.save()
        elif ((not contest.filled_status) and (contest.confirmed is False)):
            contest.cancelled = True
            contest.save()
        elif ((contest.total_player_joined==1) and (contest.confirmed is True)):
            contest.cancelled = True
            print(contest.cancelled)
            contest.save()
        elif(contest.total_player_joined==0):
            contest.cancelled = True
            contest.save()
#             joined_qs = JoiningDetail.objects.filter(joined_contest_slug__exact=contest.contest_slug)
#             for joined in joined_qs:
#                 # print(joined.username)
#                 print(joined.balance_deduction)

#                 user = Profile.objects.filter(user__username__exact=joined.joined_user).first()
#                 # print(user)
#                 # print(user.username)
#                 # print(Decimal(user.balance))
#                 print(Decimal(joined.bonus_deduction))
#                 print(Decimal(joined.balance_deduction))
#                 user.bonus = Decimal(user.bonus) + Decimal(joined.bonus_deduction)
#                 user.balance = Decimal(user.balance) + Decimal(joined.balance_deduction)
#                 # print(user.balance)
#                 # print(user.bonus)
# #             # print(Decimal(user.balance))
#                 user.save()
#                 new_trans_obj = JoiningTransactionDetail(transaction_id=''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(15)),
#                                                         transaction_amt=joined.balance_deduction + joined.bonus_deduction,
#                                                         transact_user=joined.joined_user,
#                                                         transaction_message="Refund for Contest",
#                                                         transaction_type="added",
#                 )
#                 new_trans_obj.save()

                # transaction_id = models.CharField(max_length=255)
                # transaction_amt = models.IntegerField(default=0)
                # transact_user = models.CharField(max_length=64)
                # transaction_time = models.DateTimeField(auto_now=True)
                # transaction_message = models.CharField(max_length=255, default="")
                # transaction_type = models.CharField(max_length=16,default="added")
                # except:
                #     print("except")


def RefundCancelledContest(match_slug):
    contest_obj = ContestDetail.objects.filter(contest_of_match__exact=MatchDetail.objects.filter(match_slug__exact=match_slug).first())
    for contest in contest_obj:
        if (contest.cancelled):
            joined_qs = JoiningDetail.objects.filter(joined_contest_slug__exact=contest.contest_slug)
            for joined in joined_qs:
                # print(joined.username)


                user = Profile.objects.filter(user__username__exact=joined.joined_user).first()
                # print(user)
                # print(user.username)
                # print(Decimal(user.balance))
                print(user.bonus)
                print(user.widhdrawable_balance)
                print(user.balance)
                user.bonus = Decimal(user.bonus) + Decimal(joined.bonus_deduction)
                user.balance = Decimal(user.balance) + Decimal(joined.balance_deduction)
                user.widhdrawable_balance = Decimal(user.widhdrawable_balance) + Decimal(joined.winnings_deduction)
                print(user.balance)
                print(user.bonus)
                print(user.widhdrawable_balance)
                user.save()
                new_trans_obj = JoiningTransactionDetail(transaction_id=''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(15)),
                                                        transaction_amt=joined.balance_deduction + joined.bonus_deduction + joined.winnings_deduction,
                                                        transact_user=joined.joined_user,
                                                        transaction_message="Refund for Contest",
                                                        transaction_type="added",
                                                        refund_for_contest=joined.joined_contest_slug,
                )
                new_trans_obj.save()

                # transaction_id = models.CharField(max_length=255)
                # transaction_amt = models.IntegerField(default=0)
                # transact_user = models.CharField(max_length=64)
                # transaction_time = models.DateTimeField(auto_now=True)
                # transaction_message = models.CharField(max_length=255, default="")
                # transaction_type = models.CharField(max_length=16,default="added")
                # except:
                #     print("except")


def CallThisForDistribution(match_slug):
    contest_obj = ContestDetail.objects.filter(contest_of_match__exact=MatchDetail.objects.filter(match_slug__exact=match_slug).first(), cancelled__exact=False)
    print(contest_obj)
    print(len(contest_obj))
    for contest in contest_obj:
        if (len(contest.prize_dist_type)>5 and (not contest.cancelled)):
            print("I Got Called")
            DistributeWinning(contest.contest_slug, contest.prize_dist_type, contest.contest_winners)
        elif(len(contest.prize_dist_type)<=5 and (not contest.cancelled)):
            # contest.contest_winners = 1
            # contest.contest_prize = (contest.total_player_joined*contest.contest_fee*90)/100
            # contest.save()
            DistributeWinningToOne(contest.contest_slug)
        # else (not contest.confirmed and not contest.filled_status):
        #     RefundContestAmount(contest)


# prize_distro_dict = {
#     "Winners3OutOf10Fee53 ": {"Rank1":250, "Rank2":150, "Rank3":100,},
#     "Winners20OutOf35Fee49": {"Rank1":400, "Rank2": 200, "Rank3":100, "Rank4":75, "Rank5":75, "Rank6":50, "Rank7":50, "Rank8":50, "Rank9":50, "Rank10":50, "Rank11":40, "Rank12":40, "Rank13":40, "Rank14":40, "Rank15":40, "Rank16":40, "Rank17":40, "Rank18":40, "Rank19":40, "Rank20":40},
#     "Winners25OutOf40Fee31": {"Rank1":250, "Rank2": 125, "Rank3":80, "Rank4":50, "Rank5":50, "Rank6":40, "Rank7":40, "Rank8":40, "Rank9":40, "Rank10":40, "Rank11":23, "Rank12":23, "Rank13":23, "Rank14":23, "Rank15":23, "Rank16":23, "Rank17":23, "Rank18":23, "Rank19":23, "Rank20":23},

# }


    # {1: 60, 2: 45, 3: 35, 4: 25, 5: 25, 6: 20, 7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20, 19: 20,
    #                       20: 20, 21: 20, 22: 20, 23: 20, 24: 20, 25: 20, 26: 14, 27: 14, 28: 14, 29: 14, 30: 14, 31: 14, 32: 14, 33: 14, 34: 14, 35: 14, 36: 14,
    #                       37: 14, 38: 14, 39: 14, 40: 14, 41: 8, 42: 8, 43: 8, 44: 8, 45: 8, 46: 8, 47: 8, 48: 8, 49: 8, 50: 8, 51: 8, 52: 8, 53: 8, 54: 8, 55: 8,
    #                       56: 8, 57: 8, 58: 8, 59: 8, 60: 8, 61: 8, 62: 8, 63: 8, 64: 8, 65: 8,
    # }

def DistributeWinningToOne(contest_slug):
    print("I me Called")
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points')
    contest_obj = ContestDetail.objects.filter(contest_slug__exact=contest_slug).first()
    # total_joined = contest_obj.total_playet_joined
    prize = contest_obj.contest_prize
    tie_amount = 0
    tie_count = 1
    tie_start = None
    temp_var = None

    for i, joined in enumerate(all_joined):
        print("H")
        try:
            print("T")
            if joined.total_team_points == all_joined[i + 1].total_team_points:
                temp_var = True
            else:
                temp_var = False
        except IndexError:
            temp_var = False


        if temp_var:
            tie_amount = prize
            tie_count = tie_count + 1
            if tie_start is None:
                tie_start = i + 1
            print("Tie Start :" + str(tie_start))
            print("Me")
        else:
            print("IE")
            if (tie_amount != 0) and (tie_start is not None):
                tie_amount = prize
                print("tie" + str(tie_amount))
                print("tiecount" + str(tie_count))
                winning_amount = round(tie_amount / (tie_count), 1)
                for j in all_joined[tie_start - 1: i + 1]:
                    print("Executed")
                    print(winning_amount)
                    print(j.rank, j.joined_user)
                    j.winnings = winning_amount
                    print("***************************")
                    print(j.winnings, winning_amount)
                    j.save()
                tie_amount = 0
                tie_start = 0
                temp_var = None
                tie_start = None
                break;
            if (tie_amount is 0) and (tie_start is None):
                print("No Teu")
                joined.winnings = prize
                print("***************************second if")
                print(prize)
                joined.save()
                # Save to Main Account.
                break;



def DistributeWinning(contest_slug, prize_dist_type, contest_winners):
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points')
    # try:
    model_is = apps.get_registered_model('cricket_matches', prize_dist_type)
    print("************************************&&&&&&&&&&")
    print(model_is)
    prize_distri = model_is.objects.all().first()
    prize_dict_custom = {}
    prize_dict = model_to_dict(prize_distri)
    for i in prize_dict:
        key_is = i
        key_value_is = prize_dict[i]
        pos_list = key_is.lstrip("Rank").rsplit("To",1)
        if(len(pos_list)==1):
            prize_dict_custom.update({"Rank"+str(pos_list[0]): key_value_is})
        elif(len(pos_list)>1):
            s_range = int(pos_list[0])
            e_range = int(pos_list[1])
            for j in range(s_range,e_range+1):
                prize_dict_custom.update({"Rank"+str(j): key_value_is})

    print("*******Printing something special*******")
    print(prize_dict_custom)
    print("*******Printed something special*******")
    tie_amount = 0
    tie_count = 1
    tie_start = None
    temp_var = None
    print(contest_slug)
    for i, joined in enumerate(all_joined):
        if(i>=contest_winners):
            break;
        print("H")
        print(joined.joined_user)
        try:
            print("T")
            if joined.total_team_points == all_joined[i + 1].total_team_points:
                temp_var = True
            else:
                temp_var = False
        except IndexError:
            temp_var = False
        if temp_var:
            try:
                if tie_amount == 0:
                    tie_amount = tie_amount + prize_dict_custom["Rank"+str(i + 1)] + prize_dict_custom["Rank"+str(i + 2)]
                else:
                    tie_amount = tie_amount + prize_dict_custom["Rank"+str(i + 2)]
                tie_count = tie_count + 1
                if tie_start is None:
                    tie_start = i + 1
                print("Tie Start :" + str(tie_start))
                print("Me")
            except KeyError:
                print("I am the error...")
                break;
        else:
            print("IE")
            print(str(tie_amount), str(tie_start))
            if (tie_amount != 0) and (tie_start is not None):
                # tie_amount = tie_amount + prize_dict["Rank"+str(joined.rank)]
                # print("tie" + str(tie_amount))
                # print("tiecount" + str(tie_count))
                winning_amount = round(tie_amount / (tie_count), 1)
                for j in all_joined[tie_start - 1: i + 1]:
                    print("Executed")
                    print(winning_amount)
                    print(j.rank, j.joined_user)
                    j.winnings = winning_amount
                    j.save()
                    print(j.winnings, winning_amount)
                tie_amount = 0
                tie_start = None
                tie_count = 1
                continue;
            if (tie_amount is 0) and (tie_start is None):
                print("No Teu")
                joined.winnings = prize_dict_custom["Rank"+str(joined.rank)]
                print(prize_dict_custom["Rank"+str(joined.rank)])
                joined.save()

    # except:
    #     print("A excepttion from main")
    #     contest_obj = ContestDetail.objects.filter(contest_slug__exact=contest_slug).first()
    #     prize = contest_obj.contest_prize
    #     tie_amount = 0
    #     tie_count = 1
    #     tie_start = None
    #     temp_var = None

    #     for i, joined in enumerate(all_joined):
    #         print("H")
    #         try:
    #             print("T")
    #             if joined.total_team_points == all_joined[i + 1].total_team_points:
    #                 temp_var = True
    #             else:
    #                 temp_var = False
    #         except IndexError:
    #             temp_var = False
    #         if temp_var:
    #             tie_amount = tie_amount + prize_dict["Rank"+str(i + 1)]
    #             tie_count = tie_count + 1
    #             if tie_start is None:
    #                 tie_start = i + 1
    #             print("Tie Start :" + str(tie_start))
    #             print("Me")
    #         else:
    #             print("IE")
    #             if (tie_amount != 0) and (tie_start is not None):
    #                 tie_amount = tie_amount + prize_dict["Rank"+str(joined.rank)]
    #                 print("tie" + str(tie_amount))
    #                 print("tiecount" + str(tie_count))
    #                 winning_amount = tie_amount / (tie_count)
    #                 for j in all_joined[tie_start - 1: i + 1]:
    #                     print("Executed")
    #                     print(winning_amount)
    #                     print(j.rank, j.joined_user)
    #                     j.winnings = winning_amount
    #                     print(j.winnings, winning_amount)
    #                     j.save()
    #                 tie_amount = 0
    #                 tie_start = 0
    #             if (tie_amount is 0) and (tie_start is None):
    #                 print("No Teu")
    #                 joined.winnings = prize
    #                 print(prize)
    #                 joined.save()
    #                 # Save to Main Account.

    #                 break;


def AddMoneyToWidhrawable(match_slug):
    all_joined = JoiningDetail.objects.filter(match_slug__exact=match_slug)
    list_of_winners = []
    for obj in all_joined:
        if(obj.winnings>0):
            print("If block")
            print(list_of_winners)
            print(obj.joined_user)
            try:
                user_obj = User.objects.filter(username__exact=obj.joined_user).first()
                user_obj.profile.widhdrawable_balance = user_obj.profile.widhdrawable_balance + Decimal(obj.winnings)
                if obj.joined_user in list_of_winners:
                    pass
                else:
                    print(obj.joined_user)
                    user_obj.profile.total_wins = user_obj.profile.total_wins + 1
                    list_of_winners.append(obj.joined_user)
                user_obj.save()
                user_obj.profile.save()
                new_trans_obj = JoiningTransactionDetail(transaction_id=''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(15)),
                                                            transaction_amt=obj.winnings,
                                                            transact_user=user_obj.username,
                                                            transaction_message="Won a Contest",
                                                            transaction_type="added",
                )
                new_trans_obj.save()
            except Exception as e:
                print("Something Went Wrong")
                print(e)

def UpdateMatchPlayed(match_slug):
    list_of_contest = []
    list_of_user = []
    all_joined = JoiningDetail.objects.filter(match_slug__exact=match_slug)
    for joined in all_joined:
        if (joined.joined_contest_slug in list_of_contest) and (joined.joined_user in list_of_user) and (joined.joined_user in list_of_contest):
            continue
        else:
            # try:
            user_obj = User.objects.filter(username__exact=joined.joined_user).first()
            if joined.joined_user in list_of_user:
                pass
            else:
                user_obj.profile.match_played = user_obj.profile.match_played + 1
                list_of_user.append(joined.joined_user)
            # user_obj.profile.contest_played = user_obj.profile.contest_played + 1
            # if (joined.joined_contest_slug in list_of_contest):
            #     pass
            # else:
            #     list_of_contest.append(joined.joined_contest_slug)
            #     list_of_contest.append(joined.joined_user)
            user_obj.save()
            user_obj.profile.save()

            # except:
            #     print("something went wrong")

# def RefundContestAmount(contest):
#     all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest.contest_slug).order_by('-total_team_points')
#     for i, joined in enumerate(all_joined):
#         user = Profile.objects.get(user__username__exact=joined.joined_user)
#         user.bonus = user.bonus + joined.bonus_deduction
#         user.balance = user.balance + joined.balance_deduction
#         user.save()
