from django.db import models

# Create your models here.


from django.db import models


class BlogData(models.Model):

    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title
