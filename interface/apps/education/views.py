from django.shortcuts import render
from django.shortcuts import Http404
from django.utils.translation import gettext_lazy as _
from education.models import Topic
from education.forms import TopicForm


def topics(request):
    d = {}
    d["topics"] = Topic.objects.all()
    d["education_nav_menu"] = 1
    return render(request, "education/topics.html", context=d)


def topic_view(request, topic_id: int):
    d = {}

    try:
        d["topic"] = topic = Topic.objects.get(pk=topic_id)
    except:
        raise Http404

    # форма
    if request.method == "POST":
        topic_form = TopicForm(request.POST, instance=topic)
        if topic_form.is_valid():
            print(topic_form.cleaned_data)
            # TODO сделать сохранение данных в модель
    else:
        topic_form = TopicForm(instance=topic)
    d["topic_form"] = topic_form
    
    # сниппеты 
    d["snippets"] = topic.snippet_set.all()
    
    d["education_nav_menu"] = 1

    return render(request, "education/topic_view.html", context=d)