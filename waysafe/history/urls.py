from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/homepage/
    url(r'^$', views.index, name='index'),
    url(r'^lastOrder/$', views.lastOrder, name='lastOrder'),
    url(r'^previousOrders/$', views.previousOrders, name='previousOrders'),
    url(r'^savedItems/$', views.savedItems, name='savedItems'),
]