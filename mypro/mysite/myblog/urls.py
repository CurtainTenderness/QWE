from django.conf.urls import url

from . import views
app_name='myblog'
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^signin/$',views.signin,name='signin'),
    url(r'^addarticle/$',views.addarticle,name='addarticle')
]