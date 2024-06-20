from django.db import models

# Create model Article.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    # use the title to dispay in admin for each created instance.
    def __str__(self):
        return self.title
