# Generated by Django 5.0.1 on 2024-01-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='otp',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]