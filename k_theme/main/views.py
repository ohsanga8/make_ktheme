from django.shortcuts import render, get_object_or_404

# from make_ktheme.models import Ktheme
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
import os
import zipfile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import (
    # KthemeImageForm,
    KthemeCreateForm,
    KthemeUpdateForm,
    CssColorUpdateForm,
    CssBubbleUpdateForm,
    # KthemeImagesForm,
    # AnyForm,
)
from .models import Ktheme, CssColor, CssBubble

# from .models import KthemeImage
from django.conf import settings
from django.http import JsonResponse

# import time
# timestamp = int(time.time())

from django.views.decorators.cache import never_cache

from datetime import datetime

import re


@login_required
def main(request):
    user = request.user
    user_theme_list = Ktheme.objects.filter(user=user)
    if request.method == "POST":
        form = KthemeCreateForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            ktheme = form.save()
            theme_id = ktheme.id
            theme_dir = os.path.join(settings.MEDIA_ROOT, theme_id)
            # src_css_path = os.path.join("static", "source.css")
            theme_css = os.path.join(theme_dir, "KakaoTalkTheme.css")
            # if os.path.exists(ktheme_css_path):
            #     with open(src_css_path, "r", encoding="utf-8") as f:
            #         css_content = f.read()
            #     css_content = css_content.replace("themeId", ktheme.id)
            #     css_content = css_content.replace("themeName", ktheme.name)
            #     with open(ktheme_css_path, "w", encoding="utf-8") as f:
            #         f.write(css_content)

            # return redirect("ktheme_detail", theme_id=theme_id)

            try:
                with open(theme_css, "r") as f:
                    css_content = f.read()
                css_content = css_content.replace("themeId", ktheme.id)
                css_content = css_content.replace("themeName", ktheme.name)
                with open(theme_css, "w") as f:
                    f.write(css_content)
                return redirect("ktheme_detail", id=theme_id)
            except Exception as e:
                print(f"{str(e)}")
    else:
        form = KthemeCreateForm()
    return render(
        request,
        "main/main.html",
        {"user_theme_list": user_theme_list, "form": form},
    )


# @login_required
# def create_theme(request):
#     if request.method == "POST":
#         form = KthemeCreateForm(request.POST)
#         if form.is_valid():
#             ktheme = form.save()
#             theme_id = ktheme.id
#             theme_css = os.path.join(
#                 settings.MEDIA_ROOT, theme_id, "KakaoTalkTheme.css"
#             )

#             try:
#                 with open(theme_css, "r") as f:
#                     css_content = f.read()
#                 css_content = css_content.replace("themeId", ktheme.id)
#                 css_content = css_content.replace("themeName", ktheme.name)
#                 with open(theme_css, "w") as f:
#                     f.write(css_content)
#                 return redirect("ktheme_detail", id=theme_id)
#             except Exception as e:
#                 print(f"{str(e)}")
#             # if os.path.exists(theme_css):
#             #     with open(src_css_path, "r", encoding="utf-8") as f:
#             #         css_content = f.read()
#             #     css_content = css_content.replace("themeId", ktheme.id)
#             #     css_content = css_content.replace("themeName", ktheme.name)
#             #     with open(ktheme_css_path, "w", encoding="utf-8") as f:
#             #         f.write(css_content)
#             # return redirect("ktheme_detail", id=theme_id)
#     else:
#         form = KthemeCreateForm()
#     return render(request, "main/create_theme.html", {"form": form})


