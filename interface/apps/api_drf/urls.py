from django.urls import include, path
from rest_framework import routers
from api_drf import views


router = routers.DefaultRouter()
router.register(r'topic', views.TopicViewSet)
