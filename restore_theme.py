import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

theme_block = '''@theme {
    --color-brand-dark:   #141229;
    --color-brand-ocean:  #141229;
    --color-brand-bronze: #e8b01e;
    --color-brand-alice:  #F5F3EE;
    --color-brand-beige:  #F5F3EE;
    --color-brand-text:   #141229;
    --font-heading: 'Playfair Display', serif;
    --font-body:    'DM Sans', sans-serif;
}
'''

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if @theme is already there
    if '@theme' not in content:
        # Check if the <style type="text/tailwindcss"> tag exists
        if '<style type="text/tailwindcss">' in content:
            new_content = content.replace('<style type="text/tailwindcss">', f'<style type="text/tailwindcss">\n        {theme_block}')
        else:
            # Add it just before </head>
            style_tag = f'<style type="text/tailwindcss">\n        {theme_block}        </style>'
            new_content = content.replace('</head>', f'{style_tag}\n</head>')
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Restored @theme to {filepath}')
