# Generated by Django 2.1.1 on 2018-12-07 11:37

from django.db import migrations
from django.conf import settings

def default_category(apps, schema_editor):
    Category = apps.get_model('gdpr_tools', 'Category')

    Category.objects.bulk_create([
        Category(
            name = 'Marketing',
            type = 'FA',
        ),
        Category(
            name = 'Technical',
            type = 'NE',
        ),
        Category(
            name = 'Statistics',
            type = 'FA',
        ),
    ])

def reverse_default_category(apps, schema_editor):
    Category = apps.get_model('gdpr_tools', 'Category')
    Category.objects.get(name='Marketing').delete()
    Category.objects.get(name='Technical').delete()
    Category.objects.get(name='Statistics').delete()

def default_cookie(apps, schema_editor):
    Category = apps.get_model('gdpr_tools', 'Category')
    Cookie = apps.get_model('gdpr_tools', 'Cookie')

    Cookie.objects.create(
        name = settings.CSRF_COOKIE_NAME,
        description = 'Necessary for Cross Site Request Forgery Protection',
        category = Category.objects.get(name='Technical'),
    )

def reverse_default_cookie(apps, schema_editor):
    Cookie = apps.get_model('gdpr_tools', 'Cookie')
    Cookie.objects.get(name=settings.CSRF_COOKIE_NAME)

class Migration(migrations.Migration):

    dependencies = [
        ('gdpr_tools', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_category, reverse_default_category),
        migrations.RunPython(default_cookie, reverse_default_cookie),
    ]
