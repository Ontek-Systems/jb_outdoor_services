import os
import re

# 1. Read existing style.css content
style_css_path = 'style.css'
with open(style_css_path, 'r', encoding='utf-8') as f:
    style_content_full = f.read()

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

css_to_append = ""
seen_css_snippets = set()

# Grab any existing custom classes from style_content_full
# to avoid duplicating them.
def is_in_style(snippet, style_text):
    # just do a rough check
    snippet_clean = re.sub(r'\s+', '', snippet)
    style_clean = re.sub(r'\s+', '', style_text)
    return snippet_clean in style_clean

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<style type="text/tailwindcss">(.*?)</style>', content, re.DOTALL)
    if match:
        style_content = match.group(1).strip()
        
        # Remove the @theme block because it's already in style.css
        style_content = re.sub(r'@theme\s*\{[^}]+\}', '', style_content).strip()
        
        # Remove body, h1..h6, img base rules because they are already in style.css
        style_content = re.sub(r'body\s*\{[^}]+\}', '', style_content).strip()
        style_content = re.sub(r'h1,\s*h2,\s*h3,\s*h4,\s*h5,\s*h6\s*\{[^}]+\}', '', style_content).strip()
        style_content = re.sub(r'img\s*\{[^}]+\}', '', style_content).strip()
        
        # What is left is unique custom classes for that page
        if style_content and len(style_content) > 10:
            if not is_in_style(style_content, style_content_full) and not is_in_style(style_content, css_to_append):
                css_to_append += f"\n\n/* --- Extracted from {os.path.basename(filepath)} --- */\n"
                css_to_append += style_content

# Append the new css to style.css
if css_to_append:
    with open(style_css_path, 'a', encoding='utf-8') as f:
        f.write(css_to_append)
    print("Appended new CSS to style.css")

# 2. Strip the inline <style type="text/tailwindcss"> block from all HTML files
count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We remove the entire <style type="text/tailwindcss"> ... </style> block
    new_content = re.sub(r'\s*<style type="text/tailwindcss">.*?</style>', '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Removed inline style from {filepath}")

print(f"Done! Cleaned {count} HTML files.")
