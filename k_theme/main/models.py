import os
import re
import shutil

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import get_css_template_path, get_default_images_dir, safe_theme_dir


def ktheme_images_path(instance, filename):
    """더 이상 사용되지 않는 KthemeImages 모델의 upload_to 콜백.
    과거 마이그레이션 파일들이 이 함수를 'main.models.ktheme_images_path'로
    직접 참조하고 있어서, 실제 모델을 지워도 이 함수 자체는
    호환성을 위해 남겨둬야 함. 절대 지우지 말 것."""
    return f"media/{instance.ktheme.id}/{filename}"


# id는 사용자가 직접 입력하지만, 그대로 파일시스템 경로로 쓰이기 때문에
# 영문/숫자/-/_ 로만 제한한다 (path traversal 방지).
THEME_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,50}$")


def validate_theme_id(value):
    if not THEME_ID_PATTERN.fullmatch(value):
        raise ValidationError(
            "테마 ID는 영문자, 숫자, '-', '_'만 사용할 수 있고 50자 이하여야 합니다."
        )


class Ktheme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        validators=[validate_theme_id],
    )
    name = models.CharField(max_length=50, verbose_name="테마 이름")

    def __str__(self):
        return f"{self.name}"


class CssColor(models.Model):
    ktheme = models.OneToOneField(
        Ktheme, on_delete=models.CASCADE, related_name="css_color"
    )
    bg_color = models.CharField(max_length=7, default="#FFFFFF", verbose_name="배경")
    main_text_color = models.CharField(
        max_length=7, default="#000000", verbose_name="메인 텍스트"
    )
    point_text_color = models.CharField(
        max_length=7, default="#414141", verbose_name="강조 텍스트"
    )
    input_bg_color = models.CharField(
        max_length=7, default="#D3D3D3", verbose_name="입력창"
    )
    receive_text_color = models.CharField(
        max_length=7, default="#000001", verbose_name="받은 말풍선 텍스트"
    )
    send_text_color = models.CharField(
        max_length=7, default="#000002", verbose_name="보낸 말풍선 텍스트"
    )


class CssBubble(models.Model):
    ktheme = models.OneToOneField(
        Ktheme, on_delete=models.CASCADE, related_name="css_bubble"
    )
    r_1_x = models.PositiveIntegerField(default=25)
    r_1_y = models.PositiveIntegerField(default=25)
    r_1_t = models.PositiveIntegerField(default=15)
    r_1_l = models.PositiveIntegerField(default=20)
    r_1_b = models.PositiveIntegerField(default=15)
    r_1_r = models.PositiveIntegerField(default=20)

    r_2_x = models.PositiveIntegerField(default=25)
    r_2_y = models.PositiveIntegerField(default=25)
    r_2_t = models.PositiveIntegerField(default=15)
    r_2_l = models.PositiveIntegerField(default=20)
    r_2_b = models.PositiveIntegerField(default=15)
    r_2_r = models.PositiveIntegerField(default=20)

    s_1_x = models.PositiveIntegerField(default=25)
    s_1_y = models.PositiveIntegerField(default=25)
    s_1_t = models.PositiveIntegerField(default=15)
    s_1_l = models.PositiveIntegerField(default=20)
    s_1_b = models.PositiveIntegerField(default=15)
    s_1_r = models.PositiveIntegerField(default=20)

    s_2_x = models.PositiveIntegerField(default=25)
    s_2_y = models.PositiveIntegerField(default=25)
    s_2_t = models.PositiveIntegerField(default=15)
    s_2_l = models.PositiveIntegerField(default=20)
    s_2_b = models.PositiveIntegerField(default=15)
    s_2_r = models.PositiveIntegerField(default=20)


@receiver(post_save, sender=Ktheme)
def create_css_model(sender, instance, created, **kwargs):
    if created:
        CssColor.objects.create(ktheme=instance)
        CssBubble.objects.create(ktheme=instance)


@receiver(post_save, sender=Ktheme)
def create_theme_dir(sender, instance, created, **kwargs):
    if not created:
        return

    # id는 이미 validate_theme_id로 검증됐지만, 파일시스템 접근 직전에
    # 한 번 더 안전 경로인지 확인 (defense in depth).
    theme_dir = safe_theme_dir(instance.id)
    theme_image_dir = os.path.join(theme_dir, "Images")
    theme_css = os.path.join(theme_dir, "KakaoTalkTheme.css")

    if os.path.exists(theme_dir):
        return

    default_image_dir = get_default_images_dir()
    shutil.copytree(default_image_dir, theme_image_dir)
    shutil.copy2(get_css_template_path(), theme_css)