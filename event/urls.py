from django.urls import path
from .views import home, event_detail, create_sme,create_college


urlpatterns = [
    path('', home, name='event'),
    path('detail/<int:event_id>', event_detail, name='event-detail'),
    path('sme/', create_sme, name='sme'),
    path('college/',create_college,name='college')
]
