# Generated by Django 4.1.3 on 2023-11-09 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_cssbubble_r_1_l_alter_cssbubble_r_1_r_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="kthemeimages",
            name="add_friend",
            field=models.ImageField(
                default="Images/findBtnAddFriend@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="chat_bg",
            field=models.ImageField(
                default="Images/chatroomBgImage@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="chat_bubble_r_1",
            field=models.ImageField(
                default="Images/chatroomBubbleReceive01@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="chat_bubble_r_2",
            field=models.ImageField(
                default="Images/chatroomBubbleReceive02@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="chat_bubble_s_1",
            field=models.ImageField(
                default="Images/chatroomBubbleSend01@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="chat_bubble_s_2",
            field=models.ImageField(
                default="Images/chatroomBubbleSend02@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="main_bg",
            field=models.ImageField(default="Images/mainBgImage@3x.png", upload_to=""),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_bg",
            field=models.ImageField(
                default="Images/passcodeBgImage@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_1",
            field=models.ImageField(
                default="Images/passcodeImgCode01@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_1_s",
            field=models.ImageField(
                default="Images/passcodeImgCode01Selected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_2",
            field=models.ImageField(
                default="Images/passcodeImgCode02@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_2_s",
            field=models.ImageField(
                default="Images/passcodeImgCode02Selected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_3",
            field=models.ImageField(
                default="Images/passcodeImgCode03@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_3_s",
            field=models.ImageField(
                default="Images/passcodeImgCode03Selected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_4",
            field=models.ImageField(
                default="Images/passcodeImgCode04@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_img_4_s",
            field=models.ImageField(
                default="passcodeImgCode04Selected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="passcode_pressed",
            field=models.ImageField(
                default="Images/passcodeKeypadPressed@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="profile_img",
            field=models.ImageField(default="Images/profileImg01@3x.png", upload_to=""),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_bg",
            field=models.ImageField(
                default="Images/maintabBgImage@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_1",
            field=models.ImageField(
                default="Images/maintabIcoFriends@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_1_s",
            field=models.ImageField(
                default="Images/maintabIcoFriendsSelected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_2",
            field=models.ImageField(
                default="Images/maintabIcoChats@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_2_s",
            field=models.ImageField(
                default="Images/aintabIcoChatsSelected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_3",
            field=models.ImageField(
                default="Images/maintabIcoOpenChats@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_3_s",
            field=models.ImageField(
                default="Images/maintabIcoOpenChatsSelected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_4",
            field=models.ImageField(
                default="Images/maintabIcoShopping@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_4_s",
            field=models.ImageField(
                default="Images/maintabIcoShoppingSelected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_5",
            field=models.ImageField(
                default="Images/maintabIcoMore@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="tab_ico_5_s",
            field=models.ImageField(
                default="Images/maintabIcoMoreSelected@3x.png", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="kthemeimages",
            name="theme_icon",
            field=models.ImageField(default="Images/commonIcoTheme.png", upload_to=""),
        ),
    ]
