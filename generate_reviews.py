import re

reviews = [
    {
        "text": "I was really impressed with JB Outdoor Services. They were quick, efficient, polite and friendly. Their prices are competitive and I am happy to recommend.",
        "name": "Joyzie Anderson",
        "loc": "Wincanton",
        "icon": "G"
    },
    {
        "text": "Highly recommend. Excellent service.",
        "name": "Sian White",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "Reliable and cheap service carried out. Turned up when he said he would and what was done exceeded expectations. 100% recommend.",
        "name": "Sam Smith",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "Great communication, reliable, quick, polite and very clean. Picked up my mixed rubble with no hassle and left the driveway spotless. Very reasonably priced as well, cheaper than skip hire and less hassle. 100% would recommend and I'll definitely ask JB for help again. Thank you Jack!",
        "name": "Waldemar Bach",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "Jack is a very prompt and professional guy. He clears up after himself and is really polite.",
        "name": "CJ Dixon-Payne",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "Jack has completed the hard landscaping and waste removal for our property. Jack and his team worked to plan clearing the site and proved to be professional and polite. We are delighted with the result and have no hesitation in recommending their services.",
        "name": "Julie Beard",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "Very reliable. Arrive at the time they say they are going to arrive. Very polite and reasonably priced. Highly recommended.",
        "name": "Gemma Keddie",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "Cleared our garage. Great communication, excellent service. Thank you so much!",
        "name": "Jen Lemen",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "We've used Jack a lot over the past year, building patios, re-landscaping areas and even knocking down a garage. Jack took the time to go through our ideas and made great suggestions. He's a reliable worker, always on time and tidy. I would highly recommend him.",
        "name": "Frankie Lemen",
        "loc": "Wincanton",
        "icon": "F"
    },
    {
        "text": "Recommend Jack and his team. Friendly, efficient, competitively priced. Made a tidy job of cutting hedges, clearing up and taking away cuttings.",
        "name": "Janet Perry",
        "loc": "Wincanton",
        "icon": "F"
    }
]

google_svg = '''<svg class="w-4 h-4 text-white/40 group-hover:text-white/90 transition-colors duration-500" viewBox="0 0 24 24" fill="currentColor">
                                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
                                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
                                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
                                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
                                        </svg>'''

fb_svg = '''<svg class="w-4 h-4 text-white/40 group-hover:text-white/90 transition-colors duration-500" viewBox="0 0 24 24" fill="currentColor">
                                            <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/>
                                        </svg>'''

html = ""
for rev in reviews + reviews:
    svg = google_svg if rev["icon"] == "G" else fb_svg
    html += f'''                            <div class="w-[85vw] sm:w-[350px] lg:w-[380px] flex-shrink-0">
                                <div class="group p-6 sm:p-6 lg:p-8 rounded-3xl h-full flex flex-col justify-between transition-all duration-500 hover:-translate-y-2 shadow-lg hover:shadow-xl"
                                    style="background:#141229;" onmouseenter="this.style.background='#e8b01e'"
                                    onmouseleave="this.style.background='#141229'">
                                    <div>
                                        <div class="flex text-yellow-400 group-hover:text-white transition-colors duration-500 mb-5 text-xl tracking-widest"
                                            aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                                        <p
                                            class="font-body text-white/80 group-hover:text-white italic mb-8 text-sm sm:text-sm lg:text-base leading-relaxed transition-colors duration-500">
                                            "{rev['text']}"
                                        </p>
                                    </div>
                                    <div
                                        class="flex items-center justify-between border-t border-white/10 group-hover:border-white/30 transition-colors duration-500 pt-4 mt-auto">
                                        <p
                                            class="font-body font-bold text-white text-sm lg:text-base transition-colors duration-500">
                                            {rev['name']}, {rev['loc']}</p>
                                        {svg}
                                    </div>
                                </div>
                            </div>\n'''

with open("index.html", "r") as f:
    content = f.read()

start_marker = '<div class="flex gap-4 sm:gap-6 md:gap-8 pr-4 sm:pr-6 md:pr-8 w-max">'
start_idx = content.find(start_marker)

end_marker = '                        </div>\n                    </div>\n                </div>\n            </div>\n\n            </div>\n            </div>\n            </div>'
end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    # Just find the </div> that closes the flex wrapper
    # Let's search for "                            <div class="w-[85vw] sm:w-[350px] lg:w-[380px] flex-shrink-0">" and replace until the end of that list
    pass

import re
# Use regex to replace the content between <div class="flex gap-4 sm:gap-6 md:gap-8 pr-4 sm:pr-6 md:pr-8 w-max">\n  and the closing </div> of that container.
# The container closes before `                    </div>\n                </div>\n            </div>` (lines 1704+)
pattern = r'(<div class="flex gap-4 sm:gap-6 md:gap-8 pr-4 sm:pr-6 md:pr-8 w-max">).*?(?=                        </div>\n                    </div>\n                </div>\n            </div>)'
new_content = re.sub(pattern, r'\1\n\n' + html, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(new_content)

print("Replacement done")
