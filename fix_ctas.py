import glob

files = glob.glob('*.html') + glob.glob('pages/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We will search for the second image div in the CTA section. 
    # Usually it's: class="w-full lg:w-3/12 reveal reveal-up order-3 flex justify-center lg:justify-end mt-0 lg:mt-16"
    # Or something similar. Let's look for `order-3 flex justify-center` or similar strings inside the BOTTOM CTA sections.
    # To be safe, we can just find:
    # class="w-full lg:w-3/12 reveal reveal-up order-3 flex justify-center
    # and change it to:
    # class="hidden lg:flex w-full lg:w-3/12 reveal reveal-up order-3 justify-center
    
    new_content = content.replace(
        'class="w-full lg:w-3/12 reveal reveal-up order-3 flex justify-center lg:justify-end',
        'class="hidden lg:flex w-full lg:w-3/12 reveal reveal-up order-3 justify-center lg:justify-end'
    )
    
    # Check if anything changed
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

