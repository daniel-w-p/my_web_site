from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    hp_field = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def clean_hp_field(self):
        data = self.cleaned_data.get("hp_field")
        if data:
            raise forms.ValidationError("Spam detected")
        return data