def ktheme_detail(request, id):
    version = str(int(datetime.now().timestamp()))

    ktheme = Ktheme.objects.get(pk=id)
    theme_id = ktheme.id

    css_color = CssColor.objects.get(ktheme=ktheme)
    css_bubble = CssBubble.objects.get(ktheme=ktheme)

    # src_css = os.path.join("static", "source.css")
    theme_dir = os.path.join(settings.MEDIA_ROOT, theme_id)
    theme_css = os.path.join(theme_dir, "KakaoTalkTheme.css")
    theme_images_dir = os.path.join(theme_dir, "Images")

    action = request.POST.get("action", "")

    if request.method == "POST":
        ktheme_update_form = KthemeUpdateForm(request.POST, instance=ktheme)
        # ktheme_images_form = KthemeImagesForm(request.POST, instance=ktheme_images)
        css_color_update_form = CssColorUpdateForm(request.POST, instance=css_color)
        css_bubble_update_form = CssBubbleUpdateForm(request.POST, instance=css_bubble)

        if action == "ktheme_update":
            if ktheme_update_form.is_valid():
                ktheme = ktheme_update_form.save()
                theme_name = ktheme.name
                with open(theme_css, "r", encoding="utf-8") as f:
                    css_content = f.read()
                css_content = css_content.replace("themeName", theme_name)
                with open(theme_css, "w", encoding="utf-8") as f:
                    f.write(css_content)

        elif action == "upload_image":
            image_upload = request.FILES["image_upload"]
            if image_upload:
                image_path = request.POST.get("image_path")
                if image_path.startswith("/"):
                    image_path = image_path[1:]

                with open(image_path, "wb") as destination:
                    for chunk in image_upload.chunks():
                        destination.write(chunk)

        elif action == "css_color":
            if css_color_update_form.is_valid():
                bg_color = css_color_update_form.cleaned_data["bg_color"]
                main_text_color = css_color_update_form.cleaned_data["main_text_color"]
                point_text_color = css_color_update_form.cleaned_data[
                    "point_text_color"
                ]
                input_bg_color = css_color_update_form.cleaned_data["input_bg_color"]
                send_text_color = css_color_update_form.cleaned_data["send_text_color"]
                receive_text_color = css_color_update_form.cleaned_data[
                    "receive_text_color"
                ]

                color_replacement = {
                    bg_color: css_color.bg_color,
                    main_text_color: css_color.main_text_color,
                    point_text_color: css_color.point_text_color,
                    input_bg_color: css_color.input_bg_color,
                    send_text_color: css_color.send_text_color,
                    receive_text_color: css_color.receive_text_color,
                }

                with open(theme_css, "r", encoding="utf-8") as f:
                    css_content = f.read()

                for cur_color, new_color in color_replacement.items():
                    css_content = css_content.replace(cur_color, new_color)

                with open(theme_css, "w", encoding="utf-8") as f:
                    f.write(css_content)

                css_color = css_color_update_form.save()

        elif action == "css_bubble":
            if css_bubble_update_form.is_valid():
                css_bubble = css_bubble_update_form.save()
                with open(theme_css, "r") as f:
                    css_content = f.read()

                replacement_dict = {
                    # send
                    r"-ios-background-image: 'chatroomBubbleSend01.png' (\d+)px (\d+)px;": r'-ios-background-image: "chatroomBubbleSend01.png" {s_1_x}px {s_1_y}px;',
                    r"-ios-selected-background-image: 'chatroomBubbleSend01Selected.png' (\d+)px (\d+)px;": r'-ios-selected-background-image: "chatroomBubbleSend01Selected.png" {s_1_x}px {s_1_y}px;',
                    r"-ios-group-background-image: 'chatroomBubbleSend02.png' (\d+)px (\d+)px;": r"-ios-group-background-image: 'chatroomBubbleSend02.png' {s_2_x}px {s_2_y}px;",
                    r"-ios-group-selected-background-image: 'chatroomBubbleSend02Selected.png' (\d+)px (\d+)px;": r"-ios-group-selected-background-image: 'chatroomBubbleSend02Selected.png' {s_2_x}px {s_2_y}px;",
                    r"-ios-title-edgeinsets: (\d+)px (\d+)px (\d+)px (\d+)px;": r"-ios-title-edgeinsets: {s_1_t}px {s_1_l}px {s_1_b}px {s_1_r}px;",
                    r"-ios-group-title-edgeinsets: (\d+)px (\d+)px (\d+)px (\d+)px;": r"-ios-group-title-edgeinsets: {s_2_t}px {s_2_l}px {s_2_b}px {s_2_r}px;",
                    # recieve
                    r"-ios-background-image: 'chatroomBubbleReceive01.png' (\d+)px (\d+)px;": r"-ios-background-image: 'chatroomBubbleReceive01.png' {r_1_x}px {r_1_y}px;",
                    r"-ios-selected-background-image: 'chatroomBubbleReceive01Selected.png' (\d+)px (\d+)px;": r"-ios-selected-background-image: 'chatroomBubbleReceive01Selected.png' {r_1_x}px {r_1_y}px;",
                    r"-ios-group-background-image: 'chatroomBubbleReceive02.png' (\d+)px (\d+)px;": r"-ios-group-background-image: 'chatroomBubbleReceive02.png' {r_2_x}px {r_2_y}px;",
                    r"-ios-group-selected-background-image: 'chatroomBubbleReceive02Selected.png' (\d+)px (\d+)px;": r"-ios-group-selected-background-image: 'chatroomBubbleReceive02Selected.png' {r_2_x}px {r_2_y}px;",
                    r"-ios-title-edgeinsets: (\d+)px (\d+)px (\d+)px (\d+)px;": r"-ios-title-edgeinsets: {r_1_t}px {r_1_l}px {r_1_b}px {r_1_r}px;",
                    r"-ios-group-title-edgeinsets: (\d+)px (\d+)px (\d+)px (\d+)px;": r"-ios-group-title-edgeinsets: {r_1_t}px {r_1_l}px {r_1_b}px {r_1_r}px;",
                }

                for pattern, replacement in replacement_dict.items():
                    css_content = re.sub(pattern, replacement, css_content)

                with open(theme_css, "w") as f:
                    f.write(css_content)

        elif action == "create_zip":
            theme_zip = os.path.join(theme_dir, f"{theme_name}.ktheme")
            with zipfile.ZipFile(theme_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(theme_css, os.path.basename(theme_css))
                directory_subdir = "Images"
                for root, _, files in os.walk(theme_images_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, theme_images_dir)
                        zipf.write(file_path, os.path.join(directory_subdir, arcname))
    else:
        ktheme_update_form = KthemeUpdateForm()
        css_color_update_form = CssColorUpdateForm()
        css_bubble_update_form = CssBubbleUpdateForm()
    initial_name = {"name": ktheme.name}
    initial_color = {
        "bg_color": css_color.bg_color,
        "main_text_color": css_color.main_text_color,
        "point_text_color": css_color.point_text_color,
        "input_bg_color": css_color.input_bg_color,
        "send_text_color": css_color.send_text_color,
        "receive_text_color": css_color.receive_text_color,
    }
    initial_bubble = {
        "s_1_x": css_bubble.s_1_x,
        "s_1_y": css_bubble.s_1_y,
        "s_1_t": css_bubble.s_1_t,
        "s_1_l": css_bubble.s_1_l,
        "s_1_b": css_bubble.s_1_b,
        "s_1_r": css_bubble.s_1_r,
        "s_2_x": css_bubble.s_2_x,
        "s_2_y": css_bubble.s_2_y,
        "s_2_t": css_bubble.s_2_t,
        "s_2_l": css_bubble.s_2_l,
        "s_2_b": css_bubble.s_2_b,
        "s_2_r": css_bubble.s_2_r,
        "r_1_x": css_bubble.r_1_x,
        "r_1_y": css_bubble.r_1_y,
        "r_1_t": css_bubble.r_1_t,
        "r_1_l": css_bubble.r_1_l,
        "r_1_b": css_bubble.r_1_b,
        "r_1_r": css_bubble.r_1_r,
        "r_2_x": css_bubble.r_2_x,
        "r_2_y": css_bubble.r_2_y,
        "r_2_t": css_bubble.r_2_t,
        "r_2_l": css_bubble.r_2_l,
        "r_2_b": css_bubble.r_2_b,
        "r_2_r": css_bubble.r_2_r,
    }
    ktheme_update_form = KthemeUpdateForm(instance=ktheme, initial=initial_name)
    css_color_update_form = CssColorUpdateForm(
        instance=css_color, initial=initial_color
    )
    css_bubble_update_form = CssBubbleUpdateForm(
        instance=css_bubble, initial=initial_bubble
    )
    image_filenames = [
        "chatroomBgImage@3x.png",
        "chatroomBubbleReceive01@2x.png",
        "chatroomBubbleReceive01@3x.png",
        "chatroomBubbleReceive01Selected@2x.png",
        "chatroomBubbleReceive01Selected@3x.png",
        "chatroomBubbleReceive02@2x.png",
        "chatroomBubbleReceive02@3x.png",
        "chatroomBubbleReceive02Selected@2x.png",
        "chatroomBubbleReceive02Selected@3x.png",
        "chatroomBubbleSend01@2x.png",
        "chatroomBubbleSend01@3x.png",
        "chatroomBubbleSend01Selected@2x.png",
        "chatroomBubbleSend01Selected@3x.png",
        "chatroomBubbleSend02@2x.png",
        "chatroomBubbleSend02@3x.png",
        "chatroomBubbleSend02Selected@2x.png",
        "chatroomBubbleSend02Selected@3x.png",
        "commonIcoTheme.png",
        "findBtnAddFriend@2x.png",
        "findBtnAddFriend@3x.png",
        "mainBgImage@3x.png",
        "maintabBgImage@2x.png",
        "maintabBgImage@3x.png",
        "maintabIcoBrowse@2x.png",
        "maintabIcoBrowse@3x.png",
        "maintabIcoBrowseSelected@2x.png",
        "maintabIcoBrowseSelected@3x.png",
        "maintabIcoCall@2x.png",
        "maintabIcoCall@3x.png",
        "maintabIcoCallSelected@2x.png",
        "maintabIcoCallSelected@3x.png",
        "maintabIcoChats@2x.png",
        "maintabIcoChats@3x.png",
        "maintabIcoChatsSelected@2x.png",
        "maintabIcoChatsSelected@3x.png",
        "maintabIcoFind@2x.png",
        "maintabIcoFind@3x.png",
        "maintabIcoFindSelected@2x.png",
        "maintabIcoFindSelected@3x.png",
        "maintabIcoFriends@2x.png",
        "maintabIcoFriends@3x.png",
        "maintabIcoFriendsSelected@2x.png",
        "maintabIcoFriendsSelected@3x.png",
        "maintabIcoMore@2x.png",
        "maintabIcoMore@3x.png",
        "maintabIcoMoreSelected@2x.png",
        "maintabIcoMoreSelected@3x.png",
        "maintabIcoOpenChats@2x.png",
        "maintabIcoOpenChats@3x.png",
        "maintabIcoOpenChatsSelected@2x.png",
        "maintabIcoOpenChatsSelected@3x.png",
        "maintabIcoPiccoma@2x.png",
        "maintabIcoPiccoma@3x.png",
        "maintabIcoPiccomaSelected@2x.png",
        "maintabIcoPiccomaSelected@3x.png",
        "maintabIcoShopping@2x.png",
        "maintabIcoShopping@3x.png",
        "maintabIcoShoppingSelected@2x.png",
        "maintabIcoShoppingSelected@3x.png",
        "maintabIcoView@2x.png",
        "maintabIcoView@3x.png",
        "maintabIcoViewSelected@2x.png",
        "maintabIcoViewSelected@3x.png",
        "passcodeBgImage@3x.png",
        "passcodeImgCode01@3x.png",
        "passcodeImgCode01Selected@3x.png",
        "passcodeImgCode02@3x.png",
        "passcodeImgCode02Selected@3x.png",
        "passcodeImgCode03@3x.png",
        "passcodeImgCode03Selected@3x.png",
        "passcodeImgCode04@3x.png",
        "passcodeImgCode04Selected@3x.png",
        "passcodeKeypadPressed@3x.png",
        "profileImg01@3x.png",
    ]
    image_paths = [
        f"/media/{theme_id}/Images/{filename}" for filename in image_filenames
    ]
    bubble_filenames = [
        "chatroomBubbleSend01@3x.png",
        "chatroomBubbleSend02@3x.png",
        "chatroomBubbleReceive01@3x.png",
        "chatroomBubbleReceive02@3x.png",
    ]
    bubble_image_paths = [
        f"/media/{theme_id}/Images/{filename}" for filename in bubble_filenames
    ]

    return render(
        request,
        "main/ktheme_detail.html",
        {
            "version": version,
            "ktheme": ktheme,
            # "ktheme_images": ktheme_images,
            "ktheme_update_form": ktheme_update_form,
            "image_paths": image_paths,
            "bubble_image_paths": bubble_image_paths,
            # "ktheme_images_form": ktheme_images_form,
            "css_color_update_form": css_color_update_form,
            "css_bubble_update_form": css_bubble_update_form,
        },
    )


def zip_css_and_directory(css_file, source_directory, output_zip_path):
    theme_css = os.path.join(settings.MEDIA_ROOT, "KakaoTalkTheme.css")
    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(css_file, os.path.basename(css_file))
        directory_subdir = "Images"

        for root, _, files in os.walk(source_directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_directory)
                zipf.write(file_path, os.path.join(directory_subdir, arcname))


def create_zip(request):
    images = KthemeImage.objects.all()
    if images:
        zip_filename = "image_zip.zip"
        zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)
        with zipfile.ZipFile(zip_path, "w") as zipf:
            for image in images:
                image_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
                zipf.write(image_path, os.path.basename(image_path))

        with open(zip_path, "rb") as zip_file:
            response = HttpResponse(zip_file.read(), content_type="application/zip")
            response["Content-Disposition"] = f'attachment; filename="{zip_filename}"'
            return response
    return redirect("main")
