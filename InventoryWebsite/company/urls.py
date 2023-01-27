from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('companys', views.all_companys, name="list-companys"),
]