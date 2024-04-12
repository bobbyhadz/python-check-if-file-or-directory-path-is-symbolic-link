# Python: Check if a File path is symlink (symbolic link)

from pathlib import Path

path = Path(r'/home/borislav/Desktop/bobbyhadz_python/src')

print(path.is_symlink()) # 👉️ True

if path.is_symlink():
    print('The given path points to a symbolic link')
else:
    print('The path does NOT point to a symbolic link')