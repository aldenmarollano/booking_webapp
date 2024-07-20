from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.views import View



from account.forms import UserRegistrationForm, AccountAuthenticationForm
from account.models import Account


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
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect('bookapp:room_bldg_list')
        else:
            context['registration_form'] = form
    return render(request, 'account/account_register.html', context)


def logout_view(request):
    logout(request)
    return redirect('bookapp:room_bldg_list')


def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('bookapp:room_bldg_list')
    
    destination = get_redirect_if_exists(request)

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("bookapp:room_bldg_list")
        
        else:
            context['login_form'] = form

    return render(request, "account/account_login.html", context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def account_view(request, username, *args, **kwargs):
    try:
        account = Account.objects.get(username = username)
    except:
        return HttpResponse("Something went wrong.")
    
    context = {
        'profile': account
    }
    return render(request, 'account/account_profile.html', context)


