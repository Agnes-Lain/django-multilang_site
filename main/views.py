from django.shortcuts import render, redirect
from django.utils.translation import get_language
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

# Create a view for one article detail with giving id. Inside, nested the routing for delete the showing article
def article_show(request, pk):
    article = Article.objects.get(pk=pk)
    lang = get_language()
    if request.method=="POST":
        article.delete()
        return redirect('/%s' % lang) # redirect to the corresponding language root


    context = {
        "article": article,
    }
    return render(request, "article/show.html", context)

# Create a form for adding new article to database
def article_new(request):
    # initiate an empty dict to stock the data
    context = {}

    form = CreatArticle()
    lang = get_language()
    if request.method == "POST":
        form = CreatArticle(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/%s' % lang) # redirect to the corresponding language root

    context['form'] = form
    return render(request, 'article/new.html', context)
