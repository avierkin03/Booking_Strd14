from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("rooms/", views.rooms_list, name="rooms"),
    path("booking/", views.book_room, name="booking"),
]
