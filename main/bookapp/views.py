from django.shortcuts import render

def user_home_screenview(request):
    context = {}
    return render(request, "bookapp/home.html", context)
