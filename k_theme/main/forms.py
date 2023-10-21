from django import forms

# from .models import KthemeImage


class KthemeImageForm(forms.Form):
    image = forms.ImageField(required=True)


# class KthemeImageForm(forms.ModelForm):
#     class Meta:
#         model = KthemeImage
#         fields = (
#             "image1",
#             # "image2",
#             # "image3",
#             # "image4",
#             # "image5",
#             # "image6",
#             # "image7",
#             # "image8",
#             # "image9",
#             # "image10",
#         )


# image1 = forms.ImageField(required=False)
# image2 = forms.ImageField(required=False)
# image3 = forms.ImageField(required=False)
# image4 = forms.ImageField(required=False)
# image5 = forms.ImageField(required=False)
# image6 = forms.ImageField(required=False)
# image7 = forms.ImageField(required=False)
# image8 = forms.ImageField(required=False)
# image9 = forms.ImageField(required=False)
# image10 = forms.ImageField(required=False)


class cssForm(forms.Form):
    bg_color = forms.CharField(label="bg color", max_length=7)
    text_color = forms.CharField(label="text color", max_length=7)
