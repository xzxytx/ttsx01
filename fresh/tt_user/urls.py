from django.conf.urls import url
import views
urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^ok/$', views.ok),
    url(r'^register_valid/$', views.register_valid),
    url(r'^login/$', views.login),
    url(r'^user_judge/$', views.user_judge),
    url(r'^userok/$', views.userok),
]