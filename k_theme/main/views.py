import os
import uuid
from datetime import datetime
from urllib.parse import quote
import shutil

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from PIL import Image

from .constants import (
    CHAT_IMG_DIC,
    ICON_IMG_DIC,
    MAIN_IMG_DIC,
    PASSCODE_IMG_DIC,
    BUBBLE_PREVIEW_FILENAMES,
    all_images_flat,
)
from .forms import (
    CssBubbleUpdateForm,
    CssColorUpdateForm,
    KthemeCreateForm,
    KthemeImageForm,
    KthemeUpdateForm,
)
from .models import CssBubble, CssColor, Ktheme
from .utils import (
    InvalidImageError,
    apply_bubble_css,
    apply_color_theme,
    apply_theme_identity,
    build_theme_zip,
    ensure_theme_dirs,
    get_css_template_path,
    theme_paths,
    validate_uploaded_image,
)


def _get_owned_theme(request, theme_pk):
    """소유권 검증 포함 조회. 남의 테마 접근 시 404."""
    return get_object_or_404(Ktheme, pk=theme_pk, user=request.user)


@login_required
def main(request):
    user = request.user
    user_theme_list = Ktheme.objects.filter(user=user)

    if request.method == "POST":
        form = KthemeCreateForm(request.POST)
        if form.is_valid():
            # form.instance.user = user
            # ktheme = form.save()

            ktheme = form.save(commit=False)
            ktheme.user = user

            random_suffix = uuid.uuid4().hex[:6]
            ktheme.id = f"{user.username}_{random_suffix}"
            
            ktheme.save()
            

            return redirect("ktheme_detail", theme_pk=ktheme.id)
    else:
        form = KthemeCreateForm()

    return render(
        request,
        "main/main.html",
        {
            "user_theme_list": user_theme_list,
            "form": form,
            "user": user,
        },
    )


@login_required
def ktheme_detail(request, theme_pk):
    ktheme = _get_owned_theme(request, theme_pk)
    css_color = CssColor.objects.get(ktheme=ktheme)
    css_bubble = CssBubble.objects.get(ktheme=ktheme)

    version = str(int(datetime.now().timestamp()))

    ktheme_update_form = KthemeUpdateForm(instance=ktheme, initial={"name": ktheme.name})
    ktheme_image_form = KthemeImageForm()
    css_color_update_form = CssColorUpdateForm(instance=css_color)
    css_bubble_update_form = CssBubbleUpdateForm(instance=css_bubble)

    image_filenames = [filenames[0] for filenames in all_images_flat().values()]
    image_paths = [f"/media/{ktheme.id}/Images/{fn}" for fn in image_filenames]
    bubble_image_paths = [f"/media/{ktheme.id}/Images/{fn}" for fn in BUBBLE_PREVIEW_FILENAMES]

    return render(
        request,
        "main/ktheme_detail.html",
        {
            "version": version,
            "ktheme": ktheme,
            "icon_img_dic": ICON_IMG_DIC,
            "main_img_dic": MAIN_IMG_DIC,
            "chat_img_dic": CHAT_IMG_DIC,
            "passcode_img_dic": PASSCODE_IMG_DIC,
            "ktheme_image_form": ktheme_image_form,
            "ktheme_update_form": ktheme_update_form,
            "image_paths": image_paths,
            "bubble_image_paths": bubble_image_paths,
            "css_color_update_form": css_color_update_form,
            "css_bubble_update_form": css_bubble_update_form,
        },
    )


@login_required
@require_POST
def ktheme_update_name(request, theme_pk):
    ktheme = _get_owned_theme(request, theme_pk)
    form = KthemeUpdateForm(request.POST, instance=ktheme)

    if form.is_valid():
        ktheme = form.save()
        paths = theme_paths(ktheme.id)

        with open(paths["css"], "r", encoding="utf-8") as f:
            css_content = f.read()
        css_content = apply_theme_identity(css_content, ktheme.name, ktheme.id, request.user.username)
        with open(paths["css"], "w", encoding="utf-8") as f:
            f.write(css_content)

    return redirect("ktheme_detail", theme_pk=theme_pk)


