import os
from PIL import Image

# 특정 폴더 경로 설정
folder_path = 'C:/Users/USER/Downloads/bubble2'

# 폴더 내의 모든 파일 확인
for filename in os.listdir(folder_path):
    # PNG 파일만 선택
    if filename.endswith('.png'):
        # 이미지 열기
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        
        # 이미지 좌우 반전
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        
        # 새로운 파일 이름 설정
        new_filename = f"{os.path.splitext(filename)[0]}_f.png"
        new_img_path = os.path.join(folder_path, new_filename)
        
        # 반전된 이미지 저장
        flipped_img.save(new_img_path)

print("모든 PNG 파일이 성공적으로 좌우 반전되었습니다.")
