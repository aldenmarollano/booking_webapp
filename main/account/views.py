from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views import View

from account.forms import UserRegistrationForm

# class UserRegistrationView(View):
#     def get(self, request): 
#         form = UserRegistrationForm()
#         context = {
#             'form':form
#         }
#         return render(request, 'account/account_register.html', context)
    
#     def post(self, request):
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('home')

def user_registration_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}.")
    context = {}

    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password = raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect('account:home')
        else:
            context['registration_form'] = form
    return render(request, 'account/account_register.html', context)


def user_home_screenview(request):
    context = {}
    return render(request, "account/account_home.html", context)