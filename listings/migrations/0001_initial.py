# Generated by Django 5.0.2 on 2024-03-01 13:42

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('society', models.TextField()),
                ('sale_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=50)),
                ('house_type', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial')], default='Residential', max_length=50)),
                ('price', models.DecimalField(decimal_places=5, max_digits=100)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('furnish_type', models.CharField(choices=[('Furnished', 'Furnish'), ('Semifurnished', 'Semifurnish'), ('Unfurnished', 'Unfurnish')], default='Furnished', max_length=50)),
                ('carpet_area', models.IntegerField()),
                ('floor_no', models.CharField(max_length=20)),
                ('facing', models.CharField(max_length=20)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_9', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_10', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]