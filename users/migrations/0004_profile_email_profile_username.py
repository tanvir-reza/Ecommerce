# Generated by Django 4.2.4 on 2023-12-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_name_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]