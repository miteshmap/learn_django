# Generated by Django 2.0.6 on 2018-09-20 17:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MiteshmapBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('alias', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True, help_text='Designates whether this blog is published. Unselect this instead of deleting blogs.', verbose_name='published')),
            ],
            options={
                'db_table': 'blogs',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='MiteshmapBlogTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='MiteshmapBlogWebsites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'websites',
            },
        ),
        migrations.AddField(
            model_name='miteshmapblog',
            name='tags',
            field=models.ManyToManyField(to='blog.MiteshmapBlogTags'),
        ),
        migrations.AddField(
            model_name='miteshmapblog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='miteshmapblog',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.MiteshmapBlogWebsites'),
        ),
    ]
