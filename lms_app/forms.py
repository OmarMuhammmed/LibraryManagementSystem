from django import forms 
from .models import Book , Category



class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'


class AddBookForm(forms.ModelForm):
  
  class Meta :

    model = Book
    fields = [ 
              'title',
              'author',
              'image_book',
              'image_author',
              'pages',
              'price',
              'price_day',
              'rentel_period',
              'total_rental_price',
              'status',
              'category',
                    ]
    
    widgets ={
       'price_day':forms.NumberInput(attrs={'class':'form-control', 'id':'rentaldays'}),
       'rentel_period':forms.NumberInput(attrs={'class':'form-control','id':'rentalprice'}),
       'total_rental_price':forms.NumberInput(attrs={'class':'form-control','id':'totalrental'})
    }

