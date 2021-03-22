from django.db import models
import datetime as dt

# Create your models here.
"""
creating class editor and assigning models
"""

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class Blog(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_blogs(cls):
        today = dt.date.today()
        blogs = cls.objects.filter(pub_date__date = today)
        return blogs

    @classmethod
    def days_blogs(cls,date):
        blogs = cls.objects.filter(pub_date__date = date)
        return blogs