# Generated by Django 2.2.5 on 2019-10-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_register', '0002_auto_20191004_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
