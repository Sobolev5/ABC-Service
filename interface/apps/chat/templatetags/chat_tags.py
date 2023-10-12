import random
from django import template
from chat.models import ChatMessage


register = template.Library()


@register.simple_tag
def warrior_quote(author):
    if author == "Footman":
        quotes = [
        "Ready to work.",
        "Yes, milord?",
        "What is it?",
        "More work?",
        "What?"
        ]
        return random.choice(quotes)
    else:
        return ""

@register.filter
def show_hp(author):
    return f"{author} (HP {len(author)})"

    
