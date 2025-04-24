from django.db import models

# Create your models here.
class AllProducts(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='AllProducts', default=1, null=False, blank=False)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id:05d} - {self.name} - {self.price} - {self.image.url} - {self.created_at} - {self.updated_at} - {self.is_active}"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name