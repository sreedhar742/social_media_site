# Generated by Django 4.2.7 on 2024-12-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='picture_binary',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
