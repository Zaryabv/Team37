# Generated by Django 3.2.8 on 2022-11-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_historyitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyitem',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
