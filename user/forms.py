from django import forms
from django.contrib.auth import get_user_model
from music.models import *
from user.models import My_list,Myusers,My_favorite
Myuser = get_user_model()

class Reg_form(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ('username', 'email', 'password')
        widgets = {
            'password':forms.PasswordInput(),
            'email':forms.EmailInput()
        }
class Login_form(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(), required=True)

class Usercommentsform(forms.ModelForm):
    class Meta:
        model = Usermoviecomments
        fields = ('user', 'music', 'context')

class Mylistform(forms.ModelForm):
    class Meta:
        model = My_list
        fields = ('user_id','music_id')

class Myfavorlistform(forms.ModelForm):
    class Meta:
        model = My_favorite
        fields = ('user_id','music_id')