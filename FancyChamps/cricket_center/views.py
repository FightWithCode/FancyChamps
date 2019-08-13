from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import MatchDetail, PlayerDetail, JoiningDetail, ContestDetail, JoiningTransactionDetail, ContestMessages
import time
from decimal import Decimal
from .forms import CreateTeamKeeperForm, CreateTeamBatsmenForm, CreateTeamAllroundersForm, CreateTeamBowlersForm
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from accounts.models import Profile
from django.http import Http404
from django.apps import apps
from django.forms.models import model_to_dict
import razorpay, random, string
import operator
from collections import OrderedDict


@login_required(login_url='IndexView')
def CricketCenterIndexView(request):
    upcomming_match_obj = MatchDetail.objects.filter(match_tick__gte=time.time()).order_by('match_date')
    live_match_obj = MatchDetail.objects.filter(match_tick__lte=time.time(), history_activate=False, live=True).order_by('match_date')
    history_match_obj = MatchDetail.objects.filter(history_activate=True).order_by('-match_tick')
    return render(request, "cricket_center/cricket_center_index.html", context={'upcomming_match_obj': upcomming_match_obj, "live_match_obj": live_match_obj, "history_match_obj": history_match_obj})


@login_required(login_url='IndexView')
def MyTeams(request, match_slug):
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug).first()
    model_name = match_obj.team_one + match_obj.team_two + "Team"
    model_is = apps.get_registered_model('cricket_center', model_name)
    my_teams = model_is.objects.filter(username_of_player__exact=request.user.username)
    return render(request, "cricket_center/my_teams.html", context={'match_slug': match_slug, 'my_teams': my_teams, 'match_obj': match_obj})


@login_required(login_url='IndexView')
def JoinedContests(request, match_slug):
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    model_name = match_objs.first().team_one + match_objs.first().team_two + "Team"
    model_is = apps.get_registered_model('cricket_center', model_name)
    match_obj = match_objs.first()
    all_joined = JoiningDetail.objects.filter(Q(joined_user__exact=request.user.username), Q(match_slug__exact=match_obj.match_slug))
    contests_joined = []
    for contest in all_joined:
        contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest.joined_contest_slug)
        if contest_obj not in contests_joined:
            contests_joined.append(contest_obj)
    total_teams = model_is.objects.filter(username_of_player__exact=request.user.username)
    contests_count = len(contests_joined)
    return render(request, "cricket_center/joined_contests.html", context={'contests_joined': contests_joined, 'match_slug': match_slug, 'contests_count': contests_count, 'total_teams': total_teams, 'match_obj': match_obj})


def MessageCreateShow(request):
    messages={
        "1": "Hello!","2": "Hi!","3": "Good Bye.","4": "Nice to Meet you!","5": "Good Luck!","6": "I Won!",
        "7":"I Lose!","8":"Too Close.","9":"Well Played!","10":"Same Captain!","11":"#LetsBeTheChampsTogether",
        }
    contest_slug = request.GET.get('slug')
    print("1")
    print(type(request.GET.get('message_no')))
    if("0"==request.GET.get('message_no')):
        print("2")
        messages_of_contest = ContestMessages.objects.filter(contest_slug__exact=contest_slug)
        data=messages_of_contest.values()
        data =list(data)
        data.append(request.user.username)
        saved = False
        data.append(saved)
    else:
        print("3")
        message_is = messages[request.GET.get('message_no')]
        message_obj = ContestMessages(
            contest_slug=contest_slug,
            message=message_is,
            user=request.user.username
        )

        messages_of_contest = ContestMessages.objects.filter(contest_slug__exact=contest_slug)
        try:
            if(messages_of_contest.latest('id').user==request.user.username):
                print("if")
                data=messages_of_contest.values()
                data =list(data)
                data.append(request.user.username)
                saved = False
                data.append(saved)
                print(data[-1])
            else:
                print("else")
                message_obj.save()
                messages_of_contest = ContestMessages.objects.filter(contest_slug__exact=contest_slug)
                data=messages_of_contest.values()
                data =list(data)
                data.append(request.user.username)
                saved = True
                data.append(saved)
                print(data[-1])
        except:
            print("except")
            message_obj.save()
            messages_of_contest = ContestMessages.objects.filter(contest_slug__exact=contest_slug)
            data=messages_of_contest.values()
            data =list(data)
            data.append(request.user.username)
            saved = True
            data.append(saved)
            print(data[-1])
    return JsonResponse(data, safe=False)


def ViewPayout(request, contest_slug):
    contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest_slug)
    dist_type = contest_obj.prize_dist_type
    try:
        print("Try Executed")
        print(dist_type)
        model_is = apps.get_registered_model('cricket_matches', dist_type)
        print(model_is)
        prize_distri = model_is.objects.first()
        print(prize_distri)
        data = model_to_dict(prize_distri)
        print(data)
    except:
        data = {'Rank1': contest_obj.contest_prize}
    data = sorted(data.items(),key=operator.itemgetter(1),reverse=True)
    print(data)
    dict_data = OrderedDict(data)
    dict_data["multiple_entry"] = contest_obj.multiple_entry
    dict_data["bonus_contest"] = contest_obj.bonus_contest
    dict_data["confirmed"] = contest_obj.confirmed
    return JsonResponse(dict_data)


    # contest_of_match = models.ForeignKey(MatchDetail)
    # contest_name = models.CharField(max_length=100)
    # contest_slug = models.CharField(max_length=512, unique=True, default="Test")
    # contest_prize = models.IntegerField()
    # contest_fee = models.IntegerField()
    # contest_size = models.IntegerField()
    # contest_winners = models.IntegerField(default=1)
    # total_player_joined = models.IntegerField()
    # joined_percentage = models.IntegerField(default=0)
    # contest_category = models.CharField(max_length=100)
    # multiple_entry = models.BooleanField(default=False)
    # filled_status = models.BooleanField(default=False)
    # bonus_contest = models.BooleanField(default=False)
    # free_contest = models.BooleanField(default=False)
    # confirmed = models.BooleanField(default=False)
    # prize_dist_type = models.CharField(max_length=100)


