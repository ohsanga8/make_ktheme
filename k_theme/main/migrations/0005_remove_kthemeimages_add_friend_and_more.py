# Generated by Django 4.1.3 on 2023-11-10 06:53

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_kthemeimages_add_friend_kthemeimages_chat_bg_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="kthemeimages",
            name="add_friend",
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="chat_bg",
            field=models.ImageField(
                default="static/Images/chatroomBgImage@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="chat_bubble_r_1",
            field=models.ImageField(
                default="static/Images/chatroomBubbleReceive01@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="chat_bubble_r_2",
            field=models.ImageField(
                default="static/Images/chatroomBubbleReceive02@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="chat_bubble_s_1",
            field=models.ImageField(
                default="static/Images/chatroomBubbleSend01@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="chat_bubble_s_2",
            field=models.ImageField(
                default="static/Images/chatroomBubbleSend02@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="main_bg",
            field=models.ImageField(
                default="static/Images/mainBgImage@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_bg",
            field=models.ImageField(
                default="static/Images/passcodeBgImage@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_1",
            field=models.ImageField(
                default="static/Images/passcodeImgCode01@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_1_s",
            field=models.ImageField(
                default="static/Images/passcodeImgCode01Selected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_2",
            field=models.ImageField(
                default="static/Images/passcodeImgCode02@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_2_s",
            field=models.ImageField(
                default="static/Images/passcodeImgCode02Selected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_3",
            field=models.ImageField(
                default="static/Images/passcodeImgCode03@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_3_s",
            field=models.ImageField(
                default="static/Images/passcodeImgCode03Selected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_4",
            field=models.ImageField(
                default="static/Images/passcodeImgCode04@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_img_4_s",
            field=models.ImageField(
                default="static/Images/passcodeImgCode04Selected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="passcode_pressed",
            field=models.ImageField(
                default="static/Images/passcodeKeypadPressed@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="profile_img",
            field=models.ImageField(
                default="static/Images/profileImg01@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_bg",
            field=models.ImageField(
                default="static/Images/maintabBgImage@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_1",
            field=models.ImageField(
                default="static/Images/maintabIcoFriends@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_1_s",
            field=models.ImageField(
                default="static/Images/maintabIcoFriendsSelected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_2",
            field=models.ImageField(
                default="static/Images/maintabIcoChats@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_2_s",
            field=models.ImageField(
                default="static/Images/aintabIcoChatsSelected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_3",
            field=models.ImageField(
                default="static/Images/maintabIcoOpenChats@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_3_s",
            field=models.ImageField(
                default="static/Images/maintabIcoOpenChatsSelected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_4",
            field=models.ImageField(
                default="static/Images/maintabIcoShopping@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_4_s",
            field=models.ImageField(
                default="static/Images/maintabIcoShoppingSelected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_5",
            field=models.ImageField(
                default="static/Images/maintabIcoMore@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="tab_ico_5_s",
            field=models.ImageField(
                default="static/Images/maintabIcoMoreSelected@3x.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
        migrations.AlterField(
            model_name="kthemeimages",
            name="theme_icon",
            field=models.ImageField(
                default="static/Images/commonIcoTheme.png",
                upload_to=main.models.ktheme_images_path,
            ),
        ),
    ]