from django.db import models
from django.contrib.auth.models import User



class chart_upload(models.Model):
    user_name = models.TextField(max_length=254, unique=True, db_index=True, primary_key=True)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    upload_chart = models.FileField(upload_to="chart/",max_length=250,null=True,default=None)
    gender = models.TextField(max_length=10)
    your_name = models.TextField(max_length=50)
    partner_name = models.TextField(max_length=50)


