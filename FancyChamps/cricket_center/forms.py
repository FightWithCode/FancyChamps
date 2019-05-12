from django import forms
from cricket_center.models import PlayerDetail
from django.db.models import Q


class CreateTeamKeeperForm(forms.Form):

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('kqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)
    
    # team_one = ""
    # team_two = ""
    # print("exec")
    # def __init__(self, *args, **kwargs):
    #     team_one = kwargs.pop('team_one', None)
    #     team_two = kwargs.pop('team_two', None)
    #     super().__init__(*args, **kwargs)
    # # keepers = MatchDetail.objects.filter(player_current_team__exact=team_one)
    # plaeyr_obj = PlayerDetail.objects.filter(Q(player_current_team=team_one) | Q(player_current_team=team_two))
    # for player in plaeyr_obj:
    #     if(plaeyr.player_type=='Keeper'):

    #         player.name = forms.BooleanField(required=False, initial=False)
    #         #S_Saha = forms.BooleanField(required=False, initial=False)
    #         #S_Goswami = forms.BooleanField(required=False, initial=False)
        
    # players = forms.ModelMultipleChoiceField(queryset=PlayerDetail.objects.all())

    # def __init__(self, *args, **kwargs):
    #     team_one = kwargs.pop('team_one')
    #     team_two = kwargs.pop('team_two')
    #     super(CreateTeamKeeperForm, self).__init__(*args, **kwargs)
    #     self.fields['players'].queryset = PlayerDetail.objects.filter(Q(player_current_team=team_one) | Q(player_current_team=team_two))

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     true_count = list(cleaned_data.values())
    #     if true_count.count(True) != 1:
    #         raise forms.ValidationError("Please Select only One Keeper.")




class CreateTeamBatsmenForm(forms.Form):

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('bqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)

#     R_Sharma = forms.BooleanField(required=False, initial=False)
#     #K_Williamson = forms.BooleanField(required=False)
#     Surya_K_Yadav = forms.BooleanField(required=False)
#     K_Williamson = forms.BooleanField(required=False)
#     M_Pandey = forms.BooleanField(required=False)
#     K_Pollard = forms.BooleanField(required=False)
#     M_Guptill = forms.BooleanField(required=False)
#     E_Levis = forms.BooleanField(required=False)
#     Y_Singh = forms.BooleanField(required=False)
#     I_Kishan = forms.BooleanField(required=False)
#     Y_Pathan = forms.BooleanField(required=False)
#     D_Hooda = forms.BooleanField(required=False)
#     A_Tare = forms.BooleanField(required=False)
#     Siddhess_Lad = forms.BooleanField(required=False)

#     def clean(self):
#         cleaned_data = self.cleaned_data
#         true_count = list(cleaned_data.values())
#         if true_count.count(True) > 5:
#             raise forms.ValidationError("Only 5 Batsmen are Allowed")
#         elif true_count.count(True) < 3:
#             raise forms.ValidationError("Please, Select at Least 3 Batsmen")


class CreateTeamAllroundersForm(forms.Form):
    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('aqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)
    # H_Pandya = forms.BooleanField(required=False)
    # M_Nabi = forms.BooleanField(required=False)
    # K_Pandya = forms.BooleanField(required=False)
    # B_Cutting = forms.BooleanField(required=False)
    # Abhishek_S = forms.BooleanField(required=False)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     true_count = list(cleaned_data.values())
    #     if true_count.count(True) > 3:
    #         raise forms.ValidationError("Only 3 Allrounder are Allowed")
    #     elif true_count.count(True) < 1:
    #         raise forms.ValidationError("Please, Select at Least 1 Allrounder")


class CreateTeamBowlersForm(forms.Form):
    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('bqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)
    # J_Bumrah = forms.BooleanField(required=False)
    # Rashid_Khan = forms.BooleanField(required=False)
    # L_Malinga = forms.BooleanField(required=False)
    # M_McClenaghan = forms.BooleanField(required=False)
    # R_Chahar = forms.BooleanField(required=False)
    # B_Kumar = forms.BooleanField(required=False)
    # K_Ahmed = forms.BooleanField(required=False)
    # Sandeep_S = forms.BooleanField(required=False)
    # S_Kaul = forms.BooleanField(required=False)
    # Jayant_Yadav = forms.BooleanField(required=False)
    # M_Markande = forms.BooleanField(required=False)
    # B_Saran = forms.BooleanField(required=False)
    # S_Nadeem = forms.BooleanField(required=False)
    # B_Thampi = forms.BooleanField(required=False)
    # T_Natrajan = forms.BooleanField(required=False)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     true_count = list(cleaned_data.values())
    #     if true_count.count(True) > 5:
    #         raise forms.ValidationError("Only 5 Bowlers are Allowed")
    #     elif true_count.count(True) < 3:
    #         raise forms.ValidationError("Please, Select at Least 3 Bowlers")

# class CreateCaptainViceCaptain(forms.Form):
    # Andre_Fletcher = models.CharField(max_length=255, default="{'Picked':False, Player_Id':1, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")  # on/off,
    # Evin_Lewis = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':2, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Andre_Russell = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':3, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Marlon_Samuels = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':4, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Rovman_Powell = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':5, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    #Denesh_Ramdin = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':6, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Carlos_Brathwaite = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':7, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Ashley_Nurse = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':8, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Samuel_Badree = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':9, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Keemo_Paul = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':10, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Kesrick_Williams = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':11, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Chadwick_Walton = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':12, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Sheldon_Cottrell = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':13, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
