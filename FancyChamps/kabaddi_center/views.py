from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MatchDetail, JoiningDetail, PlayerDetail, ContestDetail, JoiningTransactionDetail, ContestMessages
import time, random, string, operator
from django.apps import apps
from .forms import CreateTeamDefendersForm, CreateTeamRaidersForm, CreateTeamAllroundersForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, reverse
from decimal import Decimal
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from accounts.models import Profile
from collections import OrderedDict


@login_required(login_url='IndexView')
def KabaddiCenterIndexView(request):
    upcomming_match_obj = MatchDetail.objects.filter(match_tick__gte=time.time()).order_by('match_date')
    live_match_obj = MatchDetail.objects.filter(match_tick__lte=time.time(), history_activate=False, live=True).order_by('match_date')
    history_match_obj = MatchDetail.objects.filter(history_activate=True).order_by('-match_tick')
    return render(request, "kabaddi_center/kabaddi_center_index.html", context={'upcomming_match_obj': upcomming_match_obj, "live_match_obj": live_match_obj, "history_match_obj": history_match_obj})


@login_required(login_url='IndexView')
def SingleMatchView(request, match_slug):
    try:
        match_obj = MatchDetail.objects.get(match_slug__exact=match_slug)
    except MatchDetail.DoesNotExist:
        return HttpResponse("Something went Wrong!")
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug).first()
    # if match_obj.match_tick < time.time():
    #     time_over_error = True
    #     return render(request, "kabaddi_center/match.html", context={"time_over_error": time_over_error})

    print(match_obj.match_tick)
    print(time.time())

    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
    else:
        model_name = match_obj.team_one + match_obj.team_two + "Team"
        model_is = apps.get_registered_model('kabaddi_center', model_name)
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
        return render(request, "kabaddi_center/match.html", context={'AllGoesToChampionContests': AllGoesToChampionContests, 'BonusContests': BonusContests, 'FreeRoll':FreeRoll, 'ThreeOnOne':ThreeOnOne, 'OtherContests':OtherContests, 'match_obj': match_obj, 'FourOnOne': FourOnOne, "HeadToHead": HeadToHead, 'EqualContests': EqualContests, 'GreatAndGrand': GreatAndGrand, 'match_slug': match_slug, 'total_teams': total_teams, 'contest_joined': contest_joined, 'all_joined_list': all_joined_list})


