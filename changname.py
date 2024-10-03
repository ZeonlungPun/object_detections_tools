import os
import time
from datetime import datetime

# 設定圖片與標籤的文件夾路徑
image_folder = '/home/kingargroo/YOLOVISION/newspore/wheat/img'
label_folder = '/home/kingargroo/YOLOVISION/newspore/wheat/label'

# 遍歷圖片文件夾
for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # 提取圖片的名稱與擴展名
        file_base, file_ext = os.path.splitext(filename)
        
        # 獲取當前時間並格式化
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')

        # 設定新圖片名稱
        new_image_name = f'{current_time}{file_ext}'
        
        # 設定對應的標籤文件名稱
        new_label_name = f'{current_time}.txt'
        
        # 原圖片與標籤文件的完整路徑
        old_image_path = os.path.join(image_folder, filename)
        old_label_path = os.path.join(label_folder, f'{file_base}.txt')
        
        # 新圖片與標籤文件的完整路徑
        new_image_path = os.path.join(image_folder, new_image_name)
        new_label_path = os.path.join(label_folder, new_label_name)
        
        # 重命名圖片與標籤文件
        os.rename(old_image_path, new_image_path)
        os.rename(old_label_path, new_label_path)
        
        print(f'Renamed {filename} to {new_image_name}')
        print(f'Renamed {file_base}.txt to {new_label_name}')
        
        # 為避免名稱衝突，稍微等待一秒
        time.sleep(1)
