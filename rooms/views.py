from django.shortcuts import render
from .models import Room, Booking


# Функція представлення списку всіх кімнат
def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms  
    }
    return render(request=request, template_name="rooms/room_list.html", context=context)
