# Generated by Django 4.0.1 on 2024-08-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_assistancerequest_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistanceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('contact_info', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='AssistanceRequest',
        ),
    ]
