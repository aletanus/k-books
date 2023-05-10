# Generated by Django 4.2.1 on 2023-05-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_author_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='json_data',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdfs'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='BookPdf',
        ),
    ]