# Generated by Django 4.1.5 on 2023-05-14 19:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchList',
            field=models.ManyToManyField(blank=True, null=True, related_name='ListingWatchList', to=settings.AUTH_USER_MODEL),
        ),
    ]
