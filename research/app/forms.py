from django import forms
from .models import Publication


class AddResearchForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
