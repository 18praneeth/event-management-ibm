from django.urls import path
from .views import home


urlpatterns = [
    path('', home, name='home'),
    # path('home/', home_page, name='sjd')
    # user/
    # user/home
]