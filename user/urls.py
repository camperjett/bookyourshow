from django.urls import path, include
from django.conf import settings
from . import views
from movie.views import home_view
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='index'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.registration_view, name="register"),
    path('editprofile/', views.edit_profile, name="edit_profile"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('password/', views.change_password.as_view(template_name='user/change_password.html'), name='change_password'),
]
