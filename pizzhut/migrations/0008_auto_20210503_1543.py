# Generated by Django 3.0.5 on 2021-05-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzhut', '0007_auto_20210503_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='size5',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='pizza',
            name='size6',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='shape1',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='shape2',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size1',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size2',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size3',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size4',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
    ]
