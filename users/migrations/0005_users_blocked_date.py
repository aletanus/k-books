# Generated by Django 4.2 on 2023-05-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_users_blocked"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="blocked_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
