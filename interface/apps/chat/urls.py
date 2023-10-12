from django.urls import re_path

from . import views

app_name = "main"

# lesson5 lesson6 
urlpatterns = [  
    re_path(r"^room/(?P<room_name>\w+)/$", views.room_simple, name="room_simple"),
    re_path(r"^room/descriptor_under_the_hood/(?P<room_id>\w+)/$", views.room_descriptor, name="room_descriptor"),
    re_path(r"^http/$", views.http, name="http"),
]
