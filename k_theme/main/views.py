from django.shortcuts import render, get_object_or_404

# from make_ktheme.models import Ktheme
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
import os
import zipfile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import KthemeForm, KthemeImageForm, CssColorForm, CssBubbleForm
from .models import Ktheme, CssColor, CssBubble

# from .models import KthemeImage
from django.conf import settings
from django.http import JsonResponse

# import time
# timestamp = int(time.time())

from django.views.decorators.cache import never_cache

from datetime import datetime


@login_required
def main(request):
    user = request.user
    user_kthemes = Ktheme.objects.filter(user=user)
    return render(request, "main/main.html", {"user_kthemes": user_kthemes})


# static_dir = settings.STATICFILES_DIRS[0]
def create_theme(request):
    if request.method == "POST":
        form = KthemeForm(request.POST)
        if form.is_valid():
            ktheme = form.save()
            return redirect("ktheme_detail")
    else:
        form = KthemeForm()
    return render(request, "main/create_ktheme.html", {"form": form})


def ktheme_detail(request, theme_id):
    ktheme = get_object_or_404(Ktheme, theme_id=theme_id)
    css_color = CssColor.objects.filter(ktheme=ktheme)
    css_bubble = CssBubble.objects.filter(ktheme=ktheme)
    ktheme_form = KthemeForm(request.POST, isinstance=ktheme)
    css_color_form = CssColorForm(request.POST, instance=css_color)
    css_bubble_form = CssBubbleForm(request.POST, instance=css_bubble)
    action = request.POST.get("action", "")

    origin_css = os.path.join("static", "origin.css")
    ktheme_css = os.path.join("media", "KakaoTalkTheme.css")

    if request.method == "POST":
        if action == "ktheme_revise" and ktheme_form.is_valid():
            theme_id = ktheme_form.cleaned_data["theme_id"]
            theme_name = ktheme_form.cleaned_data["theme_name"]
        elif action == "upload_image":
            image_upload = request.FILES["image_upload"]
            if image_upload:
                image_path = request.POST.get("image_path")
                with open(image_path, "wb") as destination:
                    for chunk in image_upload.chunks():
                        destination.write(chunk)

        elif action == "css_color" and css_color_form.is_valid():
            theme_name = css_color_form.cleaned_data["theme_name"]
            bg_color = css_color_form.cleaned_data["bg_color"]
            main_text_color = css_color_form.cleaned_data["main_text_color"]
            point_text_color = css_color_form.cleaned_data["point_text_color"]
            input_bg_color = css_color_form.cleaned_data["input_bg_color"]
            send_text_color = css_color_form.cleaned_data["send_text_color"]
            receive_text_color = css_color_form.cleaned_data["receive_text_color"]

            with open(origin_css, "r", encoding="utf-8") as f:
                original_content = f.read()
            modified_content = (
                original_content.replace("themeId", theme_id)
                .replace("themeName", theme_name)
                .replace("white", bg_color)
                .replace("black", main_text_color)
                .replace("pink", point_text_color)
                .replace("lightgray", input_bg_color)
                .replace("darkgray", send_text_color)
                .replace("gray", receive_text_color)
            )
            with open(ktheme_css, "w", encoding="utf-8") as f:
                f.write(modified_content)

        elif action == "css_bubble" and css_bubble_form.is_valid():
            pass
        # if (
        #     ktheme_form.is_valid()
        #     and css_color_form.is_valid()
        #     and css_bubble_form.is_valid()
        # ):
        #     ktheme_form.save()
        #     css_color_form.save()
        #     css_bubble_form.save()
        #     return redirect("ktheme_detail", theme_id=ktheme.theme_id)
    return render(
        request,
        "ktheme_detail.html",
        {
            "ktheme": ktheme,
            "ktheme_form": ktheme_form,
            "css_color_form": css_color_form,
            "css_bubble_form": css_bubble_form,
        },
    )


@never_cache
def make_theme(request):
    version = str(int(datetime.now().timestamp()))
    img_form = KthemeImageForm(request.POST, request.FILES)
    css_form = CssColorForm(request.POST)
    bubble_size_form = CssBubbleForm(request.POST)
    action = request.POST.get("action", "")
    if request.method == "POST":
        if action == "upload_images":
            image_upload = request.FILES["image_upload"]
            if image_upload:
                image_path = request.POST.get("image_path")
                with open(image_path, "wb") as destination:
                    for chunk in image_upload.chunks():
                        destination.write(chunk)

        elif action == "create_css":
            if css_form.is_valid():
                theme_id = css_form.cleaned_data["theme_id"]
                theme_name = css_form.cleaned_data["theme_name"]
                bg_color = css_form.cleaned_data["bg_color"]
                main_text_color = css_form.cleaned_data["main_text_color"]
                point_text_color = css_form.cleaned_data["point_text_color"]
                input_bg_color = css_form.cleaned_data["input_bg_color"]
                send_text_color = css_form.cleaned_data["send_text_color"]
                receive_text_color = css_form.cleaned_data["receive_text_color"]

                origin_css = os.path.join("static", "origin.css")
                ktheme_css = os.path.join("media", "KakaoTalkTheme.css")
                with open(origin_css, "r", encoding="utf-8") as f:
                    original_content = f.read()
                modified_content = (
                    original_content.replace("themeId", theme_id)
                    .replace("themeName", theme_name)
                    .replace("white", bg_color)
                    .replace("black", main_text_color)
                    .replace("pink", point_text_color)
                    .replace("lightgray", input_bg_color)
                    .replace("darkgray", send_text_color)
                    .replace("gray", receive_text_color)
                )

                with open(ktheme_css, "w", encoding="utf-8") as f:
                    f.write(modified_content)

        elif action == "create_zip":
            css_file_path = os.path.join("media", "KakaoTalkTheme.css")
            source_directory = os.path.join("media", "images")
            output_zip_path = os.path.join("media", "sample.ktheme")
            zip_css_and_directory(css_file_path, source_directory, output_zip_path)

    else:
        img_form = KthemeImageForm()
        css_form = cssForm()

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

    image_paths = [f"media/images/{filename}" for filename in image_filenames]
    modal_filenames = [
        "chatroomBubbleReceive01@3x.png",
        "chatroomBubbleReceive02@3x.png",
        "chatroomBubbleSend01@3x.png",
        "chatroomBubbleSend02@3x.png",
    ]
    modal_image_paths = [f"media/images/{filename}" for filename in modal_filenames]

    return render(
        request,
        "make_ktheme/make_ktheme.html",
        {
            "img_form": img_form,
            "css_form": css_form,
            "bubble_size_form": bubble_size_form,
            # "images": images,
            "version": version,
            "image_paths": image_paths,
            "modal_image_paths": modal_image_paths,
        },
    )


def zip_css_and_directory(css_file, source_directory, output_zip_path):
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
