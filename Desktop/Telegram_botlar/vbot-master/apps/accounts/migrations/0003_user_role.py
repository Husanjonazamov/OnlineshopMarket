# Generated by Django 4.2.5 on 2023-09-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(blank=True, choices=[(1, 'Veterenar'), (2, 'Yetkazib beruvchi')], null=True),
        ),
    ]
