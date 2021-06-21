from os import name
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='event'),
    path('detail/<int:event_id>', event_detail, name='event-detail'),
    path('detail/event-delete/<int:event_id>', event_delete, name='event-delete'),
    path('detail/event-update/<int:event_id>', event_update, name='event-update'),
    path('college/',create_college,name='college-create'),
    path('create-event', create_event, name='create-event'),
    path('college-details',college_details,name='college-details'),
    path('college-edit/<int:id>', college_edit, name='college-edit'),
    path('college-delete/<int:id>', college_delete, name='college-delete'),
    path('accept-event/<int:id>', signup_event, name='signup-event'),
    path('signup-event/<int:id>', mail_signup, name='mail-signup'),
    path('edit-sme/<int:id>', edit_sme, name='edit-sme'),
    path('sme-list/', sme_list, name='sme-list')
]
