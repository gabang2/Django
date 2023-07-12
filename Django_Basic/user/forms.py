from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=32, label="사용자 이름")
    user_password = forms.CharField(max_length=64, label="사용자 비밀번호", widget=forms.PasswordInput)
