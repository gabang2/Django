from django.urls import path

from board import views

app_name = "board"
urlpatterns = [
    path("", views.board_list, name="board_list"),
    path("write/", views.board_write, name="board_write"),
    path("<int:pk>/", views.board_detail, name="board_detail")
]
