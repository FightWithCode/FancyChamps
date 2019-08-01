from django import forms
from cricket_center.models import PlayerDetail
from django.db.models import Q


class CreateTeamDefendersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('dqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)


class CreateTeamAllroundersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('aqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)


class CreateTeamRaidersForm(forms.Form):
    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('rqs')
        super().__init__(*args, **kwargs)

        for instance in qs:
            self.fields[instance.player_name] = forms.BooleanField(required=False, initial=False)

