import uuid

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from users.forms import LoginForm, RegisterForm, PasswordForm, ForgotForm
from users.models import User
from vk_bot import settings
from users.tasks import send_email


def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"])
            print("______-???")
            if user is not None:
                print(reverse("index"))
                login(request, user)
                # return redirect('/home/')
                return redirect(reverse("index"))
            else:
                return render(
                    request, "user/login.html",
                    {"form": form, "errors": ["Incorrect login or password"]})
        else:
            return render(request, "user/login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})


@login_required(login_url="/auth/login")
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))


def register(request):
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"])

            return redirect(reverse("login"))
        else:
            # print(render(request, "user/register.html", {"form": form}))
            return render(request, "user/register.html", {"form": form})
    else:
        print(render(request, "user/register.html", {"form": RegisterForm()}))
        return render(request, "user/register.html", {"form": RegisterForm()})


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "upper_buttons.html"


def confirm(request, code):
    success = False
    if request.method == "GET":
        try:
            user = User.objects.get(confirm_code=code)
            if user.is_confirmed is False:
                user.is_confirmed = True
                user.save()
                success = True
        except User.DoesNotExist:
            success = False
        except ValidationError:
            success = False
        return render(request, "confirm-page.html", {"success": success})


def forgot(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        form = ForgotForm()
        return render(request, "forgot.html", {"form": form})
    elif request.method == "POST":
        form = ForgotForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                token = uuid.uuid4()
                user.confirm_code = token
                user.save()
                # test.delay()
                send_email.delay("Reset password", settings.DEFAULT_FROM_EMAIL, user.email,
                                 'mail-reset.html', args=dict(code=user.confirm_code, name=user.first_name))
            except User.DoesNotExist:
                return render(
                    request, "forgot.html",
                    {"form": form, "errors": ["This email is wrong"]})
            return render(request, "forgot_success.html", {})


def reset(request, code):
    success = False
    if request.method == "GET":
        try:
            user = User.objects.get(confirm_code=code)
            form = PasswordForm()
        except User.DoesNotExist:
            return redirect(reverse('index'))
        except ValidationError:
            return redirect(reverse('index'))
        return render(request, "reset.html", {"form": form, "code": code})
    elif request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(confirm_code=code)
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect(reverse("login"))
            except User.DoesNotExist:
                pass
        else:
            render(request, "reset.html", {"form": form, "code": code})