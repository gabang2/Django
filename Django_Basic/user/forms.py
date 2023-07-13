from django import forms
from django.contrib.auth.hashers import check_password

from user.models import FcUser


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=32, label="사용자 이름",
                                error_messages={
                                    "required": "사용자 이름을 입력해주세요."
                                })
    password = forms.CharField(max_length=64, label="사용자 비밀번호", widget=forms.PasswordInput,
                               error_messages={
                                   "required": "사용자 비밀번호를 입력해주세요."
                               })

    # 예외 처리 할 것 - 없는 사용자를 검색할 경우
    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get("user_name")
        password = cleaned_data.get("password")
        if user_name and password:
            try:
                fcuser = FcUser.objects.get(user_name=user_name)
            except FcUser.DoesNotExist:
                self.add_error("user_name", "사용자가 없습니다.")
                return
            if not check_password(password, fcuser.password):  # 비밀번호가 일치하는지 확인
                self.add_error("password", "비밀번호를 틀렸습니다.")  # password field에 error를 넣는 함수
            else:
                self.user_id = fcuser.id
