# Generated by Django 3.2.8 on 2022-11-22 20:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_historyitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]