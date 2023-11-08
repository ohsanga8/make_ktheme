from django import forms
from .models import Ktheme, CssColor, CssBubble

# from .models import KthemeImage


class KthemeImageForm(forms.Form):
    image = forms.ImageField(required=True)


class AnyForm(forms.Form):
    any = forms.CharField()


class KthemeCreateForm(forms.ModelForm):
    class Meta:
        model = Ktheme
        fields = ("id", "name")

    # def save(self, commit=True, user=None):
    #     instance = super(KthemeCreateForm, self).save(commit=False)
    #     if user:
    #         instance.user = user
    #     if commit:
    #         instance.save()
    #     return instance


class KthemeUpdateForm(forms.ModelForm):
    class Meta:
        model = Ktheme
        fields = ("name",)


# class KthemeImageForm(forms.ModelForm):
#     class Meta:
#         model = KthemeImage


# class KthemeImagesForm(forms.ModelForm):
#     class Meta:
#         model = KthemeImages
#         fields = (
#             "chat_bg",
#             "chat_bubble_r_1",
#             "chat_bubble_r_2",
#             "chat_bubble_s_1",
#             "chat_bubble_s_2",
#             "theme_icon",
#             "main_bg",
#             "tab_bg",
#             "tab_ico_1",
#             "tab_ico_2",
#             "tab_ico_3",
#             "tab_ico_4",
#             "tab_ico_5",
#             "tab_ico_s_1",
#             "tab_ico_s_2",
#             "tab_ico_s_3",
#             "tab_ico_s_4",
#             "tab_ico_s_5",
#             "passcode_bg",
#             "passcode_1",
#             "passcode_2",
#             "passcode_3",
#             "passcode_4",
#             "passcode_s_1",
#             "passcode_s_2",
#             "passcode_s_3",
#             "passcode_s_4",
#             "passcode_pressed",
#             "profile_img",
#         )


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
        fields = (
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
        )

        widgets = {
            "s_1_x": forms.NumberInput(
                attrs={"id": "x-1", "name": "x-1", "style": "width:100px;"}
            ),
            "s_1_y": forms.NumberInput(
                attrs={"id": "y-1", "name": "y-1", "style": "width:100px;"}
            ),
            "s_1_t": forms.NumberInput(
                attrs={"id": "t-1", "name": "t-1", "style": "width:100px;"}
            ),
            "s_1_l": forms.NumberInput(
                attrs={"id": "l-1", "name": "l-1", "style": "width:100px;"}
            ),
            "s_1_b": forms.NumberInput(
                attrs={"id": "b-1", "name": "b-1", "style": "width:100px;"}
            ),
            "s_1_r": forms.NumberInput(
                attrs={"id": "r-1", "name": "r-1", "style": "width:100px;"}
            ),
            "s_2_x": forms.NumberInput(
                attrs={"id": "x-2", "name": "x-2", "style": "width:100px;"}
            ),
            "s_2_y": forms.NumberInput(
                attrs={"id": "y-2", "name": "y-2", "style": "width:100px;"}
            ),
            "s_2_t": forms.NumberInput(
                attrs={"id": "t-2", "name": "t-2", "style": "width:100px;"}
            ),
            "s_2_l": forms.NumberInput(
                attrs={"id": "l-2", "name": "l-2", "style": "width:100px;"}
            ),
            "s_2_b": forms.NumberInput(
                attrs={"id": "b-2", "name": "b-2", "style": "width:100px;"}
            ),
            "s_2_r": forms.NumberInput(
                attrs={"id": "r-2", "name": "r-2", "style": "width:100px;"}
            ),
            "r_1_x": forms.NumberInput(
                attrs={"id": "x-3", "name": "x-3", "style": "width:100px;"}
            ),
            "r_1_y": forms.NumberInput(
                attrs={"id": "y-3", "name": "y-3", "style": "width:100px;"}
            ),
            "r_1_t": forms.NumberInput(
                attrs={"id": "t-3", "name": "t-3", "style": "width:100px;"}
            ),
            "r_1_l": forms.NumberInput(
                attrs={"id": "l-3", "name": "l-3", "style": "width:100px;"}
            ),
            "r_1_b": forms.NumberInput(
                attrs={"id": "b-3", "name": "b-3", "style": "width:100px;"}
            ),
            "r_1_r": forms.NumberInput(
                attrs={"id": "r-3", "name": "r-3", "style": "width:100px;"}
            ),
            "r_2_x": forms.NumberInput(
                attrs={"id": "x-4", "name": "x-4", "style": "width:100px;"}
            ),
            "r_2_y": forms.NumberInput(
                attrs={"id": "y-4", "name": "y-4", "style": "width:100px;"}
            ),
            "r_2_t": forms.NumberInput(
                attrs={"id": "t-4", "name": "t-4", "style": "width:100px;"}
            ),
            "r_2_l": forms.NumberInput(
                attrs={"id": "l-4", "name": "l-4", "style": "width:100px;"}
            ),
            "r_2_b": forms.NumberInput(
                attrs={"id": "b-4", "name": "b-4", "style": "width:100px;"}
            ),
            "r_2_r": forms.NumberInput(
                attrs={"id": "r-4", "name": "r-4", "style": "width:100px;"}
            ),
        }
