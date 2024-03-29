# Generated by Django 2.2.5 on 2019-10-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cust_id', models.IntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('father_or_husband_name', models.CharField(max_length=25)),
                ('village', models.CharField(max_length=25)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
