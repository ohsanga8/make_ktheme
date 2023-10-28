from django import forms
from .models import Ktheme, CssColor, CssBubble, KthemeImages

# from .models import KthemeImage


class KthemeImageForm(forms.Form):
    image = forms.ImageField(required=True)


class AnyForm(forms.Form):
    any = forms.CharField()


class KthemeCreateForm(forms.ModelForm):
    class Meta:
        model = Ktheme
        fields = ("id", "name")

    def save(self, commit=True, user=None):
        instance = super(KthemeCreateForm, self).save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class KthemeUpdateForm(forms.ModelForm):
    class Meta:
        model = Ktheme
        fields = ("name",)


class KthemeImagesForm(forms.ModelForm):
    class Meta:
        model = KthemeImages
        fields = (
            "chat_bg",
            "chat_bubble_r_1",
            "chat_bubble_r_2",
            "chat_bubble_s_1",
            "chat_bubble_s_2",
            "theme_icon",
            "main_bg",
            "tab_bg",
            "tab_ico_1",
            "tab_ico_2",
            "tab_ico_3",
            "tab_ico_4",
            "tab_ico_5",
            "tab_ico_s_1",
            "tab_ico_s_2",
            "tab_ico_s_3",
            "tab_ico_s_4",
            "tab_ico_s_5",
            "passcode_bg",
            "passcode_1",
            "passcode_2",
            "passcode_3",
            "passcode_4",
            "passcode_s_1",
            "passcode_s_2",
            "passcode_s_3",
            "passcode_s_4",
            "passcode_pressed",
            "profile_img",
        )
    ],
    "passcode_pressed": [
        "passcodeKeypadPressed@3x.png",
    ],
    "profile_img": [
        "profileImg01@3x.png",
    ],


class CssColorUpdateForm(forms.ModelForm):
    class Meta:
        model = CssColor
        fields = (
            "bg_color",
            "main_text_color",
            "point_text_color",
            "input_bg_color",
            "send_text_color",
            "receive_text_color",
        )


class CssBubbleUpdateForm(forms.ModelForm):
    class Meta:
        model = CssBubble
        fields = {
            "s_1_x",
            "s_1_y",
            "s_1_t",
            "s_1_l",
            "s_1_b",
            "s_1_r",
            "s_2_x",
            "s_2_y",
            "s_2_t",
            "s_2_l",
            "s_2_b",
            "s_2_r",
            "r_1_x",
            "r_1_y",
            "r_1_t",
            "r_1_l",
            "r_1_b",
            "r_1_r",
            "r_2_x",
            "r_2_y",
            "r_2_t",
            "r_2_l",
            "r_2_b",
            "r_2_r",
        }
