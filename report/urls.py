from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from report import views as report_views
from accounts import views as accounts_views

urlpatterns = [

    path('', report_views.work_submission, name='work_submission'),
 
    
]