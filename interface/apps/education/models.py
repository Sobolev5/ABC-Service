from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.utils.translation import gettext_lazy as _
import autopep8


class Topic(models.Model):
    # lesson8 lesson9 lesson10 lesson11 lesson12
    user_profile = models.ForeignKey("user_profile.UserProfile", blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Snippet(models.Model):
    # lesson8 lesson9 lesson10 lesson11 lesson12
    user_profile = models.ForeignKey("user_profile.UserProfile", blank=True, null=True, on_delete=models.CASCADE)
    topic = models.ForeignKey("education.Topic", null=True, on_delete=models.SET_NULL)
    name = models.CharField("Title", max_length=100)
    text = models.TextField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    # lesson10
    @classmethod
    def question_autopep8(
        cls,
        sender,
        instance,
        created,
        *args,
        **kwargs
    ):    
     
        signals.post_save.disconnect(Snippet.question_autopep8, sender=Snippet)
        instance.question = autopep8.fix_code(instance.question)
        print("hello signal from django")
        instance.save()
        signals.post_save.connect(Snippet.question_autopep8, sender=Snippet)

signals.post_save.connect(Snippet.question_autopep8, sender=Snippet)