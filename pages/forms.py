from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    # honeypot
    hp_field = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'style': 'display:none',
            }
        ),
        label=""
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'hp_field']
        labels = {
            'name': 'Imię, nazwisko lub nazwa firmy',
            'email': 'Adres e-mail',
            'message': 'Wiadomość',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def clean_hp_field(self):
        data = self.cleaned_data.get('hp_field')
        if data:
            raise forms.ValidationError("Spam detected")
        return data
