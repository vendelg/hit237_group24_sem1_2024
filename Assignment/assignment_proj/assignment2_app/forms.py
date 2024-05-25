from django import forms
from .models import*

#For authenticating login

from django.contrib.auth.forms import AuthenticationForm

from assignment2_app.models import Accounts, ThesisApplication
from django.contrib.auth import authenticate

from django import forms
from django.forms.widgets import PasswordInput, TextInput


class ThesisForm(forms.ModelForm):
  class Meta:
    model = Project
    
    exclude = []
    
    labels = {
      'tid': 'Thesis ID',
      'desc': 'Description',
      'sup_name': 'Supervisor'
    }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())

class AccAuthForm(forms.ModelForm):

    password = forms.CharField(label = "Password", widget=forms.PasswordInput)
    class Meta:

        model = Accounts
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email, password = password):
                raise forms.ValidationError("Incorrect Username or Password")
            
class ApplicationForm(forms.ModelForm):
  class Meta:
    model = ThesisApplication

    fields = ['ThesisID', 'GroupNumber', 'StudentID']

    labels = {'ThesisID' : 'Thesis ID', 'GroupNumber' : 'Group Number', 'StudentID' : 'Student ID'}