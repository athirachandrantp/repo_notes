# Generated by Django 4.2.4 on 2023-08-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynotes',
            name='notes_image',
            field=models.ImageField(blank=True, default='images/aman.jpeg', null=True, upload_to='images/'),
        ),
    ]
