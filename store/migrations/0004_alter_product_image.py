# Generated by Django 3.2.5 on 2022-02-26 18:37

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220225_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.path_and_rename),
        ),
    ]
