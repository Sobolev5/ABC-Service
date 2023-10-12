from django.urls import re_path, path

from . import views

app_name = "education"

urlpatterns = [  
    re_path(r"^topics/$", views.topics, name="topics"),
    path("topic/view/<int:topic_id>/", views.topic_view, name="topic_view"),
]
