import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

pattern = re.compile(r'\s*<style type="text/tailwindcss">\s*@theme\s*\{[\s\S]*?img\s*\{\s*filter:\s*saturate\(1\.1\);\s*\}\s*</style>', re.MULTILINE)

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'Removed inline style from {filepath}')

print(f'Done! Cleaned {count} files.')
