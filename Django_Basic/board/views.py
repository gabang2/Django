from django.shortcuts import render

# Create your views here.
from board.models import Board


def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, "board_list.html", {"boards": boards})
