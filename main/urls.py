from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('kettik', views.kettik),
    path('main', views.main_page),
]

urlpatterns += staticfiles_urlpatterns()
