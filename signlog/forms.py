from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _trans
from django.contrib.auth import authenticate


class SignupForm(forms.Form):
    username = forms.CharField(label=_trans('Nume de utilizator'))
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label=_trans('Parola'),
        help_text=_trans(
            "<br>Parola trebuie sa aiba minim 8 caractere.<br>"
            "Parola trebuie sa contina minim o litera mare.<br>"
            "Parola trebuie sa contina minim o cifra.<br>"
            "Parola nu trebuie sa contina spatii.<br>"
        )

    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label=_trans('Confirmare parola'),
        help_text=_trans("Introduceti aceeasi parola pentru verificare.")
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_trans('Acest nume de utilizator este deja folosit.'))
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_trans('Parolele nu se potrivesc.'))
        if len(password1) < 8:
            raise forms.ValidationError(_trans("Parola trebuie sa aiba minim 8 caractere."))
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError(_trans("Parola trebuie sa contina minim o litera mare."))
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError(_trans("Parola trebuie sa contina minim o cifra."))
        if ' ' in password1:
            raise forms.ValidationError(_trans("Parola nu trebuie sa contina spatii."))

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label=_trans('Nume de utilizator'))
    password = forms.CharField(widget=forms.PasswordInput, label=_trans('Parola'))

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(_trans('Nume de utilizator invalid.'))
        return username

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError(_trans('Parola incorecta.'))

        return cleaned_data