@login_required(login_url='IndexView')
def SingleMatchView(request, match_slug):
    try:
        match_obj = MatchDetail.objects.get(match_slug__exact=match_slug)
    except MatchDetail.DoesNotExist:
        return HttpResponse("Something went Wrong!")
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug).first()
    # if match_obj.match_tick < time.time():
    #     time_over_error = True
    #     return render(request, "cricket_center/match.html", context={"time_over_error": time_over_error})

    print(match_obj.match_tick)
    print(time.time())

    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    else:
        model_name = match_obj.team_one + match_obj.team_two + "Team"
        model_is = apps.get_registered_model('cricket_center', model_name)
        HeadToHead = []
        GreatAndGrand = []
        FourOnOne = []
        FreeRoll = []
        ThreeOnOne = []
        EqualContests = []
        OtherContests = []
        BonusContests = []
        AllGoesToChampionContests = []
        for contest in match_obj.contestdetail_set.all():
            if contest.contest_category == "4 On 1":
                FourOnOne.append(contest)
            if contest.contest_category == "Head to Head":
                HeadToHead.append(contest)
            if contest.contest_category == "Great and Grand Winning":
                GreatAndGrand.append(contest)
            if contest.contest_category == "3 On 1":
                ThreeOnOne.append(contest)
            if contest.contest_category == "Free Roll":
                FreeRoll.append(contest)
            if contest.contest_category == "Other":
                OtherContests.append(contest)
            if contest.contest_category == "Equality is Priority":
                EqualContests.append(contest)
            if contest.contest_category == "All Goes to Champion":
                AllGoesToChampionContests.append(contest)
            if contest.bonus_contest:
                BonusContests.append(contest)
        total_teams = model_is.objects.filter(username_of_player__exact=request.user.username)
        all_joined = JoiningDetail.objects.filter(Q(joined_user__exact=request.user.username), Q(match_slug__exact=match_obj.match_slug))
        contest_joined = []
        all_joined_list = []
        for contest in all_joined:
            all_joined_list.append(contest.joined_contest_slug)
            if contest.joined_contest_slug not in contest_joined:
                contest_joined.append(contest.joined_contest_slug)
        print(GreatAndGrand, match_obj.contestdetail_set.all())
        return render(request, "cricket_center/match.html", context={'AllGoesToChampionContests': AllGoesToChampionContests, 'BonusContests': BonusContests, 'FreeRoll':FreeRoll, 'ThreeOnOne':ThreeOnOne, 'OtherContests':OtherContests, 'match_obj': match_obj, 'FourOnOne': FourOnOne, "HeadToHead": HeadToHead, 'EqualContests': EqualContests, 'GreatAndGrand': GreatAndGrand, 'match_slug': match_slug, 'total_teams': total_teams, 'contest_joined': contest_joined, 'all_joined_list': all_joined_list})


@login_required(login_url='IndexView')
def SingleMatchHistoryView(request, match_slug):
    # match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    # model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    # model_is = apps.get_registered_model('cricket_center', model_name)
    all_joined = JoiningDetail.objects.filter(joined_user__exact=request.user.username, match_slug__exact=match_slug)
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    if match_obj.match_tick > time.time() or (not match_obj.history_activate):
        return redirect('/cricket_center/')
    else:
        contests_joined = []
        contest_done = []
        for contest in all_joined:
            contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest.joined_contest_slug)
            if contest_obj not in contest_done:
                obj = JoiningDetail.objects.filter(joined_user__exact=request.user.username,joined_contest_slug__exact=contest_obj.contest_slug).order_by("rank").first()
                print(obj)
                print(obj.rank)
                contest_dict = model_to_dict(contest_obj)
                contest_dict["top_rank"] = obj.rank
                contest_done.append(contest_obj)
                contests_joined.append(contest_dict)
                print(contest_dict)
        contests_count = len(contests_joined)
        # all_joined = JoiningDetail.objects.filter(username_of_player__exact=request.user.username)
        # contests = []
        # for team in all_joined:
        #     if team.joined_contest_slug not in contests:
        #         contests.append(team.contest_slug)

        return render(request, "cricket_center/match_his.html", context={"match_slug": match_slug, "contests_joined": contests_joined, "match_obj": match_obj,"contests_count":contests_count,})


@login_required(login_url='IndexView')
def SingleMatchLiveView(request, match_slug):
    all_joined = JoiningDetail.objects.filter(joined_user__exact=request.user.username, match_slug__exact=match_slug)
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    if match_obj.match_tick > time.time():
        return redirect('/cricket_center/')
    else:
        contests_joined = []
        contest_done = []
        for contest in all_joined:
            contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest.joined_contest_slug)
            if contest_obj not in contest_done:
                obj = JoiningDetail.objects.filter(joined_user__exact=request.user.username,joined_contest_slug__exact=contest_obj.contest_slug).order_by("rank").first()
                print(obj)
                print(obj.rank)
                contest_dict = model_to_dict(contest_obj)
                contest_dict["top_rank"] = obj.rank
                contest_done.append(contest_obj)
                contests_joined.append(contest_dict)
                print(contest_dict)
        contests_count = len(contests_joined)
        return render(request, "cricket_center/live_match.html", context={"match_slug": match_slug, "contests_joined": contests_joined, "match_obj": match_obj, "contests_count":contests_count,})


