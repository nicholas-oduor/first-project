from django.test import TestCase
from .models import Editor,Blog,tags
# Create your tests here.


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nicholas= Editor(first_name = 'nicholas', last_name ='Oduor', email ='oduor5742@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.nicholas,Editor))