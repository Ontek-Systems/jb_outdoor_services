import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

seen_styles = set()
unique_css = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<style type="text/tailwindcss">(.*?)</style>', content, re.DOTALL)
    if match:
        style_content = match.group(1).strip()
        style_content = re.sub(r'@theme\s*\{[^}]+\}', '', style_content).strip()
        style_content = re.sub(r'body\s*\{[^}]+\}', '', style_content).strip()
        style_content = re.sub(r'h1,h2,h3,h4,h5,h6\s*\{[^}]+\}', '', style_content).strip()
        style_content = re.sub(r'img\s*\{[^}]+\}', '', style_content).strip()
        
        if style_content and style_content not in seen_styles:
            seen_styles.add(style_content)
            unique_css.append((filepath, style_content))

for path, css in unique_css:
    print(f'\n--- FROM {path} ---\n{css[:500]}...')
