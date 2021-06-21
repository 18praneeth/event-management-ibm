from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),   
    path('profile/', profile, name="profile"),
    path('report/', csv_export, name='csv-export'),
    path('create-sme/', register, name='create-sme')
]
