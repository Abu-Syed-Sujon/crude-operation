# Generated by Django 4.2.7 on 2023-12-29 03:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="members",
            old_name="first_name",
            new_name="firstname",
        ),
        migrations.RenameField(
            model_name="members",
            old_name="last_name",
            new_name="lastname",
        ),
    ]
