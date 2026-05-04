import os
import shutil

slider_dir = r"d:\xampp\htdocs\onteksystems\Website Builds\jb_outdoor_services\assets\imgs\hero_slider"
if not os.path.exists(slider_dir):
    os.makedirs(slider_dir)

src1 = r"d:\xampp\htdocs\onteksystems\Website Builds\jb_outdoor_services\assets\imgs\c1.png"
src2 = r"d:\xampp\htdocs\onteksystems\Website Builds\jb_outdoor_services\assets\imgs\s3.jpg"
src3 = r"d:\xampp\htdocs\onteksystems\Website Builds\jb_outdoor_services\assets\imgs\s4.jpg"

if os.path.exists(src1): shutil.copy(src1, os.path.join(slider_dir, "slide1.png"))
if os.path.exists(src2): shutil.copy(src2, os.path.join(slider_dir, "slide2.jpg"))
if os.path.exists(src3): shutil.copy(src3, os.path.join(slider_dir, "slide3.jpg"))

print("Created hero_slider directory and copied images.")
