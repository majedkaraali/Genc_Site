# Generated by Django 4.2.2 on 2023-06-25 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import personal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('time', models.DateTimeField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=personal.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Events',
                'verbose_name_plural': 'Incoming Events',
            },
        ),
    ]
