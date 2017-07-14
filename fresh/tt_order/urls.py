from django.conf.urls import url
import views
urlpatterns = [
    url(r'^place_order/$', views.place_order),
    url(r'^order_list/$', views.order_list),
]