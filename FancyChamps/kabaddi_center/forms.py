from django import forms
from cricket_center.models import PlayerDetail
from django.db.models import Q


class CreateTeamKeeperForm(forms.Form):

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('kqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)


class CreateTeamBatsmenForm(forms.Form):

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('bqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)


class CreateTeamAllroundersForm(forms.Form):
    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('aqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)


class CreateTeamBowlersForm(forms.Form):
    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('bqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)
