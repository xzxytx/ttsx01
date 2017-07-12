from django.conf.urls import url
import views

urlpatterns = [
    url(r'add_cart/$', views.add_cart),
    url(r'^cart/$', views.cart),
    url(r'^revise_cart/$', views.revise_cart),
    url(r'^goods_count/$', views.goods_count),
]