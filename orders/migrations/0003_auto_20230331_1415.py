# Generated by Django 3.0.3 on 2023-03-31 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20230331_1406'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DinnerPlatters',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Pasta',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.DeleteModel(
            name='Salads',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='extras',
        ),
        migrations.DeleteModel(
            name='Catagories',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Sub',
        ),
        migrations.DeleteModel(
            name='SubExtras',
        ),
    ]
