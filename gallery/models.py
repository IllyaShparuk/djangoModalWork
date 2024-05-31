from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    categories = models.ManyToManyField('Category')
    created_date = models.DateField(auto_now_add=True)
    age_limit = models.PositiveIntegerField(blank=True)


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
