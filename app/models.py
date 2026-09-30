from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    title = models.CharField('name', max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    name = models.CharField('name', max_length=100)
    description = models.TextField('description')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField('img', upload_to='media/')
    color = models.ManyToManyField('Color', verbose_name='color')
    date = models.DateField('date')
    end_date = models.DateField('end_date')
    is_active = models.BooleanField(default=True, verbose_name='is_activate')
    
    def __str__(self):
        return self.name

class Color(models.Model):
    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'

    title = models.CharField('name')


    def __str__(self):
        return self.title

# Create your models here.
