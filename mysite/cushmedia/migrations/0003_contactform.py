# Generated by Django 3.0.7 on 2020-06-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cushmedia', '0002_portfolio_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
