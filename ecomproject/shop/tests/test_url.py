from django.test import TestCase
from django.urls import resolve, reverse
from shop.views import *

# class TestURL(TestCase):
#     def test_home(self):
#         result=self.client.get('/')
#         print(result)
#         self.assertEquals(result.status_code, 200)

class TestUrl(TestCase):
    def test_home(self):
        url=reverse('home')
        print("url is", url)
        self.assertEquals(resolve(url).func, home)
        self.assertTemplateUsed('home.html')
        print(resolve(url))

