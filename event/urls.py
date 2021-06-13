from django.urls import path
from .views import home, event_detail,create_college, create_event


urlpatterns = [
    path('', home, name='event'),
    path('detail/<int:event_id>', event_detail, name='event-detail'),
    path('college/',create_college,name='college'),
    path('create-event', create_event, name='create-event')
]
