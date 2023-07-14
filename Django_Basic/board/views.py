from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from board.forms import BoardForm
from board.models import Board
from user.models import FcUser


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = request.GET.get("p", 1)
    paginator = Paginator(all_boards, 2)
    boards = paginator.get_page(page)
    return render(request, "board_list.html", {"boards": boards})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")
    return render(request, "board_detail.html", {"board": board})


def board_write(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            try:
                user_id = request.session["user"]
            except:
                return redirect("/user/login")
            fcuser = FcUser.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data["title"]
            board.contents = form.cleaned_data["contents"]
            board.writer = fcuser
            board.save()
            return redirect("/board/")
    elif request.method == "GET":
        form = BoardForm()
    return render(request, "board_write.html", {"form": form})
