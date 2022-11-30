# Generated by Django 3.2.8 on 2022-11-03 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published')),
                ('followers', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1500, verbose_name='name')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(blank=True, default=1)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=store.models.image_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1500, verbose_name='name')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(blank=True, default=1)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='store.basket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
