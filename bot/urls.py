from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chartbot , name="chart"),
    path('upload/', views.upload_chart , name="upload"),
    path('younme/', views.youandme , name="younme"),
    path('training/', views.training_data , name="training"),
    path('main/',views.main,name="main")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


