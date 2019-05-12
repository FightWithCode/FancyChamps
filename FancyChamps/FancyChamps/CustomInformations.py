from cricket_center.models import PlayerDetail, JoiningDetail, MatchDetail, ContestDetail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from cricket_matches.models import Winners65OutOf100Fee12
from django.apps import apps
from django.forms.models import model_to_dict
from accounts.models import User
from decimal import Decimal
from django.apps import apps

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


def PrintMe():
    print("I m work")

def CallThisForDistribution(match_slug):
    contest_obj = ContestDetail.objects.filter(contest_of_match__exact=MatchDetail.objects.filter(match_slug__exact=match_slug).first())
    print(contest_obj)
    for contest in contest_obj:
        print(contest.confirmed, contest.filled_status)
        if (contest.filled_status):
            print("I Got Called")
            DistributeWinning(contest.contest_slug, contest.prize_dist_type)
        elif (not contest.filled_status and contest.contest_size<=10 and contest.total_player_joined>1):
            contest.contest_winners = 1
            contest.contest_prize = (contest.total_player_joined*contest.contest_fee*90)/100
            contest.save()
            DistributeWinningToOne(contest.contest_slug)
        else:
            #Refund
            pass
        # else (not contest.confirmed and not contest.filled_status):
        #     RefundContestAmount(contest)


contest_prize_dict = {"hund_players_65_winners": {1: 60, 2: 45, 3: 35, 4: 25, 5: 25, 6: 20, 7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20, 19: 20,
                           20: 20, 21: 20, 22: 20, 23: 20, 24: 20, 25: 20, 26: 14, 27: 14, 28: 14, 29: 14, 30: 14, 31: 14, 32: 14, 33: 14, 34: 14, 35: 14, 36: 14,
                           37: 14, 38: 14, 39: 14, 40: 14, 41: 8, 42: 8, 43: 8, 44: 8, 45: 8, 46: 8, 47: 8, 48: 8, 49: 8, 50: 8, 51: 8, 52: 8, 53: 8, 54: 8, 55: 8,
                           56: 8, 57: 8, 58: 8, 59: 8, 60: 8, 61: 8, 62: 8, 63: 8, 64: 8, 65: 8,
    }
}


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
            tie_amount = tie_amount + prize
            tie_count = tie_count + 1
            if tie_start is None:
                tie_start = i + 1
            print("Tie Start :" + str(tie_start))
            print("Me")
        else:
            print("IE")
            if (tie_amount != 0) and (tie_start is not None):
                tie_amount = tie_amount + prize
                print("tie" + str(tie_amount))
                print("tiecount" + str(tie_count))
                winning_amount = tie_amount / (tie_count)
                for j in all_joined[tie_start - 1: i + 1]:
                    print("Executed")
                    print(winning_amount)
                    print(j.rank, j.joined_user)
                    j.winnings = winning_amount
                    print(j.winnings, winning_amount)
                    j.save()
                tie_amount = 0
                tie_start = 0
            if (tie_amount is 0) and (tie_start is None):
                print("No Teu")
                joined.winnings = prize
                print(prize)
                joined.save()
                # Save to Main Account.
                break;




def DistributeWinning(contest_slug, prize_dist_type):
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points')
    try:
        model_is = apps.get_registered_model('cricket_matches', prize_dist_type)
        prize_dest_obj = models.object.all().first()
        prize_dict = model_to_dict(prize_distri)
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
                tie_amount = tie_amount + prize_dict["Rank"+str(i + 1)]
                tie_count = tie_count + 1
                if tie_start is None:
                    tie_start = i + 1
                print("Tie Start :" + str(tie_start))
                print("Me")
            else:
                print("IE")
                if (tie_amount != 0) and (tie_start is not None):
                    tie_amount = tie_amount + prize_dict["Rank"+str(joined.rank)]
                    print("tie" + str(tie_amount))
                    print("tiecount" + str(tie_count))
                    winning_amount = tie_amount / (tie_count)
                    for j in all_joined[tie_start - 1: i + 1]:
                        print("Executed")
                        print(winning_amount)
                        print(j.rank, j.joined_user)
                        j.winnings = winning_amount
                        j.save()
                        print(j.winnings, winning_amount)
                    tie_amount = 0
                    tie_start = 0
                if (tie_amount is 0) and (tie_start is None):
                    print("No Teu")
                    joined.winnings = prize_dict["Rank"+str(joined.rank)]
                    print(prize_dict["Rank"+str(joined.rank)])
                    joined.save()

    except:
        contest_obj = ContestDetail.objects.filter(contest_slug__exact=contest_slug).first()
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
                tie_amount = tie_amount + prize_dict["Rank"+str(i + 1)]
                tie_count = tie_count + 1
                if tie_start is None:
                    tie_start = i + 1
                print("Tie Start :" + str(tie_start))
                print("Me")
            else:
                print("IE")
                if (tie_amount != 0) and (tie_start is not None):
                    tie_amount = tie_amount + prize_dict["Rank"+str(joined.rank)]
                    print("tie" + str(tie_amount))
                    print("tiecount" + str(tie_count))
                    winning_amount = tie_amount / (tie_count)
                    for j in all_joined[tie_start - 1: i + 1]:
                        print("Executed")
                        print(winning_amount)
                        print(j.rank, j.joined_user)
                        j.winnings = winning_amount
                        print(j.winnings, winning_amount)
                        j.save()
                    tie_amount = 0
                    tie_start = 0
                if (tie_amount is 0) and (tie_start is None):
                    print("No Teu")
                    joined.winnings = prize
                    print(prize)
                    joined.save()
                    # Save to Main Account.

                    break;


def AddMoneyToWidhrawable(match_slug):
    all_joined = JoiningDetail.objects.all()
    for obj in all_joined:
        user_obj = User.objects.filter(username__exact=obj.joined_user).first()
        user_obj.profile.widhdrawable_balance = user_obj.profile.widhdrawable_balance + Decimal(obj.winnings)
        user_obj.save()
        user_obj.profile.save()
# def RefundContestAmount(contest):
#     all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest.contest_slug).order_by('-total_team_points')
#     for i, joined in enumerate(all_joined):
#         user = Profile.objects.get(user__username__exact=joined.joined_user)
#         user.bonus = user.bonus + joined.bonus_deduction
#         user.balance = user.balance + joined.main_deduction
#         user.save()
