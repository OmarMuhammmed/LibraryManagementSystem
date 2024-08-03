from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField( max_length=50)
    def __str__(self):
      return self.name 

class Book(models.Model):
    
    status_book = [
        ('available','available'), # 1 to show user and 1 in DB
        ('rental','rental'),
        ('soild','soild'),
    ]

    title = models.CharField( max_length=50)
    author = models.CharField( max_length=50, blank=True, null=True)
    image_book = models.ImageField(upload_to='images',blank=True, null=True) # Must edit settings media
    image_author = models.ImageField(upload_to='images',blank=True, null=True) 
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField( max_digits=5, decimal_places=2,blank=True, null=True)
    price_day = models.DecimalField( max_digits=5, decimal_places=2,blank=True, null=True)
    rentel_period = models.IntegerField(blank=True, null=True)
    total_rental_price = models.DecimalField( max_digits=5, decimal_places=2,blank=True, null=True) 
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices= status_book, blank=True, null=True) 
    category = models.ForeignKey(Category, on_delete=models.PROTECT,blank=True, null=True) # if yon Delete catogrey Book is not deleted
    
    
    
    def __str__(self):
      return self.title 



    
