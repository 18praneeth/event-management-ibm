from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='event'),
    path('detail/<int:event_id>', event_detail, name='event-detail'),
    path('detail/event-delete/<int:event_id>', event_delete, name='event-delete'),
    path('detail/event-update/<int:event_id>', event_update, name='event-update'),
    path('college/',create_college,name='college'),
    path('create-event', create_event, name='create-event'),
    path('accept-event/<int:id>', signup_event, name='signup-event'),
    path('reject-event/<int:id>', reject_event, name='reject-event'),
    path('signup-event/<int:id>', mail_signup, name='mail-signup')
]
