#每一个路由文件中必须编写路由数组

#引入路由绑定函数
from django.conf.urls import url
#2.引入路由函数绑定的的视图
from . import views
app_name = 'booktest'
urlpatterns = [
    url(r'^$',                views.index,      name='index'),
    url(r'^detail/(\d+)/$',     views.detail,     name='detail'),
    url(r'^about/$',          views.about,      name='about'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^edithero/(\d+)/$',views.edithero, name='edithero')

]