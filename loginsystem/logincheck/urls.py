from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logincheck',views.logincheck,name='logincheck'),
    path('logout',views.logout_view,name='logout'),
    path('createnewuser',views.createnewuser,name='createnewuser'),
    path('createnewblog',views.createnewblog,name='createnewblog'),
    path('deleteblog/<int:pk>',views.deleteblog,name='deleteblog'),
    path('shareall', views.shareall, name='shareall'),
    path('share/<int:pk>', views.share, name='share'),
    path('share/likecount/<int:pk>',views.likecount,name='likecount'),
    path('share/dislikecount/<int:pk>',views.dislikecount,name='dislikecount'),
    path('edit/<int:pk>',views.editblog,name='editblog'),
]
