from django import forms
from calcapp.models import SavedCalc

class SavedCalc(forms.ModelForm):
    class Meta:
        model = SavedCalc
        fields = ('left','operators','right','total','loguser')
