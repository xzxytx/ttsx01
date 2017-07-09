from django.conf.urls import url
import views
urlpatterns = [
    url(r'^user/$', views.user),
    url(r'^register/$', views.register),
    url(r'^ok/$', views.ok),
    url(r'^register_valid/$', views.register_valid),
    url(r'^login/$', views.login),
    # url(r'^user_judge/$', views.user_judge),
    url(r'^userok/$', views.userok),
    url(r'^info/$', views.info),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
    url(r'^site_addr/$', views.site_addr),
    url(r'^cart/$', views.cart),
    url(r'^exit/$', views.exit),
    url(r'^record/$', views.record),
]