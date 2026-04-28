import os
import glob

services_dir = r"d:\xampp\htdocs\onteksystems\Website Builds\jb_outdoor_services\services"
files = glob.glob(os.path.join(services_dir, "*.html"))

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Increase padding
    content = content.replace('pt-32', 'pt-48')
    
    # Add light-nav-page class to body if not already there
    if 'light-nav-page' not in content:
        content = content.replace('<body class="flex', '<body class="light-nav-page flex')
        content = content.replace('<body class="bg', '<body class="light-nav-page bg')
        
        # If the body tag is different:
        if '<body class="' in content and 'light-nav-page' not in content:
            content = content.replace('<body class="', '<body class="light-nav-page ')
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated {len(files)} files in services/")
