from django import forms
from .models import Article

# create a form to fill, in order to create new article in database

class CreatArticle(forms.ModelForm):
    # create meta class
    class Meta:
        # which model to be used for the form
        model = Article
        # which fileds to be added to the form
        fields = [
            "title",
            "content",
        ]
