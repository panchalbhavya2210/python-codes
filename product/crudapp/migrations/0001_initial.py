# Generated by Django 5.0 on 2023-12-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('productprice', models.FloatField()),
                ('productdesc', models.TextField()),
                ('productimage', models.ImageField(upload_to='photos')),
            ],
        ),
    ]