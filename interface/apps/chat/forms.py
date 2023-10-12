from django import forms
from django.core.exceptions import ValidationError


class ChatMessageForm(forms.Form):
    author = forms.CharField(required=True)
    message = forms.CharField(required=True)

    def clean_author(self):
        author = self.cleaned_data['author']
        if author == "Peon":
            raise ValidationError(
                "You can not write to Lordaeron!"
            )
        return author    

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get("author")
        message = cleaned_data.get("message")


        if author == "Orc" and message == "Lordaeron fall":
            raise ValidationError(
                "Lordaeron never fall!"
            )