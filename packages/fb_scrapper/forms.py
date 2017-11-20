from django import forms
from .models import FacebookAuth, FacebookData


class FbScrapperAuthForm(forms.ModelForm):
    
    class Meta:
        model = FacebookAuth
        fields = ['token', 'app_id', 'app_secret_id']

    def clean(self):
        # no space allowed
        if ' ' in self.cleaned_data['app_secret_id']:
            raise forms.ValidationError({'app_secret_id': 'no space allowed in secret id'})




class FbScrapperDataForm(forms.ModelForm):
    
    class Meta:
        model = FacebookData
        fields = ['page', 'name']

    def clean(self):
        # no space allowed
        if ' ' in self.cleaned_data['page']:
            raise forms.ValidationError({'page': 'no space allowed in url friendly text'})


