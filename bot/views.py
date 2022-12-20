from django.shortcuts import render,redirect
from .models import chart_upload
from django.conf import settings

def chartbot(request):
    if request.method == "POST":
        ml = request.POST['male']
        fml  = request.POST['female']
        print(settings.BASE_DIR)

        if ml=='':
            request.session['gender']=fml
            return redirect('/bot/younme/')
        else:
            request.session['gender']=ml
            return redirect('/bot/younme/')
    return render(request,"Home.html")

def youandme(request):
    if request.method == "POST":
        request.session['name'] = request.POST['yourname']
        request.session['partner'] = request.POST['partnername']
        return redirect('/bot/upload/')

    return render(request,'youandme.html')



def upload_chart(request):
    if request.method == 'POST':
        chart = request.FILES['chart']
        print(request.user.username,chart)
        chart_upload(user_name=request.user.username,
                     upload_chart=chart,
                     gender=request.session['gender'],
                     your_name=request.session['name'],
                     partner_name=request.session['partner'],
                     ).save()
        return redirect('/bot/training/')

    return render(request,'uploadFile.html')



def training_data(request):
    return render(request,'process.html')

def main(request):
    return render(request,'chart.html')
