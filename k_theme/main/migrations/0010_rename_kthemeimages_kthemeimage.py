# Generated by Django 4.1.3 on 2023-10-04 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_rename_uploadedimage_kthemeimages"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="KthemeImages",
            new_name="KthemeImage",
        ),
    ]
