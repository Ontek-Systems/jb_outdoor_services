import os
import re

def fix_all_links_to_real_files(root_dir):
    # Map of all HTML files to their root-relative paths
    file_map = {}
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs: dirs.remove('.git')
        for file in files:
            if file.lower().endswith('.html'):
                abs_path = os.path.join(root, file)
                rel_to_root = os.path.relpath(abs_path, root_dir).replace('\\', '/')
                file_map[file] = rel_to_root

    # Regex to find href="..." or src="..."
    pattern = re.compile(r'(href|src)="([^"]+\.html|[^"]+\.css|[^"]+\.js|[^"]+\.png|[^"]+\.jpg|[^"]+\.jpeg|[^"]+\.webp|[^"]+\.svg)(#[^"]*)?"')

    for root, dirs, files in os.walk(root_dir):
        if 'components' in dirs: dirs.remove('components')
        if '.git' in dirs: dirs.remove('.git')
        
        for file in files:
            if file.lower().endswith('.html'):
                path = os.path.join(root, file)
                current_dir_rel = os.path.relpath(root, root_dir).replace('\\', '/')
                if current_dir_rel == '.': current_dir_rel = ''
                
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                def replace_func(match):
                    attr = match.group(1)
                    link = match.group(2)
                    anchor = match.group(3) or ''
                    
                    if link.startswith('http') or link.startswith('tel:') or link.startswith('mailto:'):
                        return match.group(0)
                    
                    # Extract filename
                    basename = os.path.basename(link)
                    
                    if basename in file_map:
                        target_rel_to_root = file_map[basename]
                        # Calculate best relative path from current file's directory
                        best_rel = os.path.relpath(target_rel_to_root, current_dir_rel).replace('\\', '/')
                        return f'{attr}="{best_rel}{anchor}"'
                    
                    return match.group(0)

                new_content = pattern.sub(replace_func, content)
                
                if new_content != content:
                    print(f"Fixed links in {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    root = r"d:\xampp\htdocs\onteksystems\Website Builds\jb_outdoor_services"
    fix_all_links_to_real_files(root)
