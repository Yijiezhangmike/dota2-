# Generated by Django 3.0 on 2020-01-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dota2_deco', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='id',
        ),
        migrations.AlterField(
            model_name='items',
            name='item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]