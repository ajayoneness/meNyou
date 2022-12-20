from django.contrib import admin
from .models import chart_upload


class ChartAdmin(admin.ModelAdmin):
    list_display = ('user_name','upload_date','upload_chart')


admin.site.register(chart_upload)