@login_required(login_url='IndexView')
def ContestsRankings(request, match_slug, contest_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    if match_obj.match_tick > time.time():
        return redirect('/cricket_center/')
    else:
        contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest_slug)
        all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points', 'pk')
        user_teams_list = []
        for i in all_joined:
            if(i.joined_user==request.user.username):
                user_teams_list.append(i)
        # print(request.user.username)
        # if all_joined.first().total_team_points == 0:
        #     for i in all_joined:
        #         print(i.joined_user)
        #         i.rank = 1
        #         i.save()
        #         if(i.joined_user==request.user.username):
        #             user_teams_list.append(i)
        #     return render(request, "cricket_center/rankings.html", context={"match_obj": match_obj, "all_joined_with_ranking": all_joined, "contest_obj": contest_obj, "user":request.user.username, "user_teams_list":user_teams_list})
        # else:
        #     print("ELSSSSSS")
        #     for i in all_joined[0:1]:
        #         print("ELSSSSSSFOR")
        #         print(i.joined_user)
        #         i.last_rank = i.rank
        #         i.rank = 1
        #         i.save()
        #     for i, ranker in enumerate(all_joined[1:]):
        #         print(ranker.total_team_points)
        #         print(ranker.rank)
        #         print(ranker.joined_user)
        #         print("i = " + str(i))
        #         print(all_joined[i].joined_user + " Hee  " + str(all_joined[i].total_team_points))
        #         if ranker.total_team_points == all_joined[i].total_team_points:
        #             ranker.last_rank = ranker.rank
        #             ranker.rank = all_joined[i].rank
        #             ranker.save()
        #             if(ranker.joined_user==request.user.username):
        #                 user_teams_list.append(ranker)
        #         else:
        #             ranker.last_rank = ranker.rank
        #             ranker.rank = i + 2
        #             ranker.save()
        #             if(ranker.joined_user==request.user.username):
        #                 user_teams_list.append(ranker)

        return render(request, "cricket_center/rankings.html", context={"match_obj": match_obj, "all_joined_with_ranking": all_joined, "contest_obj": contest_obj, "user":request.user.username, "user_teams_list":user_teams_list})


@login_required(login_url='IndexView')
def ContestsViews(request, match_slug, contest_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest_slug)
    print("I got exe")
    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    # match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    # model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    # model_is = apps.get_registered_model('cricket_center', model_name)
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points')
    # # all_joined[0].rank = 1
    # # all_joined[0].save()
    for ranker in all_joined:
        ranker.rank = 1
        ranker.save()
    # for i, ranker in enumerate(all_joined[1:]):
    #     try:
    #         if ranker.total_team_points == all_joined[i].total_team_points:
    #             print(str(i) + " true")
    #             ranker.rank = all_joined[i].rank
    #             ranker.save()
    #         else:
    #             ranker.rank = i + 2
    #             ranker.save()
    #     except IndexError:
    #         pass
    return render(request, "cricket_center/view_contest.html", context={"match_obj": match_obj, "all_joined_with_ranking": all_joined, "contest_obj": contest_obj})


@login_required(login_url='IndexView')
def CapturePayment(request):
    razorpay_client = razorpay.Client(auth=("rzp_test_C4Ohgv6Fhh2piC", "nmz1n0jwb5avB6uEB1Fpk2dG"))
    response_of_payment = razorpay_client.payment.capture(request.POST.get("razorpay_payment_id"), request.POST.get("amt"))
    print(response_of_payment)
    transaction_obj = TransactionDetail(
                                            transaction_id=''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(15)),
                                            razorpay_transaction_payment_id=request.POST.get("razorpay_payment_id"),
                                            transaction_amt=request.POST.get("amt"),
                                            transact_user=request.user.username,
                                            captured=False
                                  )
    print(response_of_payment["status"], response_of_payment["captured"])
    if response_of_payment["status"] == "captured":
        print("Ok I am Fine HERE")

    if response_of_payment["captured"] is True:
        print("Ok I am ALSO Fine HERE")

    if (response_of_payment["status"] == "captured") and (response_of_payment["captured"] is True):
        transaction_obj.transaction_amt = response_of_payment["amount"]
        transaction_obj.captured = True
        data = {
            'success': True,
            'amount': response_of_payment["amount"],
        }
        user_obj = Profile.objects.get(user__username__exact=request.user.username)
        user_obj.balance = user_obj.balance + Decimal(response_of_payment["amount"]/100)
        user_obj.save()
        transaction_obj.save()
    else:
        data = {
            'success': False,
        }
    return JsonResponse(data)


