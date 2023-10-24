# from django import forms
# from .models import Ktheme, CssColor, CssBubble

# # from .models import KthemeImage


# class KthemeImageForm(forms.Form):
#     image = forms.ImageField(required=True)


# class KthemeForm(forms.Form):
#     class Meta:
#         model = Ktheme
#         fields = ("theme_id", "theme_name")


# class CssColorForm(forms.Form):
#     class Meta:
#         model = CssColor
#         fields = "__all__"


# class CssBubbleForm(forms.Form):
#     class Meta:
#         model = CssBubble
#         fields = "__all__"


# # class KthemeImageForm(forms.ModelForm):
# #     class Meta:
# #         model = KthemeImage
# #         fields = (
# #             "image1",
# #             # "image2",
# #             # "image3",
# #             # "image4",
# #             # "image5",
# #             # "image6",
# #             # "image6",
# #             # "image8",
# #             # "image9",
# #             # "image10",
# #         )


# # image1 = forms.ImageField(required=False)
# # image2 = forms.ImageField(required=False)
# # image3 = forms.ImageField(required=False)
# # image4 = forms.ImageField(required=False)
# # image5 = forms.ImageField(required=False)
# # image6 = forms.ImageField(required=False)
# # image7 = forms.ImageField(required=False)
# # image8 = forms.ImageField(required=False)
# # image9 = forms.ImageField(required=False)
# # image10 = forms.ImageField(required=False)


# # class cssForm(forms.Form):
# #     theme_id = forms.CharField(label="테마 ID")
# #     theme_name = forms.CharField(label="테마 name")
# #     bg_color = forms.CharField(label="배경", max_length=7)
# #     main_text_color = forms.CharField(label="메인 텍스트", max_length=7)
# #     point_text_color = forms.CharField(label="포인트 텍스트", max_length=7)
# #     input_bg_color = forms.CharField(label="입력창 배경", max_length=7)
# #     send_text_color = forms.CharField(label="보낸 말풍선 텍스트", max_length=7)
# #     receive_text_color = forms.CharField(label="받은 말풍선 텍스트", max_length=7)


# # class bubbleSizeForm(forms.Form):
# #     s_1_x = forms.CharField(label="보낸 말풍선 1 x")
# #     s_1_y = forms.CharField(label="보낸 말풍선 1 y")
# #     s_1_t = forms.CharField(label="보낸 말풍선 1 top")
# #     s_1_l = forms.CharField(label="보낸 말풍선 1 left")
# #     s_1_b = forms.CharField(label="보낸 말풍선 1 bottom")
# #     s_1_r = forms.CharField(label="보낸 말풍선 1 right")

# #     s_2_x = forms.CharField(label="보낸 말풍선 2 x")
# #     s_2_y = forms.CharField(label="보낸 말풍선 2 y")
# #     s_2_t = forms.CharField(label="보낸 말풍선 2 top")
# #     s_2_l = forms.CharField(label="보낸 말풍선 2 left")
# #     s_2_b = forms.CharField(label="보낸 말풍선 2 bottom")
# #     s_2_r = forms.CharField(label="보낸 말풍선 2 right")

# #     r_1_x = forms.CharField(label="받은 말풍선 1 x")
# #     r_1_y = forms.CharField(label="받은 말풍선 1 y")
# #     r_1_t = forms.CharField(label="받은 말풍선 1 top")
# #     r_1_l = forms.CharField(label="받은 말풍선 1 left")
# #     r_1_b = forms.CharField(label="받은 말풍선 1 bottom")
# #     r_1_r = forms.CharField(label="받은 말풍선 1 right")

# #     r_2_x = forms.CharField(label="받은 말풍선 2 x")
# #     r_2_y = forms.CharField(label="받은 말풍선 2 y")
# #     r_2_t = forms.CharField(label="받은 말풍선 2 top")
# #     r_2_l = forms.CharField(label="받은 말풍선 2 left")
# #     r_2_b = forms.CharField(label="받은 말풍선 2 bottom")
# #     r_2_r = forms.CharField(label="받은 말풍선 2 right")
