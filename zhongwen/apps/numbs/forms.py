from django import forms
from apps.numbs.models import Numb

class NumbForm(forms.ModelForm):
    class Meta:
        model = Numb
        fields = '__all__'
