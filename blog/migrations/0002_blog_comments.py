# Generated by Django 5.0.7 on 2024-07-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, to='blog.comments'),
        ),
    ]
