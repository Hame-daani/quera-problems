
from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def clean_national_code(self):
        national_code = self.cleaned_data['national_code']
        if len(national_code) != 10:
            message = "invalid national code"
            raise forms.ValidationError(message)
        return national_code

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        first_name, last_name = full_name.split()
        if first_name.istitle() and last_name.istitle():
            return full_name
        message = "invalid full name"
        raise forms.ValidationError(message)
