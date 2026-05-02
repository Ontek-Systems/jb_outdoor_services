import re

with open('index.html', 'r') as f:
    content = f.read()

# Make the card relative so we can absolutely position the SVG
content = content.replace('class="group p-6 sm:p-6 lg:p-8 rounded-3xl h-full flex flex-col', 'class="group relative p-6 sm:p-6 lg:p-8 rounded-3xl h-full flex flex-col')

# Center stars on phone
content = content.replace('class="flex text-yellow-400 group-hover:text-white transition-colors duration-500 mb-5 text-xl tracking-widest"', 'class="flex justify-center sm:justify-start text-yellow-400 group-hover:text-white transition-colors duration-500 mb-5 text-xl tracking-widest"')

# Center review text on phone
content = content.replace('class="font-body text-white/80 group-hover:text-white italic mb-8 text-sm sm:text-sm lg:text-base leading-relaxed transition-colors duration-500"', 'class="font-body text-center sm:text-left text-white/80 group-hover:text-white italic mb-8 text-sm sm:text-sm lg:text-base leading-relaxed transition-colors duration-500"')

# Change bottom container and make SVG absolute
def replace_bottom(match):
    name = match.group(1)
    svg_path = match.group(2)
    return f'''<div class="border-t border-white/10 group-hover:border-white/30 transition-colors duration-500 pt-4 mt-auto text-center sm:text-left pr-8 sm:pr-0">
                                        <p class="font-body font-bold text-white text-sm lg:text-base transition-colors duration-500">
                                            {name}</p>
                                    </div>
                                    <svg class="absolute bottom-6 lg:bottom-8 right-6 lg:right-8 w-5 h-5 text-white/40 group-hover:text-white/90 transition-colors duration-500" viewBox="0 0 24 24" fill="currentColor">
{svg_path}                                    </svg>'''

pattern = r'<div\s+class="flex items-center justify-between border-t border-white/10 group-hover:border-white/30 transition-colors duration-500 pt-4 mt-auto">\s*<p\s+class="font-body font-bold text-white text-sm lg:text-base transition-colors duration-500">\s*(.*?)</p>\s*<svg class="w-4 h-4 text-white/40 group-hover:text-white/90 transition-colors duration-500" viewBox="0 0 24 24" fill="currentColor">\n(.*?)\s*</svg>\s*</div>'

content = re.sub(pattern, replace_bottom, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print("Done fixing reviews.")
