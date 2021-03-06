# Generated by Django 4.0.4 on 2022-05-06 14:07

import Web.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nftcollection',
            name='owner',
            field=models.ForeignKey(on_delete=models.SET('USER_DELETED'), related_name='NFTCollection', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='nftcollectioncategory',
            name='backgroundPicture',
            field=models.ImageField(storage=Web.models.OverwriteStorage(), upload_to=Web.models.FileUploadLocation(fields=['name', 'background'], parentFolder='Categories/'), verbose_name='Background Picture'),
        ),
        migrations.AlterField(
            model_name='nftcollectioncategory',
            name='foregroundPicture',
            field=models.ImageField(storage=Web.models.OverwriteStorage(), upload_to=Web.models.FileUploadLocation(fields=['name', 'foreground'], parentFolder='Categories/'), verbose_name='Foreground Picture'),
        ),
    ]
