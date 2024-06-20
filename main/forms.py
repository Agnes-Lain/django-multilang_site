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

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         label= "Title of the article:",
#         max_length=255,
#         widget=forms.TextInput(
#             attrs={"class": "form-control"}
#         ),
#     )
#     content = forms.CharField(
#         label= "Content of the article:",
#         widget=forms.Textarea(
#             attrs={"class": "form-control"}
#         )
#     )
