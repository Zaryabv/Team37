# Generated by Django 3.2.8 on 2022-11-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20221123_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyitem',
            name='picture',
            field=models.ManyToManyField(blank=True, null=True, related_name='history_image', to='store.ImageFiles'),
        ),
    ]
