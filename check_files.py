import os
from pathlib import Path

required_structure = {
    'models': ['__init__.py', 'task.py', 'plan.py', 'tracking.py'],
    'views': ['__init__.py', 'task_view.py', 'plan_view.py', 'tracking_view.py'],
    'services': ['__init__.py', 'task_service.py', 'plan_service.py', 'tracking_service.py'],
    'utils': ['__init__.py', 'database.py'],
    '': ['main.py', 'requirements.txt', 'check_files.py']
}

def check_files():
    base_dir = Path('D:/secretary')
    missing_files = []
    existing_files = []

    for folder, files in required_structure.items():
        folder_path = base_dir / folder if folder else base_dir
        
        if not folder_path.exists():
            print(f"❌ Missing directory: {folder_path}")
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {folder_path}")
            continue

        for file in files:
            file_path = folder_path / file
            if not file_path.exists():
                missing_files.append(str(file_path))
            else:
                existing_files.append(str(file_path))

    print("\n=== File Check Results ===")
    print("\n✅ Existing files:")
    for file in sorted(existing_files):
        print(f"  - {file}")

    print("\n❌ Missing files:")
    for file in sorted(missing_files):
        print(f"  - {file}")

    return missing_files, existing_files

if __name__ == "__main__":
    missing_files, existing_files = check_files()
    if len(missing_files) > 0:
        print("\n需要创建以下文件。是否继续？(y/n)")
        response = input().lower()
        if response == 'y':
            print("正在创建缺失的文件...")
            # 这里可以添加创建文件的逻辑