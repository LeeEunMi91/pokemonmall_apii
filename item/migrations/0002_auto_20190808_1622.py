# Generated by Django 2.2.4 on 2019-08-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='uploads/item_images/'),
        ),
    ]
