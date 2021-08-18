from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('add_candidate', views.add_candidate),
    path('vote_candidate', views.vote_candidate),
    path('vote_result', views.vote_result),
    path('vote_summary', views.vote_summary),
]
