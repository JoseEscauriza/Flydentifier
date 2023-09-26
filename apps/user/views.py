from typing import Optional
from django.shortcuts import render
from .models import User
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


class UserDashboard(TemplateView):
    def get(self, request, id):
        info = User.objects.all().get(pk=id)

        context = {"info": info}

        return render(request, "user/dashboard.html", context)


class Login(TemplateView):

    def get(self, request):
        self.error_message = None

        form = AuthenticationForm()

        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                user: Optional[User] = authenticate(
                    username=username,
                    password=password,
                )

                if user is not None:
                    login(request, user)

                    return redirect("user-dashboard")

            else:
                self.error_message = "Sorry, something went wrong. Please try again."

        context = {'form': form, "error_message": self.error_message}

        return render(
            request,
            template_name="user/login.html",
            context=context
        )
