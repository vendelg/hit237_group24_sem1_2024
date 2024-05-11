from django import forms
from .models import*

class ThesisForm(forms.ModelForm):
  class Meta:
    model = TestThesis
    
    exclude = []
    
    labels = {
      'desc': 'Description',
      'sup_name': 'Supervisor'
    }