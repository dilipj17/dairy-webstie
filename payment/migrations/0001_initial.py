# Generated by Django 2.2.5 on 2019-10-14 18:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('trans_id', models.CharField(max_length=10, null=True, unique=True)),
                ('take_money', models.BooleanField(default=False)),
                ('amount', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('balance', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Customer')),
            ],
        ),
    ]
