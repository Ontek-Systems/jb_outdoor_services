import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

# We want to remove the @theme { ... } block inside the HTML files
pattern = re.compile(r'\s*@theme\s*\{[^}]+\}', re.MULTILINE)

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    # Also clean up empty <style type="text/tailwindcss"></style> if left behind
    empty_style_pattern = re.compile(r'<style type="text/tailwindcss">\s*</style>', re.MULTILINE)
    new_content = empty_style_pattern.sub('', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'Cleaned @theme block from {filepath}')

print(f'Done! Cleaned {count} files.')
