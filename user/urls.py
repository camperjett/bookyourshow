from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login, name ='login'),
    path('logout/', views.Logout, name ='logout'),
    path('register/', views.register, name ='register'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('password/', views.change_password.as_view(template_name='user/change_password.html'), name='change_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
