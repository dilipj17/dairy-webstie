# Generated by Django 2.2.5 on 2019-10-14 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transections',
            old_name='take_money',
            new_name='credit',
        ),
    ]