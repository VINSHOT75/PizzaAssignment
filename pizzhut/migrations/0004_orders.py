# Generated by Django 3.0.5 on 2021-05-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzhut', '0003_pizza_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size1', models.CharField(max_length=50)),
                ('size2', models.CharField(max_length=50)),
                ('size3', models.CharField(max_length=50)),
                ('size4', models.CharField(max_length=50)),
            ],
        ),
    ]
