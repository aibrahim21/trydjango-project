from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., "Smartphones"
    slug = models.SlugField(max_length=100, unique=True)  # URL-friendly version (e.g., "smartphones")
    description = models.TextField(blank=True, null=True)  # Optional

    class Meta:
        verbose_name_plural = "Categories"  # Fixes admin panel display

    def __str__(self):
        return self.name  # For readability in admin/dropdowns
    
    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,  # If category is deleted, set product's category to NULL
        null=True,
        blank=True,
        related_name="products"  # Access all products in a category via `category.products.all()`
    )
    content= models.TextField()
    price =models.DecimalField(max_digits=6 , decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d') #image=models.ImageField( upload_to = 'location of the image directory') 
    active = models.BooleanField(default= True) 

    def __str__(self):
        return self.name
    class Meta:
        ordering =['name']
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])