@login_required
@require_POST
def ktheme_upload_image(request, theme_pk):
    ktheme = _get_owned_theme(request, theme_pk)
    paths = theme_paths(ktheme.id)
    image_dic = all_images_flat()

    for key, filenames in image_dic.items():
        image = request.FILES.get(key)
        if not image:
            continue

        try:
            validate_uploaded_image(image)
        except InvalidImageError:
            # 잘못된 파일은 조용히 건너뛴다 (다른 필드는 계속 처리).
            continue

        with Image.open(image) as img:
            width = int(img.width * 2 / 3)
            height = int(img.height * 2 / 3)
            re_img = img.resize((width, height), Image.LANCZOS)

            for filename in filenames:
                filepath = os.path.join(paths["images_dir"], filename)
                if "@2x" in filename:
                    re_img.save(filepath, format="PNG")
                else:
                    img.save(filepath, format="PNG")

    return redirect("ktheme_detail", theme_pk=theme_pk)


@login_required
@require_POST
def ktheme_update_color(request, theme_pk):
    ktheme = _get_owned_theme(request, theme_pk)
    css_color = CssColor.objects.get(ktheme=ktheme)
    css_bubble = CssBubble.objects.get(ktheme=ktheme)
    form = CssColorUpdateForm(request.POST, instance=css_color)

    if form.is_valid():
        css_color = form.save()
        paths = theme_paths(ktheme.id)

        with open(get_css_template_path(), "r", encoding="utf-8") as f:
            css_content = f.read()

        css_content = apply_color_theme(css_content, css_color)
        css_content = apply_bubble_css(css_content, css_bubble)
        css_content = apply_theme_identity(css_content, ktheme.name, ktheme.id, request.user.username)

        with open(paths["css"], "w", encoding="utf-8") as f:
            f.write(css_content)

    return redirect("ktheme_detail", theme_pk=theme_pk)


@login_required
@require_POST
def ktheme_update_bubble(request, theme_pk):
    ktheme = _get_owned_theme(request, theme_pk)
    css_bubble = CssBubble.objects.get(ktheme=ktheme)
    form = CssBubbleUpdateForm(request.POST, instance=css_bubble)

    if form.is_valid():
        css_bubble = form.save()
        paths = theme_paths(ktheme.id)

        with open(paths["css"], "r", encoding="utf-8") as f:
            css_content = f.read()
        css_content = apply_bubble_css(css_content, css_bubble)
        with open(paths["css"], "w", encoding="utf-8") as f:
            f.write(css_content)

    return redirect("ktheme_detail", theme_pk=theme_pk)


@login_required
@require_POST
def ktheme_create_zip(request, theme_pk):
    ktheme = _get_owned_theme(request, theme_pk)
    zip_path = build_theme_zip(ktheme.id, ktheme.name)
    filename = os.path.basename(zip_path)  # build_theme_zip()이 이미 안전한 이름으로 정리해둠

    with open(zip_path, "rb") as f:
        response = HttpResponse(f.read(), content_type="application/octet-stream")

        # 테마 이름이 한글이면(거의 항상 그렇다) filename="테마.ktheme" 처럼 그냥
        # 넣었을 때 브라우저가 Content-Disposition을 못 읽어서 확장자 없는
        # "download"로 뜨는 문제가 있었다. RFC 5987 filename*= 형식으로 함께
        # 보내면 최신 브라우저는 이걸 읽고, 옛날 브라우저는 ASCII 대체값을 쓴다.
        ascii_fallback = filename.encode("ascii", "ignore").decode("ascii") or "theme.ktheme"
        response["Content-Disposition"] = (
            f'attachment; filename="{ascii_fallback}"; filename*=UTF-8\'\'{quote(filename)}'
        )
        return response

@login_required
@require_POST
def ktheme_delete(request, theme_pk):
    """테마 DB 레코드 및 실제 미디어 폴더 삭제"""
    # 1. 내 테마가 맞는지 검증하며 가져오기 (남이 지우는 것 방지)
    ktheme = _get_owned_theme(request, theme_pk)
    
    # 2. 실제 서버에 생성된 폴더 경로 찾기 (예: media/ohsan_a1b2c3)
    # 기존에 사용하시던 theme_paths 유틸 함수를 활용합니다.
    paths = theme_paths(ktheme.id)
    theme_dir = os.path.dirname(paths["css"]) # css 파일이 있는 부모 폴더 경로
    
    # 3. 실제 폴더가 존재하면 통째로 삭제
    if os.path.exists(theme_dir):
        shutil.rmtree(theme_dir)
        
    # 4. 데이터베이스에서 테마 삭제 (Cascade 설정으로 연결된 색상, 말풍선도 같이 지워짐)
    ktheme.delete()
    
    # 5. 다 지웠으면 메인 화면으로 돌아가기
    return redirect("main")
