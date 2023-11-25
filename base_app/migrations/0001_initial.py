# Generated by Django 4.2.7 on 2023-11-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Address', models.TextField()),
                ('DateOfBirth', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]