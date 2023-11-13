from django.db import models
from django.contrib.auth.models import User
import os
import shutil
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


def ktheme_save_path(instance, filename):
    return os.path.join("kthemes", str(instance.user.id), filename)


class Ktheme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


name_dic = {
    "chat_bg": ["chatroomBgImage@3x.png"],
    "chat_bubble_r_1": [
        "chatroomBubbleReceive01@3x.png",
        "chatroomBubbleReceive01@2x.png",
        "chatroomBubbleReceive01Selected@2x.png",
        "chatroomBubbleReceive01Selected@3x.png",
    ],
    "chat_bubble_r_2": [
        "chatroomBubbleReceive02@3x.png",
        "chatroomBubbleReceive02@2x.png",
        "chatroomBubbleReceive02Selected@2x.png",
        "chatroomBubbleReceive02Selected@3x.png",
    ],
    "chat_bubble_s_1": [
        "chatroomBubbleSend01@2x.png",
        "chatroomBubbleSend01@3x.png",
        "chatroomBubbleSend01Selected@2x.png",
        "chatroomBubbleSend01Selected@3x.png",
    ],
    "chat_bubble_s_2": [
        "chatroomBubbleSend02@2x.png",
        "chatroomBubbleSend02@3x.png",
        "chatroomBubbleSend02Selected@2x.png",
        "chatroomBubbleSend02Selected@3x.png",
    ],
    "theme_icon": ["commonIcoTheme.png"],
    "main_bg": ["mainBgImage@3x.png"],
    "tab_bg": [
        "maintabBgImage@2x.png",
        "maintabBgImage@3x.png",
    ],
    "tab_ico_1": [
        "maintabIcoFriends@2x.png",
        "maintabIcoFriends@3x.png",
    ],
    "tab_ico_2": [
        "maintabIcoChats@2x.png",
        "maintabIcoChats@3x.png",
    ],
    "tab_ico_3": [
        "maintabIcoOpenChats@2x.png",
        "maintabIcoOpenChats@3x.png",
        "maintabIcoPiccoma@2x.png",
        "maintabIcoPiccoma@3x.png",
    ],
    "tab_ico_4": [
        "maintabIcoShopping@2x.png",
        "maintabIcoShopping@3x.png",
        "maintabIcoCall@2x.png",
        "maintabIcoCall@3x.png",
    ],
    "tab_ico_5": [
        "maintabIcoMore@2x.png",
        "maintabIcoMore@3x.png",
    ],
    "tab_ico_s_1": [
        "maintabIcoFriendsSelected@2x.png",
        "maintabIcoFriendsSelected@3x.png",
    ],
    "tab_ico_s_2": [
        "maintabIcoChatsSelected@2x.png",
        "maintabIcoChatsSelected@3x.png",
    ],
    "tab_ico_s_3": [
        "maintabIcoOpenChatsSelected@2x.png",
        "maintabIcoOpenChatsSelected@3x.png",
        "maintabIcoPiccomaSelected@2x.png",
        "maintabIcoPiccomaSelected@3x.png",
    ],
    "tab_ico_s_4": [
        "maintabIcoShoppingSelected@2x.png",
        "maintabIcoShoppingSelected@3x.png",
        "maintabIcoCallSelected@2x.png",
        "maintabIcoCallSelected@3x.png",
    ],
    "tab_ico_s_5": [
        "maintabIcoMoreSelected@2x.png",
        "maintabIcoMoreSelected@3x.png",
    ],
    "passcode_bg": ["passcodeBgImage@3x.png"],
    "passcode_1": [
        "passcodeImgCode01@3x.png",
    ],
    "passcode_2": [
        "passcodeImgCode02@3x.png",
    ],
    "passcode_3": [
        "passcodeImgCode03@3x.png",
    ],
    "passcode_4": [
        "passcodeImgCode04@3x.png",
    ],
    "passcode_s_1": [
        "passcodeImgCode01Selected@3x.png",
    ],
    "passcode_s_2": [
        "passcodeImgCode02Selected@3x.png",
    ],
    "passcode_s_3": [
        "passcodeImgCode03Selected@3x.png",
    ],
    "passcode_s_4": [
        "passcodeImgCode04Selected@3x.png",
    ],
    "passcode_pressed": [
        "passcodeKeypadPressed@3x.png",
    ],
    "profile_img": [
        "profileImg01@3x.png",
    ],
}


