# Generated by Django 5.0.1 on 2024-08-31 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDFUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf1', models.FileField(upload_to='pdfs/')),
                ('pdf2', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
