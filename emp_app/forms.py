from django import forms
from .models import Employee_reg


class EmpRegForm(forms.ModelForm):
    class Meta:
        model = Employee_reg
        fields = ['name', 'address', 'contact_number', 'email','pic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'contact_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pic': forms.FileInput(attrs={'class': 'form-control'})
        }