def ktheme_images_path(instance, filename):
    return f"media/{instance.ktheme.id}/{filename}"


# class KthemeImages(models.Model):
#     ktheme = models.OneToOneField(
#         Ktheme, on_delete=models.CASCADE, related_name="ktheme_images"
#     )

#     chat_bg = models.ImageField(
#         upload_to="media/Images",
#         default="static/Images/chatroomBgImage@3x.png",
#     )
#     chat_bubble_r_1 = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/chatroomBubbleReceive01@3x.png",
#     )
#     chat_bubble_r_2 = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/chatroomBubbleReceive02@3x.png",
#     )

#     chat_bubble_s_1 = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/chatroomBubbleSend01@3x.png",
#     )
#     chat_bubble_s_2 = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/chatroomBubbleSend02@3x.png",
#     )

#     theme_icon = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/commonIcoTheme.png"
#     )
#     # add_friend = models.ImageField(
#     #     upload_to=ktheme_images_path, default="static/Images/findBtnAddFriend@3x.png"
#     # )

#     main_bg = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/mainBgImage@3x.png"
#     )

#     tab_bg = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/maintabBgImage@3x.png"
#     )
#     tab_ico_1 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/maintabIcoFriends@3x.png"
#     )
#     tab_ico_1_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/maintabIcoFriendsSelected@3x.png",
#     )
#     tab_ico_2 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/maintabIcoChats@3x.png"
#     )
#     tab_ico_2_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/aintabIcoChatsSelected@3x.png",
#     )
#     tab_ico_3 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/maintabIcoOpenChats@3x.png"
#     )
#     tab_ico_3_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/maintabIcoOpenChatsSelected@3x.png",
#     )
#     tab_ico_4 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/maintabIcoShopping@3x.png"
#     )
#     tab_ico_4_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/maintabIcoShoppingSelected@3x.png",
#     )
#     tab_ico_5 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/maintabIcoMore@3x.png"
#     )
#     tab_ico_5_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/maintabIcoMoreSelected@3x.png",
#     )

#     passcode_bg = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/passcodeBgImage@3x.png"
#     )
#     passcode_img_1 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/passcodeImgCode01@3x.png"
#     )
#     passcode_img_1_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/passcodeImgCode01Selected@3x.png",
#     )
#     passcode_img_2 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/passcodeImgCode02@3x.png"
#     )
#     passcode_img_2_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/passcodeImgCode02Selected@3x.png",
#     )
#     passcode_img_3 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/passcodeImgCode03@3x.png"
#     )
#     passcode_img_3_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/passcodeImgCode03Selected@3x.png",
#     )
#     passcode_img_4 = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/passcodeImgCode04@3x.png"
#     )
#     passcode_img_4_s = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/passcodeImgCode04Selected@3x.png",
#     )
#     passcode_pressed = models.ImageField(
#         upload_to=ktheme_images_path,
#         default="static/Images/passcodeKeypadPressed@3x.png",
#     )
#     profile_img = models.ImageField(
#         upload_to=ktheme_images_path, default="static/Images/profileImg01@3x.png"
#     )


class CssColor(models.Model):
    ktheme = models.OneToOneField(
        Ktheme, on_delete=models.CASCADE, related_name="css_color"
    )
    bg_color = models.CharField(max_length=7, default="#FFFFFF")
    main_text_color = models.CharField(max_length=7, default="#000000")
    point_text_color = models.CharField(max_length=7, default="#FFC0CB")
    input_bg_color = models.CharField(max_length=7, default="#D3D3D3")
    send_text_color = models.CharField(max_length=7, default="#A9A9A9")
    receive_text_color = models.CharField(max_length=7, default="#808080")


class CssBubble(models.Model):
    ktheme = models.OneToOneField(
        Ktheme, on_delete=models.CASCADE, related_name="css_bubble"
    )
    s_1_x = models.PositiveIntegerField(default=20)
    s_1_y = models.PositiveIntegerField(default=17)
    s_1_t = models.PositiveIntegerField(default=10)
    s_1_l = models.PositiveIntegerField(default=17)
    s_1_b = models.PositiveIntegerField(default=9)
    s_1_r = models.PositiveIntegerField(default=11)

    s_2_x = models.PositiveIntegerField(default=20)
    s_2_y = models.PositiveIntegerField(default=17)
    s_2_t = models.PositiveIntegerField(default=10)
    s_2_l = models.PositiveIntegerField(default=17)
    s_2_b = models.PositiveIntegerField(default=9)
    s_2_r = models.PositiveIntegerField(default=11)

    r_1_x = models.PositiveIntegerField(default=17)
    r_1_y = models.PositiveIntegerField(default=17)
    r_1_t = models.PositiveIntegerField(default=10)
    r_1_l = models.PositiveIntegerField(default=11)
    r_1_b = models.PositiveIntegerField(default=9)
    r_1_r = models.PositiveIntegerField(default=17)

    r_2_x = models.PositiveIntegerField(default=17)
    r_2_y = models.PositiveIntegerField(default=17)
    r_2_t = models.PositiveIntegerField(default=10)
    r_2_l = models.PositiveIntegerField(default=11)
    r_2_b = models.PositiveIntegerField(default=9)
    r_2_r = models.PositiveIntegerField(default=17)


# @receiver(post_save, sender=KthemeImages)
# def create_image_model(sender, instance, created, **kwargs):
#     if created:
#         KthemeImage.objects.get_or_create(ktheme_images=instance)


# @receiver(post_save, sender=Ktheme)
# def ktheme_user(sender, instance, created, **kwargs):
#     if created:
#         user = instance.user
#         instance.user = user
#         instance.save()


@receiver(post_save, sender=Ktheme)
def create_css_model(sender, instance, created, **kwargs):
    if created:
        CssColor.objects.get_or_create(ktheme=instance)
        CssBubble.objects.get_or_create(ktheme=instance)


# @receiver(post_save, sender=Ktheme)
# def create_image_model(sender, instance, created, **kwargs):
#     if created:
#         KthemeImages.objects.get_or_create(ktheme=instance)


@receiver(post_save, sender=Ktheme)
def create_theme_dir(sender, instance, created, **kwargs):
    if created:
        theme_dir = os.path.join(settings.MEDIA_ROOT, instance.id)
        theme_image_dir = os.path.join(theme_dir, "Images")
        theme_css = os.path.join(theme_dir, "KakaoTalkTheme.css")

        src_css = os.path.join(settings.STATIC_ROOT, "KakaoTalkTheme.css")
        default_image_dir = os.path.join(settings.STATIC_ROOT, "Images")

        if not os.path.exists(theme_dir):
            # os.makedirs(theme_dir)
            # os.makedirs(theme_image_dir)
            shutil.copytree(default_image_dir, theme_image_dir)
            shutil.copy2(src_css, theme_css)


# def create_theme_dir(sender, instance, created, **kwargs):
#     if created:
#         theme_dir = os.path.join(settings.MEDIA_ROOT, f"{instance.id}")

#         theme_image_dir = os.path.join(theme_dir, "Images")
#         default_images_dir = os.path.join(settings.STATIC_ROOT, "default_images")

#         theme_css = os.path.join(theme_dir, "KakaoTalkTheme.css")
#         src_css = os.path.join(settings.STATIC_ROOT, "KakaoTalkTheme.css")

#         try:
#             shutil.copytree(theme_image_dir, default_images_dir)
#             shutil.copy2(src_css, theme_css)

#         except Exception as e:
#             print(f"Error copying user media: {str(e)}")
