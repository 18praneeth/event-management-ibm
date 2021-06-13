from django.urls import path
from .views import user_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),   
]
