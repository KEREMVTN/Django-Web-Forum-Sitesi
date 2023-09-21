from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Kullanıcı İsmi")
    password = forms.CharField(max_length=100, label="Şifre", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            username = authenticate(username=username, password=password)

            if not username:
                raise forms.ValidationError("Kullanıcı adı ya da şifre hatalı")
            return super(LoginForm, self).clean()
