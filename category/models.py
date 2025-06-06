from django.db import models



class Category(models.Model):
    category_name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=250)
    cat_img=models.ImageField(upload_to='photos/categories', blank=True, null=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['category_name'] 
    def __str__(self):
        return self.category_name
    