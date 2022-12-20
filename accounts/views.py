from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from bot.models import chart_upload

def login(request):
    obj = chart_upload.objects.filter(user_name=str(request.user.username))
    if request.method == 'POST':
        uname = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            obj = chart_upload.objects.filter(user_name=str(request.user.username))
            try:
                if obj[0].user_name == str(request.user.username):
                    return redirect("/bot/training/")
                else:
                    return redirect("/bot/")
            except:
                return redirect("/bot/")

        else:
            messages.info(request, "invalid user")
            return redirect("/")
    if request.user.is_authenticated:
        try:
            if obj[0].user_name == str(request.user.username):
                return redirect("/bot/training/")
            else:
                return redirect("/bot/")
        except:
            return redirect("/bot/")

    else:
        return render(request, "login.html")



def register(request):
    obj = chart_upload.objects.filter(user_name=str(request.user.username))
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['user_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['repassword']

        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username Taken')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')

            else:
                user = User.objects.create_user(username=uname, password=pass1, email=email, first_name=fname,last_name=lname)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'both password are not save')
    if request.user.is_authenticated:
        try:
            if obj[0].user_name == str(request.user.username):
                return redirect("/bot/training/")
            else:
                return redirect("/bot/")
        except:
            return redirect("/bot/")

    else:
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

