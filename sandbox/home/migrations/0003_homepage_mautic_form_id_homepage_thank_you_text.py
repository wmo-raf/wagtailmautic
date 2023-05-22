# Generated by Django 4.2.1 on 2023-05-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='mautic_form_id',
            field=models.CharField(blank=True, help_text='Form ID to use. Make sure you have created the form with all the required fields on Mautic', max_length=256, null=True, verbose_name='Mautic Form ID'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='thank_you_text',
            field=models.TextField(blank=True, help_text='Message to show on successful submission', null=True),
        ),
    ]