# Generated by Django 3.0.5 on 2021-05-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzhut', '0016_auto_20210503_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='size4',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='size5',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='size6',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings10',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings11',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings12',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings13',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings14',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings15',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings16',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings17',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings18',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings19',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings20',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings7',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings8',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings9',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='toppings2',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
