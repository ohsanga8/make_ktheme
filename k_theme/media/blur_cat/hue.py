import cv2
import numpy as np
import os

def shift_hue_with_alpha(image, hue_shift):
    # 분리
    if image.shape[2] == 4:
        bgr = image[:, :, :3]
        alpha = image[:, :, 3]
    else:
        bgr = image
        alpha = None

    # 색조 변경
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0] = (hsv[:, :, 0].astype(int) + hue_shift) % 180
    shifted_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # 알파 붙이기
    if alpha is not None:
        result = cv2.merge((shifted_bgr, alpha))
    else:
        result = shifted_bgr

    return result

def process_folder(folder_path, hue_shift):
    folder_name = os.path.basename(os.path.normpath(folder_path))
    output_folder = f"{folder_path}_{hue_shift}"
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".png"):
            path = os.path.join(folder_path, filename)
            image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            if image is None:
                print(f"Failed to load: {filename}")
                continue

            shifted = shift_hue_with_alpha(image, hue_shift)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, shifted)
            print(f"Saved: {output_path}")


if __name__ == "__main__":
    folder = "C:/Users/ohsan/Desktop/ktheme_django/make_ktheme/k_theme/media/blur_cat/cat_2025_skyblue/Images_100/Images_0"  
    hue_shift_amount = 90

    process_folder(folder, hue_shift_amount)
