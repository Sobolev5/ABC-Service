from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from api_drf.serializers import TopicSerializer
from education.models import Topic


class TopicViewSet(viewsets.ModelViewSet):
    # lesson8
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]

