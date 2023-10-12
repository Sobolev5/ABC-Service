import secrets
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import UserProfile
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from settings import HOST
from simple_print import sprint


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST" and request.POST:
            username = request.POST["email"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password)
            user_profile = UserProfile.objects.filter(user=user).first()
            if user is not None and user_profile:
                login(request, user)
                response = HttpResponseRedirect(reverse("user_profile:edit_profile"))
                return response
                # lesson9 показать в хроме куки)
                # return render(request, "main/login.html")
            else:
                messages.error(request, _("Неверный адрес электронной почты или пароль"))
                return HttpResponseRedirect(reverse("main:user_login"))
        else:
            return render(request, "main/login.html")

    else:
        user = User.objects.get(id=request.user.id)
        user_profile = UserProfile.objects.filter(user=user).first()

        if user_profile:
           return HttpResponseRedirect(reverse("user_profile:edit_profile"))

        else:
            logout(request)
            return render(request, "main/login.html")


def user_registration(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_profile:edit_profile"))

    else:
        if request.method == "POST" and request.POST:

            try:
                validate_email(request.POST["email"])
            except ValidationError:
                messages.error(request, _("Некорректный формат Email"))
                return HttpResponseRedirect(reverse("main:user_registration"))

            if len(request.POST["password"]) < 6:
                messages.error(request, _("Пароль должен состоять не менее чем из 6 символов"))
                return HttpResponseRedirect(reverse("main:user_registration"))

            if len(request.POST["password"]) > 32:
                messages.error(request, _("Пароль должен состоять не более чем из 32 символов"))
                return HttpResponseRedirect(reverse("main:user_registration"))

            if request.POST["password"] != request.POST["confirm_password"]:
                messages.error(request, _("Пароли не совпадают"))
                return HttpResponseRedirect(reverse("main:user_registration"))

            user = User.objects.filter(email=request.POST["email"]).first()
            if not user:

                user = User.objects.create_user(
                    email=request.POST["email"], username=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"]
                )

                user_profile = UserProfile()
                user_profile.user = user
                user_profile.name = f"{request.POST['first_name']} {request.POST['last_name']}"
                user_profile.save()

                user.backend = "django.contrib.auth.backends.ModelBackend"
                login(request, user)

                messages.success(request, _("Успешная регистрация."))
                return HttpResponseRedirect(reverse("user_profile:edit_profile"))
            else:
                messages.error(request, _("Пользователь с данным Email уже существует"))
                return HttpResponseRedirect(reverse("main:user_registration"))

        else:
            return render(request, "main/registration.html")


def user_password_recovery(request):
    if request.method == "POST" and request.POST:
        user = User.objects.filter(email=request.POST["email"]).first()

        if user:
            user_profile = UserProfile.objects.get(user=user)
            user_profile.password_recovery_key = str(secrets.token_hex(16))
            user_profile.save()

            messages.success(request, _("Ссылка для сброса"))
            return HttpResponseRedirect(reverse("main:user_password_recovery__set_new_password", kwargs={"password_recovery_key": user_profile.password_recovery_key }))
        else:
            messages.error(request, _("Пользователь c данным Email не существует"))
            return HttpResponseRedirect(reverse("main:user_password_recovery"))

    else:
        return render(request, "main/password_recovery.html")


def user_password_recovery__set_new_password(request, password_recovery_key):

    try:
        user_profile = UserProfile.objects.get(password_recovery_key=password_recovery_key)
    except Exception as e:
        return HttpResponse("Ссылка для сброса пароля не существует или не действительна")

    if request.method == "POST" and request.POST:

        if len(request.POST["password"]) < 6:
            messages.error(request, _("Пароль должен состоять не менее чем из 6 символов"))
            return HttpResponseRedirect(reverse("main:user_password_recovery"))

        if len(request.POST["password"]) > 32:
            messages.error(request, _("Пароль должен состоять не более чем из 32 символов"))
            return HttpResponseRedirect(reverse("main:user_password_recovery"))

        if request.POST["password"] != request.POST["confirm_password"]:
            messages.error(request, _("Пароли не совпадают"))
            return HttpResponseRedirect(reverse("main:user_password_recovery"))

        user = user_profile.user
        user.set_password(request.POST["password"])
        user.save()

        user_profile.password_recovery_key = None
        user_profile.save()

        messages.success(request, _("Ваш пароль успешно сброшен"))
        return HttpResponseRedirect(reverse("main:user_login"))

    return render(request, "main/password_recovery__set_password.html")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:user_login"))


def handler404(request, *args, **argv):
    response = render(request, "404.html", {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, "500.html", {})
    response.status_code = 500
    return response


def test(request, named_group):
    print(named_group)
    # lesson1
    return render(request, "main/test.html", {"named_group": named_group})


def template_render(request):
    my_tmpl = """
        <b>{{ hello }}</b>
        <br
        <b>{{ some_var }}</b>
    """

    context = {}
    context["some_var"] = 100
    context["hello"] = "world"

    for k, v in context.items():
        tmpl_var = "{{ %s }}" % k
        my_tmpl = my_tmpl.replace(tmpl_var, str(v))
        
    my_tmpl = my_tmpl.encode() # переводим в байтовую строку
    return HttpResponse(my_tmpl)