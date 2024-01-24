from django import forms
from .import views
from .models import NetBankingCustomer,Districts,Branches
class Customerform(forms.ModelForm):
    Gender = forms.ChoiceField(choices=NetBankingCustomer.GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio-inline'}))
    Account_type = forms.MultipleChoiceField(choices=NetBankingCustomer.ACCOUNT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Materials = forms.MultipleChoiceField(choices=NetBankingCustomer.MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'}))
    BirthDate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    District = forms.ModelChoiceField(queryset=Districts.objects.all())
    Branch = forms.ModelChoiceField(queryset=Branches.objects.all())
    class Meta:
        model=NetBankingCustomer
        fields = ['Name','BirthDate','Gender','Age','Phone', 'Address', 'Account_type', 'Materials', 'District','Branch']

