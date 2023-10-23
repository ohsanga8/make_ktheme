from django import forms
from .models import Ktheme, CssColor, CssBubble

# from .models import KthemeImage


class KthemeImageForm(forms.Form):
    image = forms.ImageField(required=True)


class KthemeForm(forms.Form):
    class Meta:
        model = Ktheme
        fields = ("theme_id", "theme_name")


class CssColorForm(forms.Form):
    class Meta:
        model = CssColor
        fields = "__all__"


class CssBubbleForm(forms.Form):
    class Meta:
        model = CssBubble
        fields = "__all__"
