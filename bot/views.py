from django.shortcuts import render,redirect
from .models import chart_upload
from django.conf import settings

def chartbot(request):
    if request.method == "POST":
        ml = request.POST['male']
        fml  = request.POST['female']
        print(settings.BASE_DIR)

        if ml=='':
            print(fml)
            return redirect('/bot/upload/')
        else:
            print(ml)
            return redirect('/bot/upload/')
    return render(request,"Home.html")


def upload_chart(request):
    if request.method == 'POST':
        chart = request.FILES['chart']
        print(request.user.username,chart)
        chart_upload(user_name=request.user.username,upload_chart=chart).save()

    return render(request,'uploadFile.html')

def training_data(request):
    pass