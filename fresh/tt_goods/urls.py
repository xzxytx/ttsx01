from django.conf.urls import url
import views
urlpatterns = [
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^place/$', views.place),
    url(r'^(\d+)/$', views.detail),
    url(r'^query/$', views.query),
]