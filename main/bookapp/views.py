from email import message
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from bookapp.forms import BldgForm, RoomForm, BookingForm
from bookapp.models import Bldg, Booking, Room



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
    
class RoomBldgListView(View):
    def get(self, request):
        # building_list = Bldg.objects.all()
        room_list = Room.objects.filter(is_booked=False)
        
        context = {
            # 'building_list': building_list,
            'room_list': room_list
        }
        return render(request, 'admin/room_bldg_list.html', context)


class BookingRegistration(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:login')

    def get(self, request):
        booking_form = BookingForm()
        context = {
            'booking_form':booking_form
        }
        return render(request, 'bookapp/booking_form.html', context)
    
    def post(self, request):
        booking_form = BookingForm(request.POST, user=request.user)
        if booking_form.is_valid():
            booking_form.save()

            room_id = booking_form.cleaned_data['room'].id
            room = Room.objects.get(pk=room_id)
            room.is_booked = True
            room.save()
        return render('bookapp:room_bldg_list')
            


                        