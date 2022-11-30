# Generated by Django 3.2.8 on 2022-11-21 15:28

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20221119_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='picture',
        ),
        migrations.AddField(
            model_name='basketitem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.image_directory_path),
        ),
    ]
