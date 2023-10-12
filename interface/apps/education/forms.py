from django import forms
from education.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'text']