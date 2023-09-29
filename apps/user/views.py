from typing import Optional
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UserDashboard(LoginRequiredMixin, TemplateView):
    login_url = 'user-login'
    redirect_field_name = 'next'

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        context = {"user": user}

        return render(
            request,
            "user/dashboard.html",
            context
        )


class Login(LoginView):
    login = 'user-login'
    template_name = 'user/login.html'
    redirect_field_name = 'user-dashboard'

    # def get(self, request):
    #     self.error_message = None

    #     form = AuthenticationForm()

    #     if request.method == 'POST':
    #         form = AuthenticationForm(data=request.POST)

    #         if form.is_valid():
    #             username = form.cleaned_data.get("username")
    #             password = form.cleaned_data.get("password")

    #             user: Optional[User] = authenticate(
    #                 username=username,
    #                 password=password,
    #             )

    #             if user is not None:
    #                 login(request, user)

    #                 return redirect("user-dashboard")

    #         else:
    #             self.error_message = "Sorry, something went wrong. Please try again."

    #     context = {'form': form, "error_message": self.error_message}

    #     return render(
    #         request,
    #         template_name="user/login.html",
    #         context=context
    #     )


class Logout(LogoutView):
    logout = 'logout'