@login_required(login_url='IndexView')
def TeamEdit(request, team, match_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    team_one = match_obj.short_team_one
    team_two = match_obj.short_team_two
    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
    else:
        defenders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Defender')).order_by('-player_credit_points')
        raiders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Raider')).order_by('-player_credit_points')
        allrounders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Allrounder')).order_by('-player_credit_points')
        team_edited = False
        user_teams_obj = None
        players_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two))
        team_one = match_obj.short_team_one
        team_two = match_obj.short_team_two
        defenders_form = CreateTeamDefendersForm(dqs=defenders_obj)
        raiders_form = CreateTeamRaidersForm(rqs=raiders_obj)
        allrounders_form = CreateTeamAllroundersForm(aqs=allrounders_obj)
        print(defenders_form)
        if request.method == 'POST':
            team_one = match_obj.short_team_one
            team_two = match_obj.short_team_two
            print(team_one, team_two)
            defenders_form = CreateTeamDefendersForm(data=request.POST,dqs=defenders_obj)
            raiders_form = CreateTeamRaidersForm(data=request.POST,rqs=raiders_obj)
            allrounders_form = CreateTeamAllroundersForm(data=request.POST,aqs=allrounders_obj)
            print(request.POST.get("captain"))
            print(request.POST.get("vice"))
            if request.method == 'POST':
                team_one = match_obj.short_team_one
                team_two = match_obj.short_team_two
                print(team_one, team_two)
                defenders_form = CreateTeamDefendersForm(data=request.POST,dqs=defenders_obj)
                raiders_form = CreateTeamRaidersForm(data=request.POST,rqs=raiders_obj)
                allrounders_form = CreateTeamAllroundersForm(data=request.POST,aqs=allrounders_obj)
                print("Yes I executed 1")
                if defenders_form.is_valid() and raiders_form.is_valid() and allrounders_form.is_valid():
                    print("I am Valid Tpp")
                    print(request.POST.get("captain"))
                    print(request.POST.get("vice"))

                    model_name = match_obj.team_one + match_obj.team_two + "Team"
                    model_is = apps.get_registered_model('kabaddi_center', model_name)

                    user_teams_obj = model_is.objects.filter(username_of_player__exact=request.user.username)
                    # Keeper_Dict = list(defenders_form.cleaned_data.keys())[list(defenders_form.cleaned_data.values()).index(True)]
                    Selected_Keeper = [k for k, v in defenders_form.cleaned_data.items() if v is True]#Keeper_Dict
                    Selected_Batsmen = [k for k, v in raiders_form.cleaned_data.items() if v is True]
                    Selected_Allrounders = [k for k, v in allrounders_form.cleaned_data.items() if v is True]
                    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    def_count = len(Selected_Keeper)
                    raid_count = len(Selected_Batsmen)
                    all_count = len(Selected_Allrounders)
                    list_of_players = []
                    # list_of_players = [str(Selected_Keeper)] + list_of_players
                    for Keeper in Selected_Keeper:
                    	list_of_players.append(str(Keeper))

                    for Batsman in Selected_Batsmen:
                        list_of_players.append(str(Batsman))

                    for Allrounder in Selected_Allrounders:
                        list_of_players.append(str(Allrounder))
                    print(list_of_players)
                    print(len(list_of_players))
                    if len(list_of_players) != 7:
                        try:
                            raise forms.ValidationError('Please Select only 7 Players')
                        except forms.ValidationError as e:
                            defenders_form.add_error(None, e)
                            return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_edited': team_edited})

                    if request.POST.get("captain") is None or request.POST.get("captain") not in list_of_players or request.POST.get("captain") is "off":
                        try:

                            raise forms.ValidationError('Please Select your Captain')
                        except forms.ValidationError as e:
                            defenders_form.add_error(None, e)
                            return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_edited': team_edited})

                    if request.POST.get("vice") is None or request.POST.get("vice") not in list_of_players or request.POST.get("captain") is "off":
                        try:
                            raise forms.ValidationError('Please Select your Vice Captain')
                        except forms.ValidationError as e:
                            defenders_form.add_error(None, e)
                            return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_edited': team_edited})
                    print(request.POST.get("captain"))
                    model_name = match_obj.team_one + match_obj.team_two + "Team"
                    model_is = apps.get_registered_model('kabaddi_center', model_name)
                    team_to_edit = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=request.user.username, team_no=team).first()
                    print("Keeper : " + team_to_edit.Player1)
                    print(request.POST.get("total_credits_points"))
                    team_to_edit.Player1 = list_of_players[0]
                    team_to_edit.Player2 = list_of_players[1]
                    team_to_edit.Player3 = list_of_players[2]
                    team_to_edit.Player4 = list_of_players[3]
                    team_to_edit.Player5 = list_of_players[4]
                    team_to_edit.Player6 = list_of_players[5]
                    team_to_edit.Player7 = list_of_players[6]
                    team_to_edit.Captain = request.POST.get("captain")
                    team_to_edit.Vice_Captain = request.POST.get("vice")
                    team_to_edit.total_raiders = raid_count
                    team_to_edit.total_defenders = def_count
                    team_to_edit.total_allrounders = all_count
                    team_to_edit.total_credits_used = request.POST.get("total_credits_points")
                    team_to_edit.save()
                    team_edited = True
                    print(team_to_edit.total_allrounders, team_to_edit.total_raiders, team_to_edit.total_defenders)
                    return HttpResponseRedirect('/kabaddi_center/match' + '/' + match_slug)
        return render(request, 'kabaddi_center/edit_team.html', {"team_one": team_one, "team_two":team_two, "match_slug": match_slug, 'team': team, 'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_edited': team_edited, 'user_teams_obj': user_teams_obj})


