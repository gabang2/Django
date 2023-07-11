import re

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import FcUser


def register(request):
    res_data = {}
    email_regex = re.compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    # 1. url로 들어올 때
    if request.method == 'GET':
        return render(request, 'user/register.html')
    # 2. submit(등록)버튼을 눌러서 들어올 때
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', None)  # 에러가 나지 않도록 기본 값 설정해주기 => None은 논리적으로 False임
        user_email = request.POST.get('user_email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        if not (user_name and password and re_password and user_email):
            res_data['error'] = "모든 값을 입력 바랍니다."
        elif not email_regex.match(user_email):
            res_data['error'] = "이메일 형식의 예시는 다음과 같습니다. ex)offbeat1020@naver.com"
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            fcuser = FcUser(
                user_name=user_name,
                password=make_password(password)
            )
            fcuser.save()

        return render(request, 'user/register.html', res_data)
