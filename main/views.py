from django.shortcuts import render
from main.models import Article

# Create the view of Article index to show all articles.

def article_index(request):
    articles = Article.objects.all().order_by("-publication_date")
    context = {
        "articles": articles,
    }
    return render (request, "article/index.html", context)

def article_show(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "article/show.html", context)