def GetTeamInfo(request, team, match_slug):
    print(team, match_slug)
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    model_is = apps.get_registered_model('kabaddi_center', model_name)
    team_to_preview = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=request.user.username, team_no=team).first()
    team_dict = model_to_dict(team_to_preview)
    total_defenders_in_team = team_dict['total_defenders']
    total_allrounders_in_team = team_dict['total_allrounders']
    total_raiders_in_team = team_dict['total_raiders']
    total_credits_points = team_dict['total_credits_used']
    team_captain = team_dict['Captain']
    team_vice = team_dict['Vice_Captain']
    print("////////////////////////////////////////")
    print(team_dict)
    data = {
        "team": team,
        "team_captain": team_captain,
        "team_vice": team_vice,
        "total_raiders_in_team": total_raiders_in_team,
        "total_allrounders_in_team": total_allrounders_in_team,
        "total_defenders_in_team": total_defenders_in_team,
        "total_credits_points": total_credits_points
    }
    index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    players_key = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7"]
    # data.update({"keeper": team_dict["Keeper"].title().replace("_", " ")})
    print("??????????????????????????????")
    print(total_defenders_in_team, total_allrounders_in_team, total_raiders_in_team)
    for i in range(0, total_defenders_in_team):
        key = "def" + str(i + 1)
        data.update({key: team_dict[players_key[0]].title().replace("_", " ")})
        print("def")
        players_key.pop(0)
        print(players_key)

    for i in range(0, total_raiders_in_team):
        key = "raider" + str(i + 1)
        data.update({key: team_dict[players_key[0]].title().replace("_", " ")})
        players_key.pop(0)
        print(players_key)

    for i in range(0, total_allrounders_in_team):
        key = "allrounder" + str(i + 1)
        data.update({key: team_dict[players_key[0]].title().replace("_", " ")})
        players_key.pop(0)
        print(players_key)

    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(data)


    # for i in range(2, total_raiders_in_team + 2):
    #     key = "bat" + str(i - 1)
    #     data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
    #     players_key.pop(0)

    # for i in range(2, total_allrounders_in_team+2):
    #     key = "allrounder" + str(i - 1)
    #     data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
    #     players_key.pop(0)

    # for i in range(2, total_bowlers_in_team + 2):
    #     key = "bowl" + str(i - 1)
    #     data.update({key: team_dict[players_key[index[0]]].title().replace("_", " ")})
    #     players_key.pop(0)

    return JsonResponse(data)


@login_required(login_url='IndexView')
def CreateTeamView(request, match_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    team_one = match_obj.short_team_one
    team_two = match_obj.short_team_two
    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
    else:
        defenders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Defender')).order_by('-player_credit_points')
        raiders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Raider')).order_by('-player_credit_points')
        allrounders_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.short_team_one) | Q(player_current_team=match_obj.short_team_two), Q(player_type='Allrounder')).order_by('-player_credit_points')
        match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
        players_obj = PlayerDetail.objects.filter(Q(player_current_team=match_obj.first().short_team_one) | Q(player_current_team=match_obj.first().short_team_two))
        print(raiders_obj)
        team_created = False
        user_teams_obj = None
        team_one = match_obj.first().short_team_one
        team_two = match_obj.first().short_team_two
        defenders_form = CreateTeamDefendersForm(dqs=defenders_obj)
        raiders_form = CreateTeamRaidersForm(rqs=raiders_obj)
        print(raiders_form)
        allrounders_form = CreateTeamAllroundersForm(aqs=allrounders_obj)
        if request.method == 'POST':
            team_one = match_obj.first().short_team_one
            team_two = match_obj.first().short_team_two
            print(team_one, team_two)
            defenders_form = CreateTeamDefendersForm(data=request.POST,dqs=defenders_obj)
            raiders_form = CreateTeamRaidersForm(data=request.POST,rqs=raiders_obj)
            allrounders_form = CreateTeamAllroundersForm(data=request.POST,aqs=allrounders_obj)
            if defenders_form.is_valid() and raiders_form.is_valid() and allrounders_form.is_valid():
                model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
                model_is = apps.get_registered_model('kabaddi_center', model_name)
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
                # Keeper_Dict = list(defenders_form.cleaned_data.keys())[list(defenders_form.cleaned_data.values()).index(True)]
                Selected_Keeper = [k for k, v in defenders_form.cleaned_data.items() if v is True]
                Selected_Batsmen = [k for k, v in raiders_form.cleaned_data.items() if v is True]
                Selected_Allrounders = [k for k, v in allrounders_form.cleaned_data.items() if v is True]
                print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                print(Selected_Keeper)
                print(Selected_Batsmen)
                print(Selected_Allrounders)
                list_of_players = []
                for Keeper in Selected_Keeper:
                    list_of_players.append(str(Keeper))

                for Batsman in Selected_Batsmen:
                    list_of_players.append(str(Batsman))

                for Allrounder in Selected_Allrounders:
                    list_of_players.append(str(Allrounder))
                print(list_of_players)
                print(len(list_of_players))

                if len(list_of_players) != 7:
                    try:
                        raise forms.ValidationError('Please Select only 7 Players')
                    except forms.ValidationError as e:
                        defenders_form.add_error(None, e)
                        return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_created': team_created})

                if request.POST.get("captain") is None or request.POST.get("captain") not in list_of_players or request.POST.get("captain") is "off":
                    try:

                        raise forms.ValidationError('Please Select your Captain')
                    except forms.ValidationError as e:
                        defenders_form.add_error(None, e)
                        return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_created': team_created})

                if request.POST.get("vice") is None or request.POST.get("vice") not in list_of_players or request.POST.get("captain") is "off":
                    try:
                        raise forms.ValidationError('Please Select your Vice Captain')
                    except forms.ValidationError as e:
                        defenders_form.add_error(None, e)
                        return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_created': team_created})
                print(request.POST.get("captain"))
                print(request.POST.get("total_credits_points"))
                print(request.POST)
                model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
                model_is = apps.get_registered_model('kabaddi_center', model_name)
                print("**********************************************************************")
                print(len(Selected_Keeper), len(Selected_Allrounders), len(Selected_Batsmen))
                team_obj = model_is(
                                                Player1=list_of_players[0],
                                                Player2=list_of_players[1],
                                                Player3=list_of_players[2],
                                                Player4=list_of_players[3],
                                                Player5=list_of_players[4],
                                                Player6=list_of_players[5],
                                                Player7=list_of_players[6],
                                                Captain=request.POST.get("captain"),
                                                Vice_Captain=request.POST.get("vice"),
                                                team_no=new_team_no,
                                                username_of_player=request.user.username,
                                                match_slug=match_slug,
                                                total_defenders=len(Selected_Keeper),
                                                total_allrounders=len(Selected_Allrounders),
                                                total_raiders=len(Selected_Batsmen),
                                                total_credits_used=total_sallery,
                                            )
                team_obj.save()
                print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
                print(team_obj)
                team_created = True
                return HttpResponseRedirect('/kabaddi_center/match' + '/' + match_slug)
        return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'defenders_form': defenders_form, 'allrounders_form': allrounders_form, 'raiders_form': raiders_form, 'team_created': team_created, 'user_teams_obj': user_teams_obj, 'team_one': team_one, 'team_two': team_two})


