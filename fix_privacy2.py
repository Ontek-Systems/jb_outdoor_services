import re

with open('pages/privacy-policy.html', 'r') as f:
    content = f.read()

# Add text-left to the main container
content = content.replace(
    '<div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 font-body reveal reveal-up"',
    '<div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 font-body reveal reveal-up text-left"'
)

# Add justify-start to the flex items
content = content.replace(
    'flex items-center gap-2 md:gap-3',
    'flex items-center justify-start gap-2 md:gap-3'
)
content = content.replace(
    'flex items-start gap-2',
    'flex items-start justify-start gap-2 text-left'
)

# Ensure sections are text-left
content = content.replace(
    'bg-white rounded-2xl p-5 md:p-8 shadow-sm border border-brand-dark/5',
    'bg-white rounded-2xl p-5 md:p-8 shadow-sm border border-brand-dark/5 text-left'
)

with open('pages/privacy-policy.html', 'w') as f:
    f.write(content)

print("Fixed privacy policy responsiveness again.")
