from django.shortcuts import render


# Create your views here.

def register(request):
    # 1. url로 들어올 때
    if request.method == 'GET':
        return render(request, 'user/register.html')
    # 2. submit(등록)버튼을 눌러서 들어올 때
    elif request.method == 'POST':
        return render(request, 'user/register.html')

