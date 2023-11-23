from django import forms
from .models import Ktheme, CssColor, CssBubble

# from .models import KthemeImage


# class KthemeImageForm(forms.Form):
#     image = forms.ImageField(required=True)


# class AnyForm(forms.Form):
#     any = forms.CharField()


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


class KthemeImageForm(forms.Form):
    chat_bg = forms.ImageField(required=False, label="채팅창 배경")
    chat_bubble_r_1 = forms.ImageField(required=False, label="보낸 말풍선 1")
    chat_bubble_r_2 = forms.ImageField(required=False, label="보낸 말풍선 2")
    chat_bubble_s_1 = forms.ImageField(required=False, label="받은 말풍선 1")
    chat_bubble_s_2 = forms.ImageField(required=False, label="받은 말풍선 2")
    theme_icon = forms.ImageField(required=False, label="테마 아이콘")
    main_bg = forms.ImageField(required=False, label="메인 배경")
    tab_bg = forms.ImageField(required=False, label="탭 배경")
    tab_ico_1 = forms.ImageField(required=False, label="탭 아이콘 1")
    tab_ico_1_s = forms.ImageField(required=False, label="탭 아이콘 1 선택")
    tab_ico_2 = forms.ImageField(required=False, label="탭 아이콘 2")
    tab_ico_2_s = forms.ImageField(required=False, label="탭 아이콘 2 선택")
    tab_ico_3 = forms.ImageField(required=False, label="탭 아이콘 3")
    tab_ico_3_s = forms.ImageField(required=False, label="탭 아이콘 3 선택")
    tab_ico_4 = forms.ImageField(required=False, label="탭 아이콘 4")
    tab_ico_4_s = forms.ImageField(required=False, label="탭 아이콘 4 선택")
    tab_ico_5 = forms.ImageField(required=False, label="탭 아이콘 5")
    tab_ico_5_s = forms.ImageField(required=False, label="탭 아이콘 5 선택")
    passcode_bg = forms.ImageField(required=False, label="암호 입력 배경")
    passcode_img_1 = forms.ImageField(required=False, label="암호 1")
    passcode_img_1_s = forms.ImageField(required=False, label="암호 1 선택")
    passcode_img_2 = forms.ImageField(required=False, label="암호 2")
    passcode_img_2_s = forms.ImageField(required=False, label="암호 2 선택")
    passcode_img_3 = forms.ImageField(required=False, label="암호 3")
    passcode_img_3_s = forms.ImageField(required=False, label="암호 3 선택")
    passcode_img_4 = forms.ImageField(required=False, label="암호 4")
    passcode_img_4_s = forms.ImageField(required=False, label="암호 4 선택")
    passcode_pressed = forms.ImageField(required=False, label="암호 5")
    profile_img = forms.ImageField(required=False, label="암호 5 선택")


