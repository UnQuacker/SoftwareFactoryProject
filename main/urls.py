from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('kettik', views.kettik, name='kettik'),
    path('main', views.main_page, name='main'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
]

urlpatterns += staticfiles_urlpatterns()