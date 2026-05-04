import os
import re

def fix_paths(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs: dirs.remove('.git')
        for file in files:
            if file.lower().endswith('.html'):
                path = os.path.join(root, file)
                rel_root = os.path.relpath(root_dir, root).replace('\\', '/')
                if rel_root == '.':
                    rel_root = ''
                else:
                    rel_root += '/'
                
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix absolute paths to style.css and global.js
                # Replace href="/style.css" with href="{rel_root}style.css"
                # Replace src="/global.js" with src="{rel_root}global.js"
                
                new_content = re.sub(r'href="/style\.css"', f'href="{rel_root}style.css"', content)
                new_content = re.sub(r'src="/global\.js"', f'src="{rel_root}global.js"', new_content)
                
                # Also fix favicon and other root assets if they are absolute
                new_content = re.sub(r'href="/(favicon|apple-touch-icon|android-chrome|site\.webmanifest)', f'href="{rel_root}\\1', new_content)
                
                if new_content != content:
                    print(f"Fixed paths in {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    root = r"d:\xampp\htdocs\onteksystems\Website Builds\jb_outdoor_services"
    fix_paths(root)
