from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import FoodPostRudView, FoodAPIView


urlpatterns = [

    url(r'^(?P<pk>\d+)/$', FoodPostRudView.as_view(), name ='foods-rud'),
    url(r'^$', FoodAPIView.as_view(), name ='foods-create'),

]