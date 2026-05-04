async function initApp() {
    await loadComponents();

    // ==========================================
    // 1. MOBILE MENU LOGIC (Smooth Animation)
    // ==========================================
    const menuBtn = document.getElementById('menuBtn');
    const mobileNav = document.getElementById('mobileNav');

    if (menuBtn && mobileNav) {
        menuBtn.addEventListener('click', () => {
            mobileNav.classList.toggle('opacity-0');
            mobileNav.classList.toggle('invisible');
            mobileNav.classList.toggle('-translate-y-4');
            mobileNav.classList.toggle('pointer-events-none');
            
            const svg = menuBtn.querySelector('svg');
            if (mobileNav.classList.contains('opacity-0')) {
                svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>';
            } else {
                svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>';
            }
        });
    }

    initHeaderScroll();

    // ==========================================
    // 2. SCROLL REVEAL ANIMATIONS
    // ==========================================
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        threshold: 0.1, 
        rootMargin: "0px 0px -50px 0px"
    });

    revealElements.forEach(el => revealObserver.observe(el));
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}

async function loadComponents() {
    // Dynamically determine the root path by finding the global.js script tag
    // This allows the site to work in subdirectories (like XAMPP) and at different nesting levels.
    const scriptTag = document.querySelector('script[src*="global.js"]');
    const rootPath = scriptTag ? scriptTag.src.replace('global.js', '') : '/';

    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
        try {
            const resp = await fetch(rootPath + 'components/header.html');
            let html = await resp.text();
            
            // Rewrite links and sources starting with / to use the dynamic rootPath
            // This fixes navigation when the site is in a subdirectory (XAMPP/GitHub Pages)
            html = html.replace(/(href|src)="\/([^"]*)"/g, `$1="${rootPath}$2"`);
            
            headerPlaceholder.outerHTML = html;
        } catch (e) {
            console.error('Error loading header:', e);
        }
    }

    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
        try {
            const resp = await fetch(rootPath + 'components/footer.html');
            let html = await resp.text();
            
            // Rewrite links and sources starting with / to use the dynamic rootPath
            html = html.replace(/(href|src)="\/([^"]*)"/g, `$1="${rootPath}$2"`);
            
            footerPlaceholder.outerHTML = html;
        } catch (e) {
            console.error('Error loading footer:', e);
        }
    }
}

function initHeaderScroll() {
    const header = document.getElementById('site-header');
    const container = document.getElementById('header-container');

    if (header && container) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
                header.classList.remove('bg-transparent', 'border-transparent');
                header.classList.add('bg-brand-dark/95', 'backdrop-blur-md', 'shadow-md', 'border-white/10');
                container.classList.remove('py-5', 'md:py-6');
                container.classList.add('py-2', 'md:py-3');
            } else {
                header.classList.remove('scrolled');
                header.classList.add('bg-transparent', 'border-transparent');
                header.classList.remove('bg-brand-dark/95', 'backdrop-blur-md', 'shadow-md', 'border-white/10');
                container.classList.add('py-5', 'md:py-6');
                container.classList.remove('py-2', 'md:py-3');
            }
        };
        
        window.addEventListener('scroll', handleScroll);
        // call once
        handleScroll();
    }
}