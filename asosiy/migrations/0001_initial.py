# Generated by Django 4.1.1 on 2022-09-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intervyu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=50)),
                ('sana', models.DateField()),
                ('link', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=60)),
                ('matn', models.TextField()),
                ('sana', models.DateField()),
                ('rasm', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
