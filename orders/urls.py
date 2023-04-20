from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.mainpage, name = "love"),
    path("love/", views.love, name = 'lovee'),
    path("sad/", views.sad, name = "sad"),
    path('favicon.ico', RedirectView.as_view(url='/static/orders/favicon.ico')),
    path("home/", views.home, name = "home"),
    path("menu/predict", views.predict),
    #path("home/predict", views.predict, name="predict"),
    path("menu/", views.index, name="index"),
    path("analysis/", views.analysis, name = "analysis")
]