@login_required(login_url='IndexView')
def MyTeams(request, match_slug):
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug).first()
    model_name = match_obj.team_one + match_obj.team_two + "Team"
    model_is = apps.get_registered_model('kabaddi_center', model_name)
    my_teams = model_is.objects.filter(username_of_player__exact=request.user.username)
    return render(request, "kabaddi_center/my_teams.html", context={'match_slug': match_slug, 'my_teams': my_teams, 'match_obj': match_obj})


@login_required(login_url='IndexView')
def PreviewTeam(request, team, match_slug):
    index = [1, 2, 3, 4, 5, 6, 7]
    players_key = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7"]
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    model_is = apps.get_registered_model('kabaddi_center', model_name)
    team_to_preview = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=request.user.username, team_no=team).first()
    team_dict = model_to_dict(team_to_preview)
    total_defenders_in_team = team_dict['total_defenders']
    total_allrounders_in_team = team_dict['total_allrounders']
    total_raiders_in_team = team_dict['total_raiders']
    data = {
        "captain": team_dict["Captain"].title().replace("_", " "),
        "vice": team_dict["Vice_Captain"].title().replace("_", " "),
    }
    # data.update({"keeper": team_dict["Keeper"].title().replace("_", " ")})
    for i in range(0, total_defenders_in_team):
        key = "def" + str(i + 1)
        print(i)
        print(team_dict[players_key[0]])
        data.update({key: team_dict[players_key[0]].title().replace("_", " ")})
        players_key.pop(0)
        print(players_key)

    for i in range(total_defenders_in_team + total_allrounders_in_team, (total_defenders_in_team + total_raiders_in_team + total_allrounders_in_team)):
        key = "raider" + str(i + 1)
        print("ra")
        print(i)
        print(team_dict[players_key[0]])
        data.update({key: team_dict[players_key[0]].title().replace("_", " ")})
        players_key.pop(0)
        print(players_key)

    for i in range((total_defenders_in_team), (total_defenders_in_team + total_allrounders_in_team)):
        key = "allrounder" + str(i + 1)
        print("aa")
        print(i)
        print(team_dict[players_key[0]])
        data.update({key: team_dict[players_key[0]].title().replace("_", " ")})
        players_key.pop(0)
        print(players_key)

    data.update({"def_count": total_defenders_in_team})
    data.update({"allrounder_count": total_allrounders_in_team})
    data.update({"raider_count": total_raiders_in_team})
    return JsonResponse(data)