@login_required(login_url='IndexView')
def PayAndJoin(request):
    error = False
    log_in_error = False
    contest_error = False
    match_slug = request.POST.get('match_slug')
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    contest_slug = request.POST.get('contest_slug')
    team_no = request.POST.get('team_no')
    print("Printitn.............................................")
    print(match_slug,contest_slug)
    already_joined_or_filled = False;
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug, joined_user__exact=request.user.username)

    try:
        user = Profile.objects.get(user__username__exact=request.user.username)
    except Profile.DoesNotExist:
        error = True
        log_in_error = True

    try:
        contest = ContestDetail.objects.get(contest_slug__exact=contest_slug)
        if(((contest.multiple_entry is True) and (len(all_joined) < 3)) or ((contest.multiple_entry is False) and (len(all_joined) == 0)) and (contest.filled_status is False)) :
            error = False
        else:
            error = True
            already_joined_or_filled = True
    except ContestDetail.DoesNotExist:
        print("#####################################*******************I am the fault")
        error = True
        contest_error = True

    if error is False:
        # user = Profile.objects.get(user__username__exact=request.user.username)
        all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug)
        contest = ContestDetail.objects.get(contest_slug__exact=contest_slug)

        user_balance = user.balance
        user_winnings = user.widhdrawable_balance
        user_bonus = user.bonus

        joined_players = all_joined.count()
        contest_name = contest.contest_name
        contest_prize = contest.contest_prize
        contest_fee = contest.contest_fee
        bonus_percent = contest.bonus_percent
        low_balance = 0
        add_money = 0
        if contest.bonus_contest is True:
            print("Local")
            if user_bonus >= Decimal(round((bonus_percent*contest_fee)/100, 0)):
                deduction_from_bonus = Decimal(round((bonus_percent*contest_fee)/100, 0))
                new_bonus = user_bonus - deduction_from_bonus
                user.bonus = new_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > user_balance + user_winnings:
                    low_balance = 1
                    add_money = deduction_from_main - (user_balance + user_winnings)
                else:
                    print(user_balance, deduction_from_main)
                    if(deduction_from_main > user_balance):
                        deduction_from_main = user_balance
                        new_user_balance = user_balance - deduction_from_main
                        user.balance  = new_user_balance
                        deduction_from_winnings = contest_fee - (deduction_from_bonus + deduction_from_main)
                        new_user_winnings = user_winnings - deduction_from_winnings
                        user.widhdrawable_balance = new_user_winnings
                    else:
                        new_user_balance = user_balance - deduction_from_main
                        user.balance = new_user_balance
                        deduction_from_winnings = 0
                    join_obj = JoiningDetail(bonus_deduction=deduction_from_bonus, balance_deduction=deduction_from_main, winnings_deduction=deduction_from_winnings,  joined_user=request.user.username, joined_contest_slug=contest_slug, joined_user_team=team_no, match_slug=match_slug)
                    join_transaction_detail_obj = JoiningTransactionDetail(transaction_id=''.join(random.SystemRandom().choice(string.ascii_lowercase  + string.digits) for _ in range(15)),
                                                                        transaction_amt=contest_fee,
                                                                        transact_user=request.user.username,
                                                                        transaction_message = "Joined a Contest",
                                                                        transaction_type = "deducted",
                    )
                    join_transaction_detail_obj.save()
                    user.save()
                    join_obj.save()
                    contest.save()

                    if contest.filled_status:
                        new_contest_obj = ContestDetail(
                            contest_of_match=MatchDetail.objects.filter(match_slug__exact=match_slug).first(),
                            contest_name=contest.contest_name,
                            contest_slug="Test",
                            contest_prize=contest.contest_prize,
                            contest_fee = contest.contest_fee,
                            contest_size = contest.contest_size,
                            contest_winners = contest.contest_winners,
                            total_player_joined = 0,
                            joined_percentage = 0,
                            contest_category = contest.contest_category,
                            multiple_entry = contest.multiple_entry,
                            filled_status = False,
                            bonus_contest = contest.bonus_contest,
                            free_contest = contest.free_contest,
                            confirmed = contest.confirmed,
                            prize_dist_type = contest.prize_dist_type,

                        )
                        new_contest_obj.save()

            else:
                deduction_from_bonus = user_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                user.bonus = user_bonus - deduction_from_bonus
                # deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > user_balance + user_winnings:
                    low_balance = 1
                    add_money = deduction_from_main - (user_balance + user_winnings)
                else:
                    if(deduction_from_main > user_balance):
                        deduction_from_main = user_balance
                        new_user_balance = user_balance - deduction_from_main
                        user.balance  = new_user_balance
                        deduction_from_winnings = contest_fee - (deduction_from_bonus + deduction_from_main)
                        new_user_winnings = user_winnings - deduction_from_winnings
                        user.widhdrawable_balance = new_user_winnings
                    else:
                        new_user_balance = user_balance - deduction_from_main
                        user.balance = new_user_balance
                        deduction_from_winnings = 0

                    # user.balance = user_balance - deduction_from_main
                    join_obj = JoiningDetail(bonus_deduction=deduction_from_bonus, balance_deduction=deduction_from_main, winnings_deduction=deduction_from_winnings, joined_user=request.user.username, joined_contest_slug=contest_slug, joined_user_team=team_no, match_slug=match_slug)
                    join_transaction_detail_obj = JoiningTransactionDetail(transaction_id=''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(15)),
                                                                        transaction_amt=contest_fee,
                                                                        transact_user=request.user.username,
                                                                        transaction_message = "Joined a Contest",
                                                                        transaction_type = "deducted",
                    )
                    user.save()
                    join_obj.save()
                    contest.save()
                    if contest.filled_status:
                        new_contest_obj = ContestDetail(
                            contest_of_match=MatchDetail.objects.filter(match_slug__exact=match_slug).first(),
                            contest_name=contest.contest_name,
                            contest_slug="Test",
                            contest_prize=contest.contest_prize,
                            contest_fee = contest.contest_fee,
                            contest_size = contest.contest_size,
                            contest_winners = contest.contest_winners,
                            total_player_joined = 0,
                            joined_percentage = 0,
                            contest_category = contest.contest_category,
                            multiple_entry = contest.multiple_entry,
                            filled_status = False,
                            bonus_contest = contest.bonus_contest,
                            free_contest = contest.free_contest,
                            confirmed = contest.confirmed,
                            prize_dist_type = contest.prize_dist_type,

                        )
                        new_contest_obj.save()
        else:
            deduction_from_bonus = 0
            deduction_from_main = contest_fee
            if deduction_from_main > user_balance + user_winnings:
                low_balance = 1
                add_money = deduction_from_main - (user_balance + user_winnings)
            else:
                if(deduction_from_main > user_balance):
                    print("I am the choosed one!")
                    deduction_from_main = user_balance
                    new_user_balance = user_balance - deduction_from_main
                    user.balance  = new_user_balance
                    deduction_from_winnings = contest_fee - (deduction_from_bonus + deduction_from_main)
                    new_user_winnings = user_winnings - deduction_from_winnings
                    user.widhdrawable_balance = new_user_winnings
                else:
                    new_user_balance = user_balance - deduction_from_main
                    user.balance = new_user_balance
                    deduction_from_winnings = 0
                join_transaction_detail_obj = JoiningTransactionDetail(transaction_id=''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(15)),
                                                                        transaction_amt=contest_fee,
                                                                        transact_user=request.user.username,
                                                                        transaction_message = "Joined a Contest",
                                                                        transaction_type = "deducted",
                )
                # user.balance = user_balance - deduction_from_main
                join_obj = JoiningDetail(bonus_deduction=deduction_from_bonus, balance_deduction=deduction_from_main, winnings_deduction=deduction_from_winnings, joined_user=request.user.username, joined_contest_slug=contest_slug, joined_user_team=team_no, match_slug=match_slug)
                user.save()
                join_obj.save()
                contest.save()
                join_transaction_detail_obj.save()
                if contest.filled_status:
                    new_contest_obj = ContestDetail(
                        contest_of_match=MatchDetail.objects.filter(match_slug__exact=match_slug).first(),
                        contest_name=contest.contest_name,
                        contest_slug="Test",
                        contest_prize=contest.contest_prize,
                        contest_fee = contest.contest_fee,
                        contest_size = contest.contest_size,
                        contest_winners = contest.contest_winners,
                        total_player_joined = 0,
                        joined_percentage = 0,
                        contest_category = contest.contest_category,
                        multiple_entry = contest.multiple_entry,
                        filled_status = False,
                        bonus_contest = contest.bonus_contest,
                        free_contest = contest.free_contest,
                        confirmed = contest.confirmed,
                        prize_dist_type = contest.prize_dist_type,
                    )
                    new_contest_obj.save()
        print(user, user.balance, user.bonus, joined_players, contest_name, contest_prize, contest_fee, deduction_from_bonus, deduction_from_main, low_balance, add_money)
        data = {
            'called': "Ok I Got A Call From AJAX to Views",
            'contest_name': contest_name,
            'user_balance': user_balance,
            'user_bonus': user_bonus,
            'user_winnings': user_winnings,
            'joined_players': joined_players,
            'contest_prize': contest_prize,
            'contest_fee': contest_fee,
            'deduction_from_bonus': deduction_from_bonus,
            'deduction_from_main': deduction_from_main,
            'low_balance': low_balance,
            'add_money': add_money,
            'match_slug': match_slug,
            'contest_slug': contest_slug,
            'balance': user.balance,
            'bonus': user.bonus,
            'error': error,
        }
        return JsonResponse(data)
    else:
        data = {
            "error": error,
            "log_in_error": log_in_error,
            "contest_error": contest_error,
            "already_joined_or_filled": already_joined_or_filled,
        }
        return JsonResponse(data)


