from .views import HomePageView, AboutPageView, basePageView
from django.urls import path
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('base/', basePageView.as_view(), name='base'),

]