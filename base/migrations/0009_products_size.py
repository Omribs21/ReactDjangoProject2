# Generated by Django 4.0.6 on 2022-10-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
