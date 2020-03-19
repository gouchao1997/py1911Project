#每一个路由文件中必须编写路由数组

#引入路由绑定函数
from django.conf.urls import url
#2.引入路由函数绑定的的视图
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'detail/(\d+)', views.detail),
    url(r'about/$', views.about)

]