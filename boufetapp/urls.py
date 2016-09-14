from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.vistainicio),
        url(r'^productos/', views.vistaproductos),
    ]



