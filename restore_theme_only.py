import os

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

theme_block = """    <style type="text/tailwindcss">
        @theme {
            --color-brand-dark:   #141229;
            --color-brand-ocean:  #141229;
            --color-brand-bronze: #e8b01e;
            --color-brand-alice:  #F5F3EE;
            --color-brand-beige:  #F5F3EE;
            --color-brand-text:   #141229;
            --font-heading: 'Playfair Display', serif;
            --font-body:    'DM Sans', sans-serif;
        }
    </style>
"""

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<style type="text/tailwindcss">' not in content:
        # Insert right before </head>
        new_content = content.replace('</head>', f'{theme_block}</head>')
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Restored @theme to {filepath}")

print(f"Done! Restored inline theme to {count} files.")
