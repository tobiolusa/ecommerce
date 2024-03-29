from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey("Category", related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=100, default="un-branded")
    description = models.TextField(blank=True)
    slug =models.SlugField(max_length=256, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='media/', default='default_image.jpg')
    
    class Meta:
            verbose_name_plural = 'products'
    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])