#         widgets = {
#             "chat_bg": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-1",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "chat_bubble_r_1": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-2",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "chat_bubble_r_2": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-3",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "chat_bubble_s_1": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-4",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "chat_bubble_s_2": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-5",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "theme_icon": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-6",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "add_friend": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-7",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "main_bg": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-8",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_bg": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-9",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_1": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-10",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_1_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-11",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_2": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-12",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_2_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-13",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_3": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-14",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_3_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-15",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_4": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-16",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_4_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-17",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_5": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-18",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "tab_ico_5_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-19",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_bg": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-20",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_1": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-21",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_1_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-22",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_2": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-23",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_2_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-24",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_3": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-25",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_3_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-26",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_4": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-27",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_img_4_s": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-28",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "passcode_pressed": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-29",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#             "profile_img": forms.FileInput(
#                 attrs={
#                     "name": "image_upload",
#                     "id": "file-input-30",
#                     "class": "image-upload hidden-file-input",
#                 }
#             ),
#         }


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
        )
        labels = {
            "r_1_x": "x",
            "r_1_y": "y",
            "r_1_t": "top",
            "r_1_l": "left",
            "r_1_b": "bottom",
            "r_1_r": "right",
            "r_2_x": "x",
            "r_2_y": "y",
            "r_2_t": "top",
            "r_2_l": "left",
            "r_2_b": "bottom",
            "r_2_r": "right",
            "s_1_x": "x",
            "s_1_y": "y",
            "s_1_t": "top",
            "s_1_l": "left",
            "s_1_b": "bottom",
            "s_1_r": "right",
            "s_2_x": "x",
            "s_2_y": "y",
            "s_2_t": "top",
            "s_2_l": "left",
            "s_2_b": "bottom",
            "s_2_r": "right",
        }

        widgets = {
                        "r_1_x": forms.NumberInput(
                attrs={
                    "id": "x-1",
                    "name": "x-1",
                    "style": "width:40px;",
                }
            ),
            "r_1_y": forms.NumberInput(
                attrs={
                    "id": "y-1",
                    "name": "y-1",
                    "style": "width:40px;",
                }
            ),
            "r_1_t": forms.NumberInput(
                attrs={
                    "id": "t-1",
                    "name": "t-1",
                    "style": "width:40px;",
                }
            ),
            "r_1_l": forms.NumberInput(
                attrs={
                    "id": "l-1",
                    "name": "l-1",
                    "style": "width:40px;",
                }
            ),
            "r_1_b": forms.NumberInput(
                attrs={
                    "id": "b-1",
                    "name": "b-1",
                    "style": "width:40px;",
                }
            ),
            "r_1_r": forms.NumberInput(
                attrs={
                    "id": "r-1",
                    "name": "r-1",
                    "style": "width:40px;",
                }
            ),
            "r_2_x": forms.NumberInput(
                attrs={
                    "id": "x-2",
                    "name": "x-2",
                    "style": "width:40px;",
                }
            ),
            "r_2_y": forms.NumberInput(
                attrs={
                    "id": "y-2",
                    "name": "y-2",
                    "style": "width:40px;",
                }
            ),
            "r_2_t": forms.NumberInput(
                attrs={
                    "id": "t-2",
                    "name": "t-2",
                    "style": "width:40px;",
                }
            ),
            "r_2_l": forms.NumberInput(
                attrs={
                    "id": "l-2",
                    "name": "l-2",
                    "style": "width:40px;",
                }
            ),
            "r_2_b": forms.NumberInput(
                attrs={
                    "id": "b-2",
                    "name": "b-2",
                    "style": "width:40px;",
                }
            ),
            "r_2_r": forms.NumberInput(
                attrs={
                    "id": "r-2",
                    "name": "r-2",
                    "style": "width:40px;",
                }
            ),
            "s_1_x": forms.NumberInput(
                attrs={
                    "id": "x-3",
                    "name": "x-3",
                    "style": "width:40px;",
                }
            ),
            "s_1_y": forms.NumberInput(
                attrs={
                    "id": "y-3",
                    "name": "y-3",
                    "style": "width:40px;",
                }
            ),
            "s_1_t": forms.NumberInput(
                attrs={
                    "id": "t-3",
                    "name": "t-3",
                    "style": "width:40px;",
                }
            ),
            "s_1_l": forms.NumberInput(
                attrs={
                    "id": "l-3",
                    "name": "l-3",
                    "style": "width:40px;",
                }
            ),
            "s_1_b": forms.NumberInput(
                attrs={
                    "id": "b-3",
                    "name": "b-3",
                    "style": "width:40px;",
                }
            ),
            "s_1_r": forms.NumberInput(
                attrs={
                    "id": "r-3",
                    "name": "r-3",
                    "style": "width:40px;",
                }
            ),
            "s_2_x": forms.NumberInput(
                attrs={
                    "id": "x-4",
                    "name": "x-4",
                    "style": "width:40px;",
                }
            ),
            "s_2_y": forms.NumberInput(
                attrs={
                    "id": "y-4",
                    "name": "y-4",
                    "style": "width:40px;",
                }
            ),
            "s_2_t": forms.NumberInput(
                attrs={
                    "id": "t-4",
                    "name": "t-4",
                    "style": "width:40px;",
                }
            ),
            "s_2_l": forms.NumberInput(
                attrs={
                    "id": "l-4",
                    "name": "l-4",
                    "style": "width:40px;",
                }
            ),
            "s_2_b": forms.NumberInput(
                attrs={
                    "id": "b-4",
                    "name": "b-4",
                    "style": "width:40px;",
                }
            ),
            "s_2_r": forms.NumberInput(
                attrs={
                    "id": "r-4",
                    "name": "r-4",
                    "style": "width:40px;",
                }
            ),

        }
