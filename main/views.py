from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# import the model
from main.models import Article
# relative import the forms to create new article
from .forms import CreatArticle

# Create the view of Article index to show all articles.

def article_index(request):
    articles = Article.objects.all().order_by("-publication_date")
    context = {
        "articles": articles,
    }
    return render (request, "article/index.html", context)

def article_show(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=="POST":
        article.delete()
        return redirect("/")

    context = {
        "article": article,
    }
    return render(request, "article/show.html", context)

def article_new(request):
    # initiate an empty dict to stock the data
    context = {}

    form = CreatArticle()
    if request.method == "POST":
        form = CreatArticle(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')

    context['form'] = form
    return render(request, 'article/new.html', context)
