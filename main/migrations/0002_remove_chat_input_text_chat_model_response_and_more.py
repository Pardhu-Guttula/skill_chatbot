# Generated by Django 4.2.7 on 2023-12-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='input_text',
        ),
        migrations.AddField(
            model_name='chat',
            name='model_response',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='user_input',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
