from django.conf.urls import url

from . import views
app_name='myblog'
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^signin/$',views.signin,name='signin'),
    url(r'^addarticle/$',views.addarticle,name='addarticle'),
    url(r'^list/$',views.list,name='list'),
    url(r'^sendmails/$',views.sendmails,name='sendmails'),
    url(r'^createmage/$',views.createmage,name='createmage'),
    url(r'^jsontest/$',views.jsontest,name='jsontest'),
]