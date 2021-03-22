from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Editor,Blog,tags

admin.site.register(Editor)
admin.site.register(Blog)
admin.site.register(tags)