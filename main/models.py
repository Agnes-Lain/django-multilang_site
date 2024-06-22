from django.db import models
# import tool to manage translation
from django.utils.translation import gettext_lazy as _

# Create model Article.

class Article(models.Model):
    title = models.CharField(_("title"), max_length=255)
    content = models.TextField(_("content"))
    publication_date = models.DateTimeField(_("publication_date"),auto_now_add=True)
    # use the title to dispay in admin for each created instance.
    def __str__(self):
        return self.title
