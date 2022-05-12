from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('kettik', views.kettik, name='kettik'),
    path('main', views.main_page, name='main'),
    # path('login', views.login, name='login'),
    # path('search', views.search, name='search'),
    path('place', views.place, name='place'),
    path('register', views.postsignUp, name='register'),
    path('api/', views.PlaceListAPIView.as_view(), name='api_place'),
    path('api/random', views.random_place, name='random_place'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
