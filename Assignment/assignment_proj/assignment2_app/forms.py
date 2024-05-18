from django import forms
from .models import*

class ThesisForm(forms.ModelForm):
  class Meta:
    model = Project
    
    exclude = []
    
    labels = {
      'desc': 'Description',
      'sup_name': 'Supervisor'
    }