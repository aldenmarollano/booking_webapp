from email import message
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from bookapp.forms import BldgForm, RoomForm, BookingForm
from bookapp.models import Bldg, Booking, Room
from datetime import datetime
from django.contrib import messages



def user_home_screenview(request):
    context = {}
    return render(request, "bookapp/home.html", context)



class BldgRegistrationView(View):

    def get(self, request):
        if request.user.username == 'admin':
            bldg_form = BldgForm()
            context = {
                'building': bldg_form,
            }

            return render(request, 'admin/register_bldg.html', context)
        else:
            return redirect('bookapp:room_bldg_list')
    
    def post(self, request):
        if request.user.is_authenticated:
            bldg_form = BldgForm(request.POST)
            if bldg_form.is_valid():
                bldg_form.save()
        
        return redirect('bookapp:add_room')


class RoomRegistrationView(View):
    def get(self, request):
        if request.user.username == 'admin':
            room_form = RoomForm()
            context = {
                'room': room_form
            }

            return render(request, 'admin/add_room.html', context)
        else:
            return redirect('bookapp:room_bldg_list')

    def post(self, request):
        room_form = RoomForm(request.POST, request.FILES)
        if room_form.is_valid():
            room_form.save()
        return redirect('bookapp:room_bldg_list')
    
class BookedRoomView(View):
    def get(self, request):
        room_list = Booking.objects.all()
        context = {
            'room_list': room_list
        }
        return render(request, 'admin/booked_room.html', context)

class CheckedOutView(View):
    def post(self, request, id):
        checkout_room = Booking.objects.get(id=id)
        checkout_room.delete()

        return redirect('bookapp:booked')


class RoomBldgListView(View):
    def get(self, request):
        room_list = Room.objects.all()
        
        context = {
            'room_list': room_list
        }
        return render(request, 'admin/room_bldg_list.html', context)
    
class RoomView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:login')

    def get(self, request, id=None):
        if id is not None:
            room = Room.objects.get(pk=id)
            booking_form = BookingForm()
            context = {
                'room': room,
                'booking_form': booking_form
            }
            return render(request, 'bookapp/room.html', context)
        
        else:
            booking_form = BookingForm()
            context = {
                'booking_form': booking_form
            }
            return render(request, 'bookapp/room.html', context)

    def post(self, request):

        form = BookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            room_id = get_object_or_404(Room, pk=room.id)

            booking_date = Booking.objects.filter(  
                room=room_id.pk,
                start_date__lt=end_date,
                end_date__gt=start_date
            )

            if booking_date.exists():
                messages.error(request, "Room is not available for the selected dates.")
                return redirect('bookapp:room_data', id=room.id)
            form.save()

            return redirect('bookapp:booked')
        
        else:
            room = form.cleaned_data['room']
            messages.error(request, "End date must be after start date.")
            return redirect('bookapp:room_data', room.id)

        