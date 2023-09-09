from django.shortcuts import render
from .models import User

# Create your views here.


def user_dashboard(request, id):
    info = User.objects.all().get(pk=id)

    context = {"info": info}

    return render(request, "user/dashboard.html", context)
