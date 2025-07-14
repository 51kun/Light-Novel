import os

def rename_txt_to_md():
    # 获取当前文件夹路径
    current_dir = os.getcwd()
    
    # 遍历当前文件夹中的所有文件
    for filename in os.listdir(current_dir):
        # 检查文件是否以.txt结尾
        if filename.endswith('.txt'):
            # 构造新的文件名（将.txt替换为.md）
            new_filename = filename[:-4] + '.md'
            
            # 获取文件的完整路径
            old_path = os.path.join(current_dir, filename)
            new_path = os.path.join(current_dir, new_filename)
            
            # 重命名文件
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_filename}')
            except Exception as e:
                print(f'Error renaming {filename}: {e}')

if __name__ == '__main__':
    rename_txt_to_md()