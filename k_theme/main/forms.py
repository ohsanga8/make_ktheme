from django import forms
from django.core.exceptions import ValidationError

from .models import Ktheme, CssColor, CssBubble, THEME_ID_PATTERN


class KthemeCreateForm(forms.ModelForm):
    class Meta:
        model = Ktheme
        # fields = ("id", "name")
        fields = ("name",)

    # def clean_id(self):
    #     value = self.cleaned_data["id"]
    #     if not THEME_ID_PATTERN.fullmatch(value):
    #         raise ValidationError(
    #             "테마 ID는 영문자, 숫자, '-', '_'만 사용할 수 있고 50자 이하여야 합니다."
    #         )
    #     if Ktheme.objects.filter(pk=value).exists():
    #         raise ValidationError("이미 사용 중인 테마 ID입니다.")
    #     return value


class KthemeUpdateForm(forms.ModelForm):
    class Meta:
        model = Ktheme
        fields = ("name",)


class KthemeImageForm(forms.Form):
    """참고: 실제 업로드 처리는 이 폼이 아니라 constants.py의
    all_images_flat() 딕셔너리(한글 키) 기준으로 request.FILES에서
    직접 꺼내 utils.validate_uploaded_image()로 검증한다.
    (템플릿의 <input name="...">이 한글 라벨을 그대로 쓰기 때문)
    이 폼은 더 이상 실제 검증에 관여하지 않으므로 필요 없다면 제거해도 무방하다."""
    pass


class CssColorUpdateForm(forms.ModelForm):
    class Meta:
        model = CssColor
        fields = (
            "bg_color",
            "main_text_color",
            "point_text_color",
            "input_bg_color",
            "receive_text_color",
            "send_text_color",
        )


class CssBubbleUpdateForm(forms.ModelForm):
    class Meta:
        model = CssBubble
        fields = (
            "r_1_x", "r_1_y", "r_1_t", "r_1_l", "r_1_b", "r_1_r",
            "r_2_x", "r_2_y", "r_2_t", "r_2_l", "r_2_b", "r_2_r",
            "s_1_x", "s_1_y", "s_1_t", "s_1_l", "s_1_b", "s_1_r",
            "s_2_x", "s_2_y", "s_2_t", "s_2_l", "s_2_b", "s_2_r",
        )
        labels = {
            "r_1_x": "x", "r_1_y": "y", "r_1_t": "top", "r_1_l": "left",
            "r_1_b": "bottom", "r_1_r": "right",
            "r_2_x": "x", "r_2_y": "y", "r_2_t": "top", "r_2_l": "left",
            "r_2_b": "bottom", "r_2_r": "right",
            "s_1_x": "x", "s_1_y": "y", "s_1_t": "top", "s_1_l": "left",
            "s_1_b": "bottom", "s_1_r": "right",
            "s_2_x": "x", "s_2_y": "y", "s_2_t": "top", "s_2_l": "left",
            "s_2_b": "bottom", "s_2_r": "right",
        }
        widgets = {
            "r_1_x": forms.NumberInput(attrs={"id": "x-1", "name": "x-1", "style": "width:40px;"}),
            "r_1_y": forms.NumberInput(attrs={"id": "y-1", "name": "y-1", "style": "width:40px;"}),
            "r_1_t": forms.NumberInput(attrs={"id": "t-1", "name": "t-1", "style": "width:40px;"}),
            "r_1_l": forms.NumberInput(attrs={"id": "l-1", "name": "l-1", "style": "width:40px;"}),
            "r_1_b": forms.NumberInput(attrs={"id": "b-1", "name": "b-1", "style": "width:40px;"}),
            "r_1_r": forms.NumberInput(attrs={"id": "r-1", "name": "r-1", "style": "width:40px;"}),
            "r_2_x": forms.NumberInput(attrs={"id": "x-2", "name": "x-2", "style": "width:40px;"}),
            "r_2_y": forms.NumberInput(attrs={"id": "y-2", "name": "y-2", "style": "width:40px;"}),
            "r_2_t": forms.NumberInput(attrs={"id": "t-2", "name": "t-2", "style": "width:40px;"}),
            "r_2_l": forms.NumberInput(attrs={"id": "l-2", "name": "l-2", "style": "width:40px;"}),
            "r_2_b": forms.NumberInput(attrs={"id": "b-2", "name": "b-2", "style": "width:40px;"}),
            "r_2_r": forms.NumberInput(attrs={"id": "r-2", "name": "r-2", "style": "width:40px;"}),
            "s_1_x": forms.NumberInput(attrs={"id": "x-3", "name": "x-3", "style": "width:40px;"}),
            "s_1_y": forms.NumberInput(attrs={"id": "y-3", "name": "y-3", "style": "width:40px;"}),
            "s_1_t": forms.NumberInput(attrs={"id": "t-3", "name": "t-3", "style": "width:40px;"}),
            "s_1_l": forms.NumberInput(attrs={"id": "l-3", "name": "l-3", "style": "width:40px;"}),
            "s_1_b": forms.NumberInput(attrs={"id": "b-3", "name": "b-3", "style": "width:40px;"}),
            "s_1_r": forms.NumberInput(attrs={"id": "r-3", "name": "r-3", "style": "width:40px;"}),
            "s_2_x": forms.NumberInput(attrs={"id": "x-4", "name": "x-4", "style": "width:40px;"}),
            "s_2_y": forms.NumberInput(attrs={"id": "y-4", "name": "y-4", "style": "width:40px;"}),
            "s_2_t": forms.NumberInput(attrs={"id": "t-4", "name": "t-4", "style": "width:40px;"}),
            "s_2_l": forms.NumberInput(attrs={"id": "l-4", "name": "l-4", "style": "width:40px;"}),
            "s_2_b": forms.NumberInput(attrs={"id": "b-4", "name": "b-4", "style": "width:40px;"}),
            "s_2_r": forms.NumberInput(attrs={"id": "r-4", "name": "r-4", "style": "width:40px;"}),
        }