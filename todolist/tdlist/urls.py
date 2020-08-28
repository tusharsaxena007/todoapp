from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('logout',views.logout_view,name='logout'),
    path('newuser',views.NewUser.as_view(),name='newuser'),
    path('delete/<int:pk>',views.delete_view,name='delete'),
    path('newtodo',views.newtodo.as_view(),name='newtodo'),
    path('loginpage',views.loginpage.as_view(),name='loginpage')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
