# Generated by Django 3.0.5 on 2021-05-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzhut', '0014_pizza'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='toppings',
            field=models.CharField(default='onion', max_length=20),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings1',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings10',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings11',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings12',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings13',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings14',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings15',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings16',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings17',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings18',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings19',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings2',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings20',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings3',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings4',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings5',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings6',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings7',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings8',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings9',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
