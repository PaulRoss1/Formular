from ares_util.validators import czech_company_id_numeric_validator, czech_company_id_ares_api_validator
from django.core.validators import validate_email
from django import forms
from .models import Formular



class FormularForm(forms.ModelForm):
    ico = forms.IntegerField(required=True, validators=[czech_company_id_ares_api_validator], label='IČO')
    email = forms.EmailField(required=False, validators=[validate_email])
    class Meta:
        model = Formular
        fields = ['jmeno', 'email', 'ico']
        labels = {'jmeno': 'Jméno'}
