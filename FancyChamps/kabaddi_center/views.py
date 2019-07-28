from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MatchDetail, JoiningDetail, PlayerDetail
import time
from django.apps import apps
from .forms import CreateTeamKeeperForm, CreateTeamBatsmenForm, CreateTeamAllroundersForm, CreateTeamBowlersForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, reverse
# Create your views here.


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
def CreateTeamView(request, match_slug):
    match_obj = get_object_or_404(MatchDetail, match_slug__exact=match_slug)
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
        return render(request, 'kabaddi_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created, 'user_teams_obj': user_teams_obj})
