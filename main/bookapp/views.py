from django.shortcuts import redirect, render
from django.views import View

from bookapp.forms import BldgForm, RoomForm, BookingForm
from bookapp.models import Bldg, Booking, Room


def user_home_screenview(request):
    context = {}
    return render(request, "bookapp/home.html", context)


class BldgRegistrationView(View):
    def get(self, request):
        bldg_form = BldgForm()
        context = {
            'building': bldg_form
        }

        return render(request, 'admin/register_bldg.html', context)
    
    def post(self, request):
        bldg_form = BldgForm(request.POST)
        if bldg_form.is_valid():
            bldg_form.save()
        
        return redirect('bookapp:add_room')


class RoomRegistrationView(View):
    def get(self, request):
        room_form = RoomForm()
        context = {
            'building': room_form
        }

        return render(request, 'admin/add_room.html', context)
    
    def post(self, request):
        bldg_form = RoomForm(request.POST)
        if bldg_form.is_valid():
            bldg_form.save()
        
        return redirect('bookapp:room_bldg_list')
    
class RoomBldgListView(View):
    def get(self, request):
        building_list = Bldg.objects.all()
        room_list = Room.objects.all()
        
        context = {
            'building_list': building_list,
            'room_list': room_list
        }
        return render(request, 'admin/room_bldg_list.html', context)
