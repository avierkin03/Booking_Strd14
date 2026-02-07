from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Логаут користувача
def user_logout(request):
    logout(request)
    return redirect("main_page")


# Логін користувача
def user_login(request):
    if request.method == "GET":
        form = AuthenticationForm()

    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") 
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main_page")

    return render(request, template_name="auth_system/login.html", context={"form": form})

