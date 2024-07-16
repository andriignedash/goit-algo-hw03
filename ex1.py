import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів і сортування їх у піддиректорії за розширеннями.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dst_dir", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def copy_and_sort_files(src_dir, dst_dir):
    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1][1:]  # Отримання розширення файлу без крапки
                if file_ext == '':
                    file_ext = 'no_extension'  # Для файлів без розширення
                
                new_dir = os.path.join(dst_dir, file_ext)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                
                shutil.copy(file_path, new_dir)
                
            for dir in dirs:
                copy_and_sort_files(os.path.join(root, dir), dst_dir)
    except Exception as e:
        print(f"Error: {e}")

def main():
    args = parse_args()
    src_dir = args.src_dir
    dst_dir = args.dst_dir
    
    if not os.path.isdir(src_dir):
        print(f"Error: {src_dir} is not a valid directory.")
        return
    
    copy_and_sort_files(src_dir, dst_dir)
    print(f"Files have been successfully copied and sorted into '{dst_dir}'")

if __name__ == "__main__":
    main()
