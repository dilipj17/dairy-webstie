# Generated by Django 2.2.6 on 2019-11-11 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['cust_id']},
        ),
    ]