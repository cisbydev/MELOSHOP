from django import forms
from .models import FormulaireContact

class FormulaireContactForm(forms.ModelForm):
    class Meta:
        model = FormulaireContact
        fields = ['nom', 'email', 'message']
        
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }