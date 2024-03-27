# Generated by Django 4.2.11 on 2024-03-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name', max_length=100)),
                ('subject', models.CharField(help_text='Enter your subject', max_length=100)),
                ('email', models.EmailField(help_text='Enter your email address', max_length=254)),
                ('message', models.CharField(help_text='Enter your message', max_length=500)),
            ],
        ),
    ]