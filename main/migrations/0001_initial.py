# Generated by Django 3.0.6 on 2020-05-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_desc', models.TextField()),
                ('blog_publishedDate', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
