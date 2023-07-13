from django.urls import path

from board import views

urlpatterns = [
    path("", views.board_list)
]