from django import forms
from .models import*

#For authenticating login

from django.contrib.auth.forms import AuthenticationForm

from assignment2_app.models import Accounts, ThesisApplication
from django.contrib.auth import authenticate

from django import forms
from django.forms.widgets import PasswordInput, TextInput
<<<<<<< Updated upstream
=======
from .models import notification
from .models import Accounts
from django.contrib.auth.forms import PasswordChangeForm
>>>>>>> Stashed changes



class ThesisForm(forms.ModelForm):
  class Meta:
    model = Project

 

    exclude = ['is_approved', 'is_request',]
    
    labels = {
      'tid': 'Thesis ID',
      'desc': 'Description',
      'sup_name': 'Supervisor',
    }


      

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
            
#Allows Students to apply to forms           



class ApplicationForm(forms.ModelForm):

  
      
  class Meta:

        
    model = ThesisApplication

    fields = ['StudentID']

    labels = {'StudentID' : 'Student ID'}

#Allows Students to register

class StudentForm(forms.ModelForm):
    class Meta:
        model = ()

        fields = ['firstname', 'lastname', 'email', 'password', 'studentid',]

        labels = {'firstname' : 'First Name', 'lastname' : 'Last Name', 'email' : 'Email', 'password' : 'Password', 'studentid' : 'Student ID'}



<<<<<<< Updated upstream
=======
class notificationForm(forms.ModelForm):
    class Meta:
        model = notification
        fields = ['content']

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
>>>>>>> Stashed changes

