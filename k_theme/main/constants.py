# 이미지 카테고리별 매핑
# key: 화면에 표시되는 한글 라벨 (템플릿의 input name으로도 그대로 사용됨)
# value: 이 라벨 하나로 채워야 할 실제 CSS 리소스 파일명들 (2x/3x, selected 변형 포함)

ICON_IMG_DIC = {
    "테마 아이콘": ["commonIcoTheme.png"],
}

MAIN_IMG_DIC = {
    "친구 아이콘": [
        "maintabIcoFriends@3x.png",
        "maintabIcoFriends@2x.png",
    ],
    "친구 아이콘 선택": [
        "maintabIcoFriendsSelected@3x.png",
        "maintabIcoFriendsSelected@2x.png",
    ],
    "채팅 아이콘": [
        "maintabIcoChats@3x.png",
        "maintabIcoChats@2x.png",
    ],
    "채팅 아이콘 선택": [
        "maintabIcoChatsSelected@3x.png",
        "maintabIcoChatsSelected@2x.png",
    ],
    "오픈채팅 아이콘": [
        "maintabIcoOpenChats@3x.png",
        "maintabIcoOpenChats@2x.png",
        "maintabIcoPiccoma@2x.png",
        "maintabIcoPiccoma@3x.png",
    ],
    "오픈채팅 아이콘 선택": [
        "maintabIcoOpenChatsSelected@3x.png",
        "maintabIcoOpenChatsSelected@2x.png",
        "maintabIcoPiccomaSelected@2x.png",
        "maintabIcoPiccomaSelected@3x.png",
    ],
    "쇼핑 아이콘": [
        "maintabIcoShopping@3x.png",
        "maintabIcoShopping@2x.png",
        "maintabIcoCall@2x.png",
        "maintabIcoCall@3x.png",
    ],
    "쇼핑 아이콘 선택": [
        "maintabIcoShoppingSelected@3x.png",
        "maintabIcoShoppingSelected@2x.png",
        "maintabIcoCallSelected@2x.png",
        "maintabIcoCallSelected@3x.png",
    ],
    "더보기 아이콘": [
        "maintabIcoMore@3x.png",
        "maintabIcoMore@2x.png",
    ],
    "더보기 아이콘 선택": [
        "maintabIcoMoreSelected@3x.png",
        "maintabIcoMoreSelected@2x.png",
    ],
    "탭 배경": [
        "maintabBgImage@3x.png",
        "maintabBgImage@2x.png",
    ],
    "메인 배경": ["mainBgImage@3x.png"],
    "프로필 이미지": ["profileImg01@3x.png"],
}

CHAT_IMG_DIC = {
    "받은 말풍선 1": [
        "chatroomBubbleReceive01@3x.png",
        "chatroomBubbleReceive01@2x.png",
        "chatroomBubbleReceive01Selected@2x.png",
        "chatroomBubbleReceive01Selected@3x.png",
    ],
    "받은 말풍선 2": [
        "chatroomBubbleReceive02@3x.png",
        "chatroomBubbleReceive02@2x.png",
        "chatroomBubbleReceive02Selected@2x.png",
        "chatroomBubbleReceive02Selected@3x.png",
    ],
    "보낸 말풍선 1": [
        "chatroomBubbleSend01@3x.png",
        "chatroomBubbleSend01@2x.png",
        "chatroomBubbleSend01Selected@2x.png",
        "chatroomBubbleSend01Selected@3x.png",
    ],
    "보낸 말풍선 2": [
        "chatroomBubbleSend02@3x.png",
        "chatroomBubbleSend02@2x.png",
        "chatroomBubbleSend02Selected@2x.png",
        "chatroomBubbleSend02Selected@3x.png",
    ],
    "채팅 배경": ["chatroomBgImage@3x.png"],
}

PASSCODE_IMG_DIC = {
    "암호 1": ["passcodeImgCode01@3x.png"],
    "암호 2": ["passcodeImgCode02@3x.png"],
    "암호 3": ["passcodeImgCode03@3x.png"],
    "암호 4": ["passcodeImgCode04@3x.png"],
    "암호 1 선택": ["passcodeImgCode01Selected@3x.png"],
    "암호 2 선택": ["passcodeImgCode02Selected@3x.png"],
    "암호 3 선택": ["passcodeImgCode03Selected@3x.png"],
    "암호 4 선택": ["passcodeImgCode04Selected@3x.png"],
    "암호 배경": ["passcodeBgImage@3x.png"],
    "암호 눌림": ["passcodeKeypadPressed@3x.png"],
}

# 원본 static/KakaoTalkTheme.css 템플릿에 실제로 박혀 있는 "플레이스홀더" 색상값.
# apply_color_theme()이 이 값을 찾아서 사용자가 지정한 색상으로 치환하므로,
# 여기 값은 템플릿 파일 및 main/models.py의 CssColor 필드 default와 반드시 일치해야 한다.
# (틀어지면 그 색상은 아무리 바꿔도 결과물에 절대 반영되지 않는다 — 실제 발생했던 버그)
ORIGINAL_CSS_COLORS = {
    "bg_color": "#FFFFFF",
    "main_text_color": "#000000",
    "point_text_color": "#414141",
    "input_bg_color": "#D3D3D3",
    "send_text_color": "#000002",
    "receive_text_color": "#000001",
}

BUBBLE_PREVIEW_FILENAMES = [
    "chatroomBubbleReceive01@3x.png",
    "chatroomBubbleReceive02@3x.png",
    "chatroomBubbleSend01@3x.png",
    "chatroomBubbleSend02@3x.png",
]


def all_images_flat():
    """카테고리 구분 없이 {한글key: [filenames]} 전체 병합."""
    merged = {}
    merged.update(ICON_IMG_DIC)
    merged.update(MAIN_IMG_DIC)
    merged.update(CHAT_IMG_DIC)
    merged.update(PASSCODE_IMG_DIC)
    return merged