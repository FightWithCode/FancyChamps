from django import forms
from .models import SupportQueries


class SupportQuerriesForm(forms.ModelForm):
    user = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = SupportQueries
        fields = ["user","email", "mobile_no", "question", "brief_description"]
    
    def clean_email(self, *args, **kwargs):
        print("I am getting called")
        email = self.cleaned_data["email"]
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Please provide a valild Gmail Account.")
        return email
    
    def clean_mobile_no(self, *args, **kwargs):
        mobile_no = self.cleaned_data["mobile_no"]
        if not len(str(mobile_no)) == 10:
            raise forms.ValidationError("Please provide a valid Mobile No.")
        return mobile_no
