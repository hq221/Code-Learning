import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(folder_path, train_ratio=0.8):
    # 获取所有文件
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # 分割文件列表
    train_files, test_files = train_test_split(files, train_size=train_ratio, random_state=42)
    
    # 创建训练集和测试集文件夹
    train_folder = os.path.join(folder_path, 'train')
    test_folder = os.path.join(folder_path, 'test')
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    
    # 移动文件到相应文件夹
    for file in train_files:
        shutil.move(os.path.join(folder_path, file), os.path.join(train_folder, file))
    
    for file in test_files:
        shutil.move(os.path.join(folder_path, file), os.path.join(test_folder, file))

    print(f'Total files: {len(files)}')
    print(f'Training files: {len(train_files)}')
    print(f'Testing files: {len(test_files)}')

# 使用示例
folder_path = 'path_to_your_folder'
split_dataset(folder_path)