@login_required(login_url='IndexView')
def ProceedToPay(reques):
    print("Ok I am Wokruinf Fine")
    return HttpResponse("Invalid login details supplied.")


@login_required(login_url='IndexView')
def ContestJoinNow(request, match_slug, contest_slug):
    print("He got the whole world!")
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    print("Print it")
    print(match_slug, contest_slug)
    profile_error = False
    multiple_entry_error = False
    log_in_error = False
    contest_error = False
    match_slug = match_slug
    contest_slug = contest_slug
    already_joined_or_filled = False
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug, joined_user=request.user.username)
    print("Print this : " + str(len(all_joined)))
    try:
        user = Profile.objects.get(user__username__exact=request.user.username)
    except Profile.DoesNotExist:
        print("I executed")
        profile_error = True
        log_in_error = True
    print(profile_error)
    try:
        contest = ContestDetail.objects.get(contest_slug__exact=contest_slug)
        if(((contest.multiple_entry is True) and (len(all_joined) < 6)) or ((contest.multiple_entry is False) and (len(all_joined) == 0)) and (contest.filled_status is False)):
            multiple_entry_error = False
        else:
            multiple_entry_error = True
            already_joined_or_filled = True
    except ContestDetail.DoesNotExist:
        contest_error = True

    if (profile_error is False) and (multiple_entry_error is False) and (contest_error is False):
        # user = Profile.objects.get(user__username__exact=request.user.username)
        all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug)
        user_bonus = user.bonus
        user_balance = user.balance
        user_winnings = user.widhdrawable_balance
        joined_players = all_joined.count()
        contest_name = contest.contest_name
        contest_prize = contest.contest_prize
        contest_fee = contest.contest_fee
        bonus_percent = contest.bonus_percent
        low_balance = 0
        add_money = 0
        winnings_after_deduction = user_winnings
        if contest.bonus_contest is True:
            if user_bonus >= Decimal(round((bonus_percent*contest_fee)/100, 0)):
                deduction_from_bonus = Decimal(round((bonus_percent*contest_fee)/100, 0))
                bonus_balance_after_deduction = user_bonus - deduction_from_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > (user_balance + user_winnings):
                    low_balance = 1
                    print("I am here!")
                    add_money = deduction_from_main - (user_balance + user_winnings)
                    main_balance_after_deduction = 0
                else:
                    if deduction_from_main > user_balance:
                        main_balance_after_deduction = 0
                        winnings_after_deduction = deduction_from_main - user_balance
                    else:
                        main_balance_after_deduction = user_balance - deduction_from_main
                    # main_balance_after_deduction = user_balance - deduction_from_main
            else:
                deduction_from_bonus = user_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                bonus_balance_after_deduction = user_bonus - deduction_from_bonus
                # deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > user_balance + user_winnings:
                    low_balance = 1
                    add_money = deduction_from_main - (user_balance + user_winnings)
                    main_balance_after_deduction = 0
                else:
                    if deduction_from_main > user_balance:
                        main_balance_after_deduction = 0
                        winnings_after_deduction = deduction_from_main - user_balance
                    else:
                        main_balance_after_deduction = user_balance - deduction_from_main
                    # main_balance_after_deduction = user_balance - deduction_from_main
        else:
            deduction_from_bonus = 0
            bonus_balance_after_deduction = user_bonus
            deduction_from_main = contest_fee
            if deduction_from_main > user_balance + user_winnings:
                low_balance = 1
                add_money = deduction_from_main - (user_balance + user_winnings)
                main_balance_after_deduction = 0
            else:
                if deduction_from_main > user_balance:
                    main_balance_after_deduction = 0
                    winnings_after_deduction = deduction_from_main - user_balance
                else:
                    main_balance_after_deduction = user_balance - deduction_from_main
                # main_balance_after_deduction = user_balance - deduction_from_main

        print(user_winnings, user, user_balance, joined_players, contest_name, contest_prize, contest_fee, deduction_from_bonus, deduction_from_main, bonus_balance_after_deduction, main_balance_after_deduction, low_balance, add_money)
        data = {
            'called': "Ok I Got A Call From AJAX to Views",
            'contest_name': contest_name,
            'user_balance': user_balance,
            'user_bonus': user_bonus,
            'user_winnings': user_winnings,
            'joined_players': joined_players,
            'contest_prize': contest_prize,
            'contest_fee': contest_fee,
            'deduction_from_bonus': deduction_from_bonus,
            'deduction_from_main': deduction_from_main,
            'bonus_balance_after_deduction': bonus_balance_after_deduction,
            'main_balance_after_deduction': main_balance_after_deduction,
            'winnings_after_deduction': winnings_after_deduction,
            'low_balance': low_balance,
            'add_money': add_money,
            'match_slug': match_slug,
            'contest_slug': contest_slug,
        }
        print("Data is : ")
        print(data)
        return JsonResponse(data)

    else:
        data = {
            'profile_error': profile_error,
            'multiple_entry_error': multiple_entry_error,
            'log_in_error': log_in_error,
            'contest_error': contest_error,
            "already_joined_or_filled": already_joined_or_filled,
        }
        return JsonResponse(data)


