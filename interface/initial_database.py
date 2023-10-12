import os
from django.contrib.auth.models import User
from simple_print import sprint
from education.models import Topic, Snippet
from user_profile.models import UserProfile
from mixer.backend.django import Mixer


def clear() -> None:
    # python run.py initial_database "clear()"
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Topic.objects.all().delete()
    Snippet.objects.all().delete()
    sprint("Clear_database -> complete", c="green")


def prepare() -> None:
    # python run.py initial_database "prepare()"
    mixer = Mixer(commit=False)

    username = "abc"
    password = "abc"
    exist = False

    try:
        superuser = User.objects.create_superuser(username=f"{username}@abc.abc", email=f"{username}@abc.abc", password=password)
        superuser.save()
        sprint(superuser)
        superuser_profile = UserProfile()
        superuser_profile.user = superuser
        superuser_profile.name = username
        superuser_profile.password_recovery_key = 'abc'
        superuser_profile.save()
        sprint(superuser_profile)
    except Exception as e:
        # superuser exist
        print(e)
        exist = True
    
    if not exist:

        for data_type in ["str", "int", "float", "complex", "list", "tuple", "range", "dict", "set", "frozenset"]:
            topic = mixer.blend(Topic)
            topic.user_profile = superuser_profile
            topic.name = data_type
            topic.save()

            for j in range(5):
                snippet = mixer.blend(Snippet)
                snippet.topic = topic
                snippet.user_profile = superuser_profile
                snippet.name = "Print hello world"
                snippet.text = "print('hello world')"
                snippet.save()


        sprint("Fill_database -> complete", c="green")
    
    else:
        sprint("Fill_database -> already filled", c="red")