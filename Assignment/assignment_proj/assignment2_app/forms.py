from django import forms
from .models import*

class ThesisForm(forms.ModelForm):
  class Meta:
    model = Project
    
    exclude = []
    
    labels = {
      'tid': 'Thesis ID',
      'desc': 'Description',
      'supName': 'Supervisor'
    }