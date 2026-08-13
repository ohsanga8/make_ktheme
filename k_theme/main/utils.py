import os
import re
import zipfile

from django.conf import settings
from django.contrib.staticfiles.finders import find

from .constants import ORIGINAL_CSS_COLORS


# ---------------------------------------------------------------------------
# 경로 관련
# ---------------------------------------------------------------------------

def get_css_template_path():
    """원본 CSS 템플릿 경로. staticfiles finder를 통해 찾아서
    STATIC_ROOT가 로컬 파일시스템이 아닌 배포 환경(S3 등)이 되어도
    최대한 안전하게 동작하도록 함."""
    path = find("KakaoTalkTheme.css")
    if path:
        return path

    fallback = os.path.join(settings.STATIC_ROOT, "KakaoTalkTheme.css")
    if os.path.exists(fallback):
        return fallback

    raise FileNotFoundError("KakaoTalkTheme.css 템플릿을 찾을 수 없습니다.")


def get_default_images_dir():
    path = find("Images")
    if path:
        return path

    fallback = os.path.join(settings.STATIC_ROOT, "Images")
    if os.path.exists(fallback):
        return fallback

    raise FileNotFoundError("기본 이미지 디렉토리를 찾을 수 없습니다.")


def safe_theme_dir(theme_id):
    """theme_id로 만든 경로가 MEDIA_ROOT 밖으로 빠져나가지 않는지 검증.
    Ktheme.id는 사용자가 입력하는 값이라 path traversal 방지가 필요함."""
    media_root = os.path.abspath(settings.MEDIA_ROOT)
    theme_dir = os.path.abspath(os.path.join(media_root, theme_id))

    if not (theme_dir == media_root or theme_dir.startswith(media_root + os.sep)):
        raise ValueError(f"잘못된 테마 경로입니다: {theme_id!r}")

    return theme_dir


def theme_paths(theme_id):
    theme_dir = safe_theme_dir(theme_id)
    return {
        "dir": theme_dir,
        "css": os.path.join(theme_dir, "KakaoTalkTheme.css"),
        "images_dir": os.path.join(theme_dir, "Images"),
    }


def ensure_theme_dirs(theme_id):
    paths = theme_paths(theme_id)
    os.makedirs(paths["images_dir"], exist_ok=True)
    return paths


# ---------------------------------------------------------------------------
# CSS 내용 치환
# ---------------------------------------------------------------------------

def apply_theme_identity(css_content, theme_name, theme_id, author_name):
    """테마 이름/id/작성자명 치환.
    문자열 placeholder("themeName" 등)를 찾는 방식 대신, CSS 속성 값을
    정규식으로 항상 덮어써서 몇 번을 재실행해도 안전하게 동작하도록 함."""
    css_content = re.sub(
        r"-kakaotalk-theme-name: '[^']*';",
        f"-kakaotalk-theme-name: '{theme_name}';",
        css_content,
    )
    css_content = re.sub(
        r"-kakaotalk-theme-id: 'com\.kakao\.talk\.theme\.[^']*';",
        f"-kakaotalk-theme-id: 'com.kakao.talk.theme.{theme_id}';",
        css_content,
    )
    css_content = re.sub(
        r"-kakaotalk-author-name: '[^']*';",
        f"-kakaotalk-author-name: '{author_name}';",
        css_content,
    )
    return css_content


def apply_color_theme(css_content, css_color):
    """ORIGINAL_CSS_COLORS에 정의된 '원본 플레이스홀더 색상'을 찾아
    사용자가 지정한 색상으로 치환한다.

    예전에는 이 자리에 #FFC0CB / #A9A9A9 / #808080 같은 값이 하드코딩돼
    있었는데, 실제 static/KakaoTalkTheme.css 템플릿의 강조 텍스트/보낸-받은
    말풍선 텍스트 색상이 이미 #414141 / #000002 / #000001로 바뀌어 있어서
    저 세 replace()가 전부 매치되지 않는(=조용히 아무 일도 안 하는) 상태였다.
    그 결과 배경/메인 텍스트/입력창 색은 바뀌는데 나머지 텍스트 색만
    아무리 바꿔도 반영되지 않는 버그가 있었다. 이제는 constants.py의
    ORIGINAL_CSS_COLORS 한 곳만 보고 판단하므로 템플릿 색상이 또 바뀌면
    거기만 고치면 된다."""
    for field_name, placeholder in ORIGINAL_CSS_COLORS.items():
        css_content = css_content.replace(placeholder, getattr(css_color, field_name))
    return css_content


def _bubble_replacements(css_bubble):
    b = css_bubble
    return {
        "Send": [
            (r"-ios-background-image: 'chatroomBubbleSend01\.png' \d+px \d+px;",
             f"-ios-background-image: 'chatroomBubbleSend01.png' {b.s_1_x}px {b.s_1_y}px;"),
            (r"-ios-selected-background-image: 'chatroomBubbleSend01Selected\.png' \d+px \d+px;",
             f"-ios-selected-background-image: 'chatroomBubbleSend01Selected.png' {b.s_1_x}px {b.s_1_y}px;"),
            (r"-ios-group-background-image: 'chatroomBubbleSend02\.png' \d+px \d+px;",
             f"-ios-group-background-image: 'chatroomBubbleSend02.png' {b.s_2_x}px {b.s_2_y}px;"),
            (r"-ios-group-selected-background-image: 'chatroomBubbleSend02Selected\.png' \d+px \d+px;",
             f"-ios-group-selected-background-image: 'chatroomBubbleSend02Selected.png' {b.s_2_x}px {b.s_2_y}px;"),
            (r"-ios-title-edgeinsets: \d+px \d+px \d+px \d+px;",
             f"-ios-title-edgeinsets: {b.s_1_t}px {b.s_1_l}px {b.s_1_b}px {b.s_1_r}px;"),
            (r"-ios-group-title-edgeinsets: \d+px \d+px \d+px \d+px;",
             f"-ios-group-title-edgeinsets: {b.s_2_t}px {b.s_2_l}px {b.s_2_b}px {b.s_2_r}px;"),
        ],
        "Receive": [
            (r"-ios-background-image: 'chatroomBubbleReceive01\.png' \d+px \d+px;",
             f"-ios-background-image: 'chatroomBubbleReceive01.png' {b.r_1_x}px {b.r_1_y}px;"),
            (r"-ios-selected-background-image: 'chatroomBubbleReceive01Selected\.png' \d+px \d+px;",
             f"-ios-selected-background-image: 'chatroomBubbleReceive01Selected.png' {b.r_1_x}px {b.r_1_y}px;"),
            (r"-ios-group-background-image: 'chatroomBubbleReceive02\.png' \d+px \d+px;",
             f"-ios-group-background-image: 'chatroomBubbleReceive02.png' {b.r_2_x}px {b.r_2_y}px;"),
            (r"-ios-group-selected-background-image: 'chatroomBubbleReceive02Selected\.png' \d+px \d+px;",
             f"-ios-group-selected-background-image: 'chatroomBubbleReceive02Selected.png' {b.r_2_x}px {b.r_2_y}px;"),
            (r"-ios-title-edgeinsets: \d+px \d+px \d+px \d+px;",
             f"-ios-title-edgeinsets: {b.r_1_t}px {b.r_1_l}px {b.r_1_b}px {b.r_1_r}px;"),
            (r"-ios-group-title-edgeinsets: \d+px \d+px \d+px \d+px;",
             f"-ios-group-title-edgeinsets: {b.r_2_t}px {b.r_2_l}px {b.r_2_b}px {b.r_2_r}px;"),
        ],
    }


def apply_bubble_css(css_content, css_bubble):
    """Send/Receive 블록을 CSS 안에서 각각 잘라내어 그 안에서만 치환.
    (send/receive의 edgeinsets 정규식이 동일해서 서로 덮어쓰던 버그 방지)"""
    replacements = _bubble_replacements(css_bubble)

    for block_name, pattern_list in replacements.items():
        block_pattern = rf"(MessageCellStyle-{block_name} \{{)(.*?)(\}})"
        match = re.search(block_pattern, css_content, re.DOTALL)
        if not match:
            continue
        block_text = match.group(2)
        for pat, repl in pattern_list:
            block_text = re.sub(pat, repl, block_text)
        new_block = match.group(1) + block_text + match.group(3)
        css_content = css_content[:match.start()] + new_block + css_content[match.end():]

    return css_content


# ---------------------------------------------------------------------------
# 이미지 업로드 검증
# ---------------------------------------------------------------------------

ALLOWED_IMAGE_CONTENT_TYPES = {"image/png", "image/jpeg"}
MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024  # 5MB


class InvalidImageError(ValueError):
    pass


def validate_uploaded_image(uploaded_file):
    if uploaded_file.content_type not in ALLOWED_IMAGE_CONTENT_TYPES:
        raise InvalidImageError(
            f"지원하지 않는 파일 형식입니다: {uploaded_file.content_type}"
        )
    if uploaded_file.size > MAX_IMAGE_SIZE_BYTES:
        raise InvalidImageError("파일 크기가 너무 큽니다 (최대 5MB).")


# ---------------------------------------------------------------------------
# ZIP 생성
# ---------------------------------------------------------------------------

_UNSAFE_FILENAME_CHARS = re.compile(r'[\\/:*?"<>|]')


def safe_ktheme_filename(theme_name):
    """테마 이름을 파일명으로 써도 안전하게 정리한 '<이름>.ktheme'.
    Windows/서버 파일시스템에서 금지된 문자(\\ / : * ? " < > |)를 제거해서
    build_theme_zip()이 엉뚱한 하위 경로에 쓰거나 실패하는 것을 막는다."""
    cleaned = _UNSAFE_FILENAME_CHARS.sub("_", theme_name).strip()
    return f"{cleaned or 'theme'}.ktheme"


def build_theme_zip(theme_id, theme_name):
    paths = theme_paths(theme_id)
    zip_path = os.path.join(paths["dir"], safe_ktheme_filename(theme_name))

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(paths["css"], os.path.basename(paths["css"]))
        for root, _, files in os.walk(paths["images_dir"]):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, paths["images_dir"])
                zipf.write(file_path, os.path.join("Images", arcname))

    return zip_path