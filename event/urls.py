from django.urls import path
from .views import home, event_detail


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:event_id>', event_detail, name='event-detail')
]
