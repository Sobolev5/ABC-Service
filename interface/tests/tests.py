import pytest
from simple_print import sprint
from education.models import Snippet, Topic
from django.urls import reverse


@pytest.mark.django_db
def test_hello_world(auto_login_user):
    assert True


@pytest.mark.django_db
def test_topic_page(auto_login_user):
    # pytest tests/tests.py::test_topic_page -rP
    client, user = auto_login_user()
    sprint(client, user)
    url = reverse("education:topics")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic():
    # pytest tests/tests.py::test_topic -rP
    topic = Topic(name="test_topic")
    topic.save()
    topic = Topic.objects.first()
    sprint(topic)
    assert topic