@login_required(login_url='IndexView')
def ContestJoinNow(request, match_slug, contest_slug):
    print("He got the whole world!")
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
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
def PayAndJoin(request):
    error = False
    log_in_error = False
    contest_error = False
    match_slug = request.POST.get('match_slug')
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
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
def JoinedContests(request, match_slug):
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    match_obj = match_objs.first()
    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
    match_objs = MatchDetail.objects.filter(match_slug__exact=match_slug)
    model_name = match_objs.first().team_one + match_objs.first().team_two + "Team"
    model_is = apps.get_registered_model('kabaddi_center', model_name)
    match_obj = match_objs.first()
    all_joined = JoiningDetail.objects.filter(Q(joined_user__exact=request.user.username), Q(match_slug__exact=match_obj.match_slug))
    contests_joined = []
    for contest in all_joined:
        contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest.joined_contest_slug)
        if contest_obj not in contests_joined:
            contests_joined.append(contest_obj)
    total_teams = model_is.objects.filter(username_of_player__exact=request.user.username)
    contests_count = len(contests_joined)
    return render(request, "kabaddi_center/joined_contests.html", context={'contests_joined': contests_joined, 'match_slug': match_slug, 'contests_count': contests_count, 'total_teams': total_teams, 'match_obj': match_obj})


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


@login_required(login_url='IndexView')
def ContestsViews(request, match_slug, contest_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest_slug)
    print("I got exe")
    if match_obj.match_tick < time.time():
        return redirect(reverse('kabaddi_center:match_live', kwargs={'match_slug': match_slug}))
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points')
    for ranker in all_joined:
        ranker.rank = 1
        ranker.save()
    return render(request, "kabaddi_center/view_contest.html", context={"match_obj": match_obj, "all_joined_with_ranking": all_joined, "contest_obj": contest_obj})


@login_required(login_url='IndexView')
def RankingPreviewTeam(request, team_no, team_name, match_slug):
    match_obj = MatchDetail.objects.filter(match_slug__exact=match_slug)
    try:
        if match_obj.first().match_tick > time.time():
            return redirect('/kabaddi_center/')
    except:
        print("From Except")
        return redirect('/kabaddi_center/')
    model_name = match_obj.first().team_one + match_obj.first().team_two + "Team"
    model_is = apps.get_registered_model('kabaddi_center', model_name)
    team_to_preview = model_is.objects.filter(match_slug__exact=match_slug, username_of_player__exact=team_name, team_no=team_no).first()
    team_dict = model_to_dict(team_to_preview)

    data = {
        # "total_batsmen_in_team": total_batsmen_in_team,
        # "total_allrounders_in_team": total_allrounders_in_team,
        # "total_bowlers_in_team": total_bowlers_in_team,
    }
    for key in team_dict:
        if type(team_dict[key]) == str:
            data.update({key: team_dict[key].title().replace("_", " ")})
        else:
            data.update({key: team_dict[key]})
    return JsonResponse(data)


@login_required(login_url='IndexView')
def SingleMatchLiveView(request, match_slug):
    all_joined = JoiningDetail.objects.filter(joined_user__exact=request.user.username, match_slug__exact=match_slug)
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    if match_obj.match_tick > time.time():
        return redirect('/kabaddi_center/')
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
        return render(request, "kabaddi_center/live_match.html", context={"match_slug": match_slug, "contests_joined": contests_joined, "match_obj": match_obj, "contests_count":contests_count,})


@login_required(login_url='IndexView')
def ContestsRankings(request, match_slug, contest_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    messages_of_contest = ContestMessages.objects.filter(contest_slug__exact=contest_slug)
    if match_obj.match_tick > time.time():
        return redirect('/kabaddi_center/')
    else:
        contest_obj = get_object_or_404(ContestDetail, contest_slug__exact=contest_slug)
        all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug).order_by('-total_team_points', 'pk')
        user_teams_list = []
        for i in all_joined:
            if(i.joined_user==request.user.username):
                user_teams_list.append(i)
        return render(request, "kabaddi_center/rankings.html", context={"messages":messages_of_contest.count, "match_obj": match_obj, "all_joined_with_ranking": all_joined, "contest_obj": contest_obj, "user":request.user.username, "user_teams_list":user_teams_list})


def MessageCreateShow(request):
    messages={
        "1": "Hello!","2": "Hi!","3": "Good Bye.","4": "Nice to Meet you!","5": "Good Luck!","6": "I Won!",
        "7":"I Lose!","8":"Too Close.","9":"Well Played!","10":"Same Captain!","11":"#LetsBeTheChampsTogether",
        }
    contest_slug = request.GET.get('slug')
    print("1111111111111111111111111111111")
    print(contest_slug)
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


@login_required(login_url='IndexView')
def SingleMatchHistoryView(request, match_slug):
    all_joined = JoiningDetail.objects.filter(joined_user__exact=request.user.username, match_slug__exact=match_slug)
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
    if match_obj.match_tick > time.time() or (not match_obj.history_activate):
        return redirect('/kabaddi_center/')
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
        return render(request, "kabaddi_center/match_his.html", context={"match_slug": match_slug, "contests_joined": contests_joined, "match_obj": match_obj,"contests_count":contests_count})
