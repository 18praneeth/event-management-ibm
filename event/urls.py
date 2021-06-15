from django.urls import path
from .views import event_delete, event_update, home, event_detail,create_college, create_event


urlpatterns = [
    path('', home, name='event'),
    path('detail/<int:event_id>', event_detail, name='event-detail'),
    path('detail/event-delete/<int:event_id>', event_delete, name='event-delete'),
    path('detail/event-update/<int:event_id>', event_update, name='event-update'),
    path('college/',create_college,name='college'),
    path('create-event', create_event, name='create-event'),
    
]
