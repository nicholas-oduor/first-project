from django.test import TestCase
from .models import Editor,Blog
# Create your tests here.


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nicholas= Editor(first_name = 'nicholas', last_name ='Oduor', email ='oduor5742@gmail.com')