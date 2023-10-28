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

    def theme_dir(self):
        return os.path.join(settings.MEDIA_ROOT, self.name)

    def set_dir(self):
        theme_dir_path = self.theme_dir()
        os.makedires(theme_dir_path, exist_ok=True)

        image_dir_path = os.path.join(theme_dir_path, "Images")
        os.makedires(image_dir_path, exist_ok=True)

        src_dir_path = os.path.join(settings.STATIC_ROOT, "Images")

        for filename in os.listdir(src_dir_path):
            src_image_path = os.path.join(src_dir_path, filename)
            dest_image_path = os.path.join(image_dir_path, filename)
            shutil.copy2(src_image_path, dest_image_path)

    def save(self, *args, **kwargs):
        super(Ktheme, self).save(*args, **kwargs)
        if not self.id:
            CssColor.objects.create(parent=self)
            CssBubble.objects.create(parent=self)


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


def upload_path(filename):
    image_dir = "images/"
    image_path = f"{image_dir}{filename}"
    return image_path


class KthemeImages(models.Model):
    ktheme = models.OneToOneField(
        Ktheme, on_delete=models.CASCADE, related_name="ktheme_images"
    )
    for field_name, filenames in name_dic.items():
        field = models.ImageField(
            upload_to=upload_path,
            default=f"default_images/{filenames[0]}",
        )
        locals()[field_name] = field


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
    s_1_x = models.PositiveIntegerField(default=17)
    s_1_y = models.PositiveIntegerField(default=17)
    s_1_t = models.PositiveIntegerField(default=10)
    s_1_l = models.PositiveIntegerField(default=11)
    s_1_b = models.PositiveIntegerField(default=9)
    s_1_r = models.PositiveIntegerField(default=17)

    s_2_x = models.PositiveIntegerField(default=17)
    s_2_y = models.PositiveIntegerField(default=17)
    s_2_t = models.PositiveIntegerField(default=10)
    s_2_l = models.PositiveIntegerField(default=11)
    s_2_b = models.PositiveIntegerField(default=9)
    s_2_r = models.PositiveIntegerField(default=17)

    r_1_x = models.PositiveIntegerField(default=20)
    r_1_y = models.PositiveIntegerField(default=17)
    r_1_t = models.PositiveIntegerField(default=10)
    r_1_l = models.PositiveIntegerField(default=17)
    r_1_b = models.PositiveIntegerField(default=9)
    r_1_r = models.PositiveIntegerField(default=11)

    r_2_x = models.PositiveIntegerField(default=20)
    r_2_y = models.PositiveIntegerField(default=17)
    r_2_t = models.PositiveIntegerField(default=10)
    r_2_l = models.PositiveIntegerField(default=17)
    r_2_b = models.PositiveIntegerField(default=9)
    r_2_r = models.PositiveIntegerField(default=11)


@receiver(post_save, sender=Ktheme)
def create_css_model(sender, instance, **kwargs):
    CssColor.objects.get_or_create(ktheme=instance)
    CssBubble.objects.get_or_create(ktheme=instance)
    KthemeImages.objects.get_or_create(ktheme=instance)
