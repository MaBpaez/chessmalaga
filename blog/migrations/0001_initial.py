# Generated by Django 3.2.9 on 2022-12-20 07:50

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de edición')),
            ],
            options={
                'verbose_name': 'categoría',
                'verbose_name_plural': 'categorías',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='titulo')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='imagen')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contenido')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de publicación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('search_date', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(choices=[('draft', 'Borrador'), ('published', 'Publicado')], default='draft', max_length=10, verbose_name='estado')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('categories', models.ManyToManyField(blank=True, related_name='get_posts', to='blog.Category', verbose_name='categorías')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
    ]
