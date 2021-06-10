from django.urls import path
from .views import home


urlpatterns = [
    path('', home, name='home-page'),
    # path('home/', home_page, name='sjd')
    # user/
    # user/home
]