@login_required(login_url='IndexView')
def RankingPreviewTeam(request, team_no, team_name, match_slug):
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    try:
        if match_obj.first().match_tick > time.time():
            return redirect('/cricket_center/')
    except:
        print("From Except")
        return redirect('/cricket_center/')
    model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    model_is = apps.get_registered_model('cricket_center', model_name)
    team_to_preview = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=team_name, team_no=team_no).first()
    team_dict = model_to_dict(team_to_preview)
    # total_batsmen_in_team = team_dict.total_batsmen
    # total_allrounders_in_team = team_dict.total_allrounders
    # total_bowlers_in_team = team_dict.total_bowlers
    data = {
        # "total_batsmen_in_team": total_batsmen_in_team,
        # "total_allrounders_in_team": total_allrounders_in_team,
        # "total_bowlers_in_team": total_bowlers_in_team,
    }
    for key in team_dict:
        print(key)
        print(team_dict[key])
        if type(team_dict[key]) == str:
            data.update({key: team_dict[key].title().replace("_", " ")})
        else:
            data.update({key: team_dict[key]})
    # player_points_dict = {}
    # match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    # for player in PlayerDetail.objects.filter(Q(player_current_team__exact=match_obj.first().short_team_one) | Q(player_current_team__exact=match_obj.first().short_team_two)):
    #     player_points_dict[player.player_name] = player.current_points
    # index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # players_key = ["Keeper", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10", "Player11"]
    # print(index, players_key)
    # model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    # model_is = apps.get_registered_model('cricket_center', model_name)
    # team_to_preview = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=team_name, team_no=team_no).first()
    # team_dict = model_to_dict(team_to_preview)
    # total_batsmen_in_team = team_dict['total_batsmen']
    # total_allrounders_in_team = team_dict['total_allrounders']
    # total_bowlers_in_team = team_dict['total_bowlers']
    # data = {
    #     "captain": team_dict["Captain"].title().replace("_", " "),
    #     "vice": team_dict["Vice_Captain"].title().replace("_", " "),
    # }
    # data.update({"keeper": team_dict["Keeper"].title().replace("_", " ")})
    # data.update({"keeper_points": team_dict["Keeper_Points"]})
    # data.update({"captain_points": team_dict["Captain_Points"] * Decimal(2)})
    # print(player_points_dict[team_dict["Vice_Captain"].title()])
    # data.update({"vice_points": round(team_dict["Vice_Captain"] * Decimal(1.5), 2)})
    # for i in range(2, total_batsmen_in_team + 2):
    #     key = "bat" + str(i - 1)
    #     key_points = "bat" + str(i - 1) + "_points"
    #     data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
    #     data.update({key_points: player_points_dict[team_dict[players_key[index[0]]].title()]})
    #     players_key.pop(0)

    # for i in range(2 + total_batsmen_in_team, total_batsmen_in_team + total_allrounders_in_team + 2):
    #     key = "allrounder" + str(i - 1)
    #     key_points = "allrounder" + str(i - 1) + "_points"
    #     data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
    #     data.update({key_points: player_points_dict[team_dict[players_key[index[0]]].title()]})
    #     players_key.pop(0)

    # for i in range(2 + total_batsmen_in_team + total_allrounders_in_team, total_batsmen_in_team + total_allrounders_in_team + total_bowlers_in_team + 2):
    #     key = "bowl" + str(i - 1)
    #     key_points = "bowl" + str(i - 1) + "_points"
    #     data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
    #     data.update({key_points: player_points_dict[team_dict[players_key[index[0]]].title()]})
    #     players_key.pop(0)

    # data.update({"keeper_count": 1})
    # data.update({"bat_count": total_batsmen_in_team})
    # data.update({"allrounder_count": total_allrounders_in_team})
    # data.update({"bowl_count": total_bowlers_in_team})
    return JsonResponse(data)


@login_required(login_url='IndexView')
def PreviewTeam(request, team, match_slug):
    print("Hello")
    print(team, match_slug)
    index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    players_key = ["Keeper", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10", "Player11"]
    print(index, players_key)
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    print(match_obj)
    model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    model_is = apps.get_registered_model('cricket_center', model_name)
    team_to_preview = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=request.user.username, team_no=team).first()
    team_dict = model_to_dict(team_to_preview)
    total_batsmen_in_team = team_dict['total_batsmen']
    total_allrounders_in_team = team_dict['total_allrounders']
    total_bowlers_in_team = team_dict['total_bowlers']
    data = {
        "captain": team_dict["Captain"].title().replace("_", " "),
        "vice": team_dict["Vice_Captain"].title().replace("_", " "),
    }
    data.update({"keeper": team_dict["Keeper"].title().replace("_", " ")})
    for i in range(2, total_batsmen_in_team + 2):
        key = "bat" + str(i - 1)
        data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
        players_key.pop(0)

    for i in range(2 + total_batsmen_in_team, total_batsmen_in_team + total_allrounders_in_team + 2):
        key = "allrounder" + str(i - 1)
        data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
        players_key.pop(0)

    for i in range(2 + total_batsmen_in_team + total_allrounders_in_team, total_batsmen_in_team + total_allrounders_in_team + total_bowlers_in_team + 2):
        key = "bowl" + str(i - 1)
        data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
        players_key.pop(0)

    data.update({"keeper_count": 1})
    data.update({"bat_count": total_batsmen_in_team})
    data.update({"allrounder_count": total_allrounders_in_team})
    data.update({"bowl_count": total_bowlers_in_team})
    return JsonResponse(data)


@login_required(login_url='IndexView')
def TeamEdit(request, team, match_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    team_one = match_obj.short_team_one
    team_two = match_obj.short_team_two
    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    else:
        keepers_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Keeper')).order_by('-player_credit_points')
        batsmen_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Batsman')).order_by('-player_credit_points')
        allrounders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Allrounder')).order_by('-player_credit_points')
        bowlers_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Bowler')).order_by('-player_credit_points')
        team_edited = False
        user_teams_obj = None
        players_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two))
        team_one = match_obj.short_team_one
        team_two = match_obj.short_team_two
        keeper_form = CreateTeamKeeperForm(kqs=keepers_obj)
        batsmen_form = CreateTeamBatsmenForm(bqs=batsmen_obj)
        allrounders_form = CreateTeamAllroundersForm(aqs=allrounders_obj)
        bowlers_form = CreateTeamBowlersForm(bqs=bowlers_obj)
        if request.method == 'POST':
            team_one = match_obj.short_team_one
            team_two = match_obj.short_team_two
            print(team_one, team_two)
            keeper_form = CreateTeamKeeperForm(data=request.POST,kqs=keepers_obj)
            batsmen_form = CreateTeamBatsmenForm(data=request.POST,bqs=batsmen_obj)
            allrounders_form = CreateTeamAllroundersForm(data=request.POST,aqs=allrounders_obj)
            bowlers_form = CreateTeamBowlersForm(data=request.POST,bqs=bowlers_obj)

            print(request.POST.get("captain"))
            print(request.POST.get("vice"))
            if request.method == 'POST':
                team_one = match_obj.short_team_one
                team_two = match_obj.short_team_two
                print(team_one, team_two)
                keeper_form = CreateTeamKeeperForm(data=request.POST,kqs=keepers_obj)
                batsmen_form = CreateTeamBatsmenForm(data=request.POST,bqs=batsmen_obj)
                allrounders_form = CreateTeamAllroundersForm(data=request.POST,aqs=allrounders_obj)
                bowlers_form = CreateTeamBowlersForm(data=request.POST,bqs=bowlers_obj)
                print("Yes I executed 1")
                if keeper_form.is_valid() and batsmen_form.is_valid() and allrounders_form.is_valid() and bowlers_form.is_valid():
                    print("I am Valid Tpp")
                    print(request.POST.get("captain"))
                    print(request.POST.get("vice"))

                    model_name = match_obj.team_one + match_obj.team_two + "Team"
                    model_is = apps.get_registered_model('cricket_center', model_name)

                    user_teams_obj = model_is.objects.filter(username_of_player__exact=request.user.username)
                    Keeper_Dict = list(keeper_form.cleaned_data.keys())[list(keeper_form.cleaned_data.values()).index(True)]
                    Selected_Keeper = Keeper_Dict
                    Selected_Batsmen = [k for k, v in batsmen_form.cleaned_data.items() if v is True]
                    Selected_Allrounders = [k for k, v in allrounders_form.cleaned_data.items() if v is True]
                    Selected_Bowlers = [k for k, v in bowlers_form.cleaned_data.items() if v is True]
                    list_of_players = []
                    list_of_players = [str(Selected_Keeper)] + list_of_players
                    for Batsman in Selected_Batsmen:
                        list_of_players.append(str(Batsman))

                    for Allrounder in Selected_Allrounders:
                        list_of_players.append(str(Allrounder))

                    for Bowler in Selected_Bowlers:
                        list_of_players.append(str(Bowler))

                    print(list_of_players)

                    if len(list_of_players) != 11:
                        try:
                            raise forms.ValidationError('Please Select only 11 Players')
                        except forms.ValidationError as e:
                            keeper_form.add_error(None, e)
                            return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_edited': team_edited})

                    if request.POST.get("captain") is None or request.POST.get("captain") not in list_of_players or request.POST.get("captain") is "off":
                        try:

                            raise forms.ValidationError('Please Select your Captain')
                        except forms.ValidationError as e:
                            keeper_form.add_error(None, e)
                            return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_edited': team_edited})

                    if request.POST.get("vice") is None or request.POST.get("vice") not in list_of_players or request.POST.get("captain") is "off":
                        try:
                            raise forms.ValidationError('Please Select your Vice Captain')
                        except forms.ValidationError as e:
                            keeper_form.add_error(None, e)
                            return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_edited': team_edited})
                    print(request.POST.get("captain"))
                    model_name = match_obj.team_one + match_obj.team_two + "Team"
                    model_is = apps.get_registered_model('cricket_center', model_name)
                    team_to_edit = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=request.user.username, team_no=team).first()
                    print("Keeper : " + team_to_edit.Keeper)
                    print(request.POST.get("total_credits_points"))
                    team_to_edit.Keeper = list_of_players[0]
                    team_to_edit.Player2 = list_of_players[1]
                    team_to_edit.Player3 = list_of_players[2]
                    team_to_edit.Player4 = list_of_players[3]
                    team_to_edit.Player5 = list_of_players[4]
                    team_to_edit.Player6 = list_of_players[5]
                    team_to_edit.Player7 = list_of_players[6]
                    team_to_edit.Player8 = list_of_players[7]
                    team_to_edit.Player9 = list_of_players[8]
                    team_to_edit.Player10 = list_of_players[9]
                    team_to_edit.Player11 = list_of_players[10]
                    team_to_edit.Captain = request.POST.get("captain")
                    team_to_edit.Vice_Captain = request.POST.get("vice")
                    team_to_edit.total_batsmen = len(Selected_Batsmen)
                    team_to_edit.total_allrounders = len(Selected_Allrounders)
                    team_to_edit.total_bowlers = len(Selected_Bowlers)
                    team_to_edit.total_credits_used = request.POST.get("total_credits_points")
                    team_to_edit.save()
                    team_edited = True
                    return HttpResponseRedirect('/cricket_center/match' + '/' + match_slug)
        return render(request, 'cricket_center/edit_team.html', {"match_slug": match_slug, 'team': team, 'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_edited': team_edited, 'user_teams_obj': user_teams_obj, 'team_one': team_one, 'team_two': team_two})


