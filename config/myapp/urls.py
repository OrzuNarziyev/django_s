from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('categories/<slug:slug>/', views.categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/',views.archive),
]
