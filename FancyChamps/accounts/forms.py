from django import forms
from .models import User, Profile
from FancyChamps import settings

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

        error_messages = {
            'username': {
                'unique': "This username already Exists!"
            },
            'email': {
                'unique': "This email already Exists!"
            }
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email == username:
            raise forms.ValidationError("Email and Username can't be same.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ('phone_number', 'date_of_birth', 'state')


class UserLogInForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = '__all__'

class AddMoneyForm(forms.Form):
    money_to_add = forms.IntegerField(max_value=10000,initial=100)

# from django import forms
# from django.contrib.auth.models import User
# # from accounts.models import UsersProfileInfo


# class UserForm(forms.ModelForm):
#     password = forms.CharField(max_length=64, widget=forms.PasswordInput())

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')


# # class UserProfileInfoForm(forms.ModelForm):
# #     class Meta:
# #         model = UsersProfileInfo
# #         fields = ('phone_number', 'state', 'date_of_birth')


# # class LoginForm(forms.Form):
# #     username = forms.CharField()
# #     password = forms.CharField(widget=PasswordInput())