@login_required(login_url='IndexView')
def CreateTeamView(request, match_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    team_one = match_obj.short_team_one
    team_two = match_obj.short_team_two
    if match_obj.match_tick < time.time():
        return redirect(reverse('cricket_center:match_live', kwargs={'match_slug': match_slug}))
    else:
        keepers_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Keeper')).order_by('-player_credit_points')
        batsmen_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Batsman')).order_by('-player_credit_points')
        allrounders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Allrounder')).order_by('-player_credit_points')
        bowlers_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Bowler')).order_by('-player_credit_points')
        match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
        players_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.first().short_team_one) | Q(player_current_team=match_obj.first().short_team_two))
        print(players_obj)
        team_created = False
        user_teams_obj = None
        team_one = match_obj.first().short_team_one
        team_two = match_obj.first().short_team_two
        keeper_form = CreateTeamKeeperForm(kqs=keepers_obj)
        batsmen_form = CreateTeamBatsmenForm(bqs=batsmen_obj)
        allrounders_form = CreateTeamAllroundersForm(aqs=allrounders_obj)
        bowlers_form = CreateTeamBowlersForm(bqs=bowlers_obj)
        if request.method == 'POST':
            team_one = match_obj.first().short_team_one
            team_two = match_obj.first().short_team_two
            print(team_one, team_two)
            keeper_form = CreateTeamKeeperForm(data=request.POST,kqs=keepers_obj)
            batsmen_form = CreateTeamBatsmenForm(data=request.POST,bqs=batsmen_obj)
            allrounders_form = CreateTeamAllroundersForm(data=request.POST,aqs=allrounders_obj)
            bowlers_form = CreateTeamBowlersForm(data=request.POST,bqs=bowlers_obj)
            if keeper_form.is_valid() and batsmen_form.is_valid() and allrounders_form.is_valid() and bowlers_form.is_valid():
                model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
                model_is = apps.get_registered_model('cricket_center', model_name)
                user_teams_obj = model_is.objects.filter(username_of_player__exact=request.user.username)
                if user_teams_obj.count() < 3:
                    new_team_no = user_teams_obj.count() + 1
                    for obj in user_teams_obj:
                        if obj.team_no == new_team_no:
                            new_team_no = new_team_no + 1
                else:
                    return HttpResponse("Maximum reched out")
                total_sallery = Decimal(request.POST.get("total_credits_points"))
                print("Print ME")
                print(type(total_sallery))
                Keeper_Dict = list(keeper_form.cleaned_data.keys())[list(keeper_form.cleaned_data.values()).index(True)]
                Selected_Keeper = Keeper_Dict
                Selected_Batsmen = [k for k, v in batsmen_form.cleaned_data.items() if v is True]
                Selected_Allrounders = [k for k, v in allrounders_form.cleaned_data.items() if v is True]
                Selected_Bowlers = [k for k, v in bowlers_form.cleaned_data.items() if v is True]
                list_of_players = []
                list_of_players = [str(Selected_Keeper)] + list_of_players
                for Batsman in Selected_Batsmen:
                    list_of_players.append(str(Batsman))

                for Allrounder in Selected_Allrounders:
                    list_of_players.append(str(Allrounder))

                for Bowler in Selected_Bowlers:
                    list_of_players.append(str(Bowler))

                print(list_of_players)

                if len(list_of_players) != 11:
                    try:
                        raise forms.ValidationError('Please Select only 11 Players')
                    except forms.ValidationError as e:
                        keeper_form.add_error(None, e)
                        return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})

                if request.POST.get("captain") is None or request.POST.get("captain") not in list_of_players or request.POST.get("captain") is "off":
                    try:

                        raise forms.ValidationError('Please Select your Captain')
                    except forms.ValidationError as e:
                        keeper_form.add_error(None, e)
                        return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})

                if request.POST.get("vice") is None or request.POST.get("vice") not in list_of_players or request.POST.get("captain") is "off":
                    try:
                        raise forms.ValidationError('Please Select your Vice Captain')
                    except forms.ValidationError as e:
                        keeper_form.add_error(None, e)
                        return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})
                print(request.POST.get("captain"))
                print(request.POST.get("total_credits_points"))
                print(request.POST)
                model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
                model_is = apps.get_registered_model('cricket_center', model_name)

                team_obj = model_is(
                                                Keeper=list_of_players[0],
                                                Player2=list_of_players[1],
                                                Player3=list_of_players[2],
                                                Player4=list_of_players[3],
                                                Player5=list_of_players[4],
                                                Player6=list_of_players[5],
                                                Player7=list_of_players[6],
                                                Player8=list_of_players[7],
                                                Player9=list_of_players[8],
                                                Player10=list_of_players[9],
                                                Player11=list_of_players[10],
                                                Captain=request.POST.get("captain"),
                                                Vice_Captain=request.POST.get("vice"),
                                                team_no=new_team_no,
                                                username_of_player=request.user.username,
                                                match_slug=match_slug,
                                                total_batsmen=len(Selected_Batsmen),
                                                total_allrounders=len(Selected_Allrounders),
                                                total_bowlers=len(Selected_Bowlers),
                                                total_credits_used=total_sallery,
                                            )
                team_obj.save()
                team_created = True
                return HttpResponseRedirect('/cricket_center/match' + '/' + match_slug)
        return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created, 'user_teams_obj': user_teams_obj, 'team_one': team_one, 'team_two': team_two})


def GetTeamInfo(request, team, match_slug):
    print(team, match_slug)
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    model_is = apps.get_registered_model('cricket_center', model_name)
    team_to_preview = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=request.user.username, team_no=team).first()
    team_dict = model_to_dict(team_to_preview)
    total_batsmen_in_team = team_dict['total_batsmen']
    total_allrounders_in_team = team_dict['total_allrounders']
    total_bowlers_in_team = team_dict['total_bowlers']
    total_credits_points = team_dict['total_credits_used']
    team_captain = team_dict['Captain']
    team_vice = team_dict['Vice_Captain']
    data = {
        "team": team,
        "team_captain": team_captain,
        "team_vice": team_vice,
        "total_batsmen_in_team": total_batsmen_in_team,
        "total_allrounders_in_team": total_allrounders_in_team,
        "total_bowlers_in_team": total_bowlers_in_team,
        "total_credits_points": total_credits_points
    }
    index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    players_key = ["Keeper", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10", "Player11"]
    data.update({"keeper": team_dict["Keeper"].title().replace("_", " ")})
    for i in range(2, total_batsmen_in_team + 2):
        key = "bat" + str(i - 1)
        data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
        players_key.pop(0)

    for i in range(2, total_allrounders_in_team+2):
        key = "allrounder" + str(i - 1)
        data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
        players_key.pop(0)

    for i in range(2, total_bowlers_in_team + 2):
        key = "bowl" + str(i - 1)
        data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
        players_key.pop(0)

    return JsonResponse(data)
