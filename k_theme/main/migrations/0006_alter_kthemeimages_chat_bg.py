# Generated by Django 4.1.3 on 2023-11-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_remove_kthemeimages_add_friend_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kthemeimages",
            name="chat_bg",
            field=models.ImageField(
                default="static/Images/chatroomBgImage@3x.png", upload_to="media/Images"
            ),
        ),
    ]