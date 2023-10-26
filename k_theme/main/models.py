from django.db import models
from django.contrib.auth.models import User
import os
import shutil
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# from main.models import Ktheme


def ktheme_save_path(instance, filename):
    return os.path.join("kthemes", str(instance.user.id), filename)


class Ktheme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # user_id = models.CharField(max_length=50)
    theme_id = models.CharField(max_length=50)
    theme_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.theme_name} by {self.user.username}"

    # image_dir = models.CharField(max_length=255, black=True)
    def theme_dir(self):
        return os.path.join(settings.MEDIA_ROOT, self.user.username, self.theme_name)

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
        if not self.theme_id:
            CssColor.objects.create(parent=self)
            CssBubble.objects.create(parent=self)


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
