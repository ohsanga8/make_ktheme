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
