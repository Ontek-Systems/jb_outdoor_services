import re

with open('pages/privacy-policy.html', 'r') as f:
    content = f.read()

# 1. Last updated
content = content.replace('Last updated: April 2025', 'Last updated May 2026')

# 2. Title color
content = content.replace('style="color:rgba(242,247,255,0.92);"', 'class="text-white"')

# 3. Numbers without circles
# Pattern: <span class="w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold shrink-0"\s*style="background:rgba\(232,176,30,0\.15\);\s*color:#e8b01e;">(\d+)</span>
pattern = r'<span class="w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold shrink-0"\s*style="background:rgba\(232,176,30,0\.15\);\s*color:#e8b01e;">(\d+)</span>'
replacement = r'<span class="text-[#e8b01e] font-bold text-2xl mr-1">\1.</span>'
content = re.sub(pattern, replacement, content)

with open('pages/privacy-policy.html', 'w') as f:
    f.write(content)

print("Fixed privacy policy.")
