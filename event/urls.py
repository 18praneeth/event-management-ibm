from django.urls import path
from .views import home, event_detail, form_demo


urlpatterns = [
    path('', home, name='event'),
    path('detail/<int:event_id>', event_detail, name='event-detail'),
    path('form', form_demo, name='random')
]
