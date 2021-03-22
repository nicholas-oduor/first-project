# Generated by Django 3.1.3 on 2021-03-22 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blogs/'),
            preserve_default=False,
        ),
    ]
