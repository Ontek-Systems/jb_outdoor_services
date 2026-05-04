import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<!-- ═══════════════════════════════════════════════════════\s*CLASSIC HERO \(DIAGONAL\)\s*═══════════════════════════════════════════════════════ -->.*?<!-- ═══════════════════════════════════════════════════════\s*SCROLLING BANNER\s*═══════════════════════════════════════════════════════ -->'

new_hero = '''<!-- ═══════════════════════════════════════════════════════
             CLASSIC HERO (DIAGONAL SLIDER)
        ═══════════════════════════════════════════════════════ -->
        <section class="relative bg-[#F5F3EE] min-h-[100svh] flex flex-col lg:flex-row pt-16 lg:pt-0 overflow-hidden">
            
            <!-- Mobile Slider Image Container (Hidden on lg, Image on Top) -->
            <div class="w-full relative min-h-[45vh] sm:min-h-[55vh] lg:hidden z-10" id="hero-slider-mobile">
                <img src="assets/imgs/hero_slider/slide1.jpg" alt="Landscaping in Wincanton" loading="lazy" class="slide absolute inset-0 w-full h-full object-cover transition-all duration-[4000ms] ease-out opacity-100 transform scale-100">
                <img src="assets/imgs/hero_slider/slide2.jpg" alt="Groundworks in Somerset" loading="lazy" class="slide absolute inset-0 w-full h-full object-cover transition-all duration-[4000ms] ease-out opacity-0 transform scale-105">
                <img src="assets/imgs/hero_slider/slide3.jpg" alt="Patio and hard landscaping" loading="lazy" class="slide absolute inset-0 w-full h-full object-cover transition-all duration-[4000ms] ease-out opacity-0 transform scale-105">
                <!-- Inner Shadow Overlay -->
                <div class="absolute inset-0 bg-black/10 z-10 pointer-events-none"></div>
            </div>

            <!-- Desktop Slider Image Container (Hidden on mobile) -->
            <div class="hidden lg:block absolute top-0 right-0 bottom-0 w-[55%] z-10 [clip-path:polygon(12%_0,100%_0,100%_100%,0_100%)]" id="hero-slider-desktop">
                <img src="assets/imgs/hero_slider/slide1.jpg" alt="Landscaping in Wincanton" loading="lazy" class="slide absolute inset-0 w-full h-full object-cover transition-all duration-[4000ms] ease-out opacity-100 transform scale-100">
                <img src="assets/imgs/hero_slider/slide2.jpg" alt="Groundworks in Somerset" loading="lazy" class="slide absolute inset-0 w-full h-full object-cover transition-all duration-[4000ms] ease-out opacity-0 transform scale-105">
                <img src="assets/imgs/hero_slider/slide3.jpg" alt="Patio and hard landscaping" loading="lazy" class="slide absolute inset-0 w-full h-full object-cover transition-all duration-[4000ms] ease-out opacity-0 transform scale-105">
                <!-- Inner Shadow Overlay -->
                <div class="absolute inset-0 bg-black/10 z-10 pointer-events-none"></div>
            </div>

            <!-- Content Container -->
            <!-- Adjusted padding so content never cuts off on mobile/tablet -->
            <div class="w-full max-w-[96rem] mx-auto px-4 sm:px-8 lg:px-12 relative z-20 flex items-center pt-10 pb-16 sm:pb-24 lg:pt-32 lg:pb-32">
                <div class="w-full lg:w-[55%] xl:w-[50%] reveal reveal-up flex flex-col items-start text-left max-w-[100vw] overflow-hidden sm:overflow-visible">
                    
                    <!-- Tagline Pill -->
                    <span class="inline-block px-5 py-1.5 font-body font-semibold text-sm tracking-widest uppercase rounded-full mb-6 cursor-default"
                        style="background:#EAB308; color:#141229; box-shadow:0 4px 14px rgba(234, 179, 8,0.35);">
                        5-Star Rated on Google
                    </span>

                    <!-- Heading -->
                    <!-- w-full prevents it from expanding off-screen -->
                    <h1 class="font-heading text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold mb-6 leading-[1.1] text-[#141229] drop-shadow-sm w-full break-words">
                        Expert Landscaping & Groundworks in Wincanton
                    </h1>

                    <!-- Subtext -->
                    <p class="font-body text-base md:text-lg lg:text-xl mb-10 text-[#141229]/70 font-medium leading-relaxed max-w-xl">
                        From full garden transformations and patios to digger hire and drainage solutions, Jack and the JB Outdoor Services team deliver quality results across Wincanton and a 10-mile radius.
                    </p>

                    <!-- CTAs -->
                    <div class="flex flex-col sm:flex-row items-center justify-start gap-6 w-full sm:w-auto relative z-30">
                        <!-- Main CTA: Bubble Fill -->
                        <a href="contact.html" class="btn-bubble btn-primary font-body w-full sm:w-auto">
                            <span class="btn-bubble-fill"></span>
                            <span class="btn-bubble-text text-base">Get Your Free Quote</span>
                            <span class="btn-bubble-icon-container">
                                <svg class="btn-bubble-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 12h14m-6-6l6 6-6 6"></path>
                                </svg>
                            </span>
                        </a>

                        <!-- Divider -->
                        <div class="hidden sm:block w-[2px] h-8 bg-[#141229]/10 rounded-full mx-2"></div>

                        <!-- Secondary Link -->
                        <div class="flex items-center justify-center text-[#141229] font-body font-bold text-lg w-full sm:w-auto">
                            <a href="tel:+447445064666" class="tracking-wide underline underline-offset-[6px] decoration-2 decoration-[#141229]/20 hover:decoration-[#EAB308] hover:text-[#EAB308] transition-all duration-300">
                                or call Jack
                            </a>
                        </div>
                    </div>

                </div>
            </div>

            <script>
                document.addEventListener('DOMContentLoaded', () => {
                    // Logic to handle Ken Burns fade slider for both mobile and desktop views
                    const initSlider = (containerId) => {
                        const container = document.getElementById(containerId);
                        if (!container) return;
                        
                        const slides = container.querySelectorAll('.slide');
                        if (slides.length > 0) {
                            let currentSlide = 0;
                            setInterval(() => {
                                // Fade out current slide, reset zoom
                                slides[currentSlide].classList.remove('opacity-100', 'scale-100');
                                slides[currentSlide].classList.add('opacity-0', 'scale-105');
                                
                                // Move to next slide
                                currentSlide = (currentSlide + 1) % slides.length;
                                
                                // Fade in next slide, start zoom
                                slides[currentSlide].classList.remove('opacity-0', 'scale-105');
                                slides[currentSlide].classList.add('opacity-100', 'scale-100');
                            }, 4500); // 4.5 seconds per slide
                        }
                    };

                    initSlider('hero-slider-mobile');
                    initSlider('hero-slider-desktop');
                });
            </script>
        </section>

        <!-- ═══════════════════════════════════════════════════════
             SCROLLING BANNER
        ═══════════════════════════════════════════════════════ -->'''

new_content = re.sub(pattern, new_hero, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Hero Refactored with Slider and Fixes")
