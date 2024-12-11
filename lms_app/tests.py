from django.test import TestCase
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User
from .models import Category

class TestModels(TestCase):

    def test_book_model(self):
        category = Category.objects.create(name='testcategory')
        book = Book.objects.create(  
                                    title='testbook', 
                                    author='testauthor', 
                                    pages=100, price=10.99,
                                    price_day=5.99, 
                                    rentel_period=7, 
                                    active=True, 
                                    status='available', 
                                    category= category
                                    )
        self.assertEqual(str(book), 'testbook')
        self.assertTrue(isinstance(book, Book))

class TestViews(TestCase):

    def test_index_view(self):

        # reverse ==> to get url ('viewname')
        # client.get => to get request same browser 
        response = self.client.get(reverse('index')) 

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')
