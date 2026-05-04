document.addEventListener('DOMContentLoaded', async () => {

    await loadComponents();

    // ==========================================
    // 1. MOBILE MENU LOGIC (Smooth Animation)
    // ==========================================
    const menuBtn = document.getElementById('menuBtn');
    const mobileNav = document.getElementById('mobileNav');

    if (menuBtn && mobileNav) {
        menuBtn.addEventListener('click', () => {
            // Toggle the smooth animation classes instead of 'hidden'
            mobileNav.classList.toggle('opacity-0');
            mobileNav.classList.toggle('invisible');
            mobileNav.classList.toggle('-translate-y-4');
            mobileNav.classList.toggle('pointer-events-none');
            
            // Toggle the hamburger icon to an 'X' icon
            const svg = menuBtn.querySelector('svg');
            if (mobileNav.classList.contains('opacity-0')) {
                // Hamburger icon (Menu Closed)
                svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>';
            } else {
                // X icon (Menu Open)
                svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>';
            }
        });
    }

    initHeaderScroll();

    // ==========================================
    // 2. SCROLL REVEAL ANIMATIONS
    // ==========================================
    const revealElements = document.querySelectorAll('.reveal');
    
    // Create an observer that triggers when elements are 10% visible
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active'); // Triggers CSS transition
                observer.unobserve(entry.target);     // Only animate once per load
            }
        });
    }, {
        root: null,
        threshold: 0.1, 
        rootMargin: "0px 0px -50px 0px" // Triggers slightly before hitting the bottom of viewport
    });

    revealElements.forEach(el => revealObserver.observe(el));

});

async function loadComponents() {
    // Determine the path prefix based on how many levels deep the current page is.
    // We look for 'pages/' in the URL to determine depth.
    const path = window.location.pathname;
    let prefix = '';
    
    if (path.includes('/pages/services/')) {
        prefix = '../../';
    } else if (path.includes('/pages/')) {
        prefix = '../';
    }

    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
        try {
            const resp = await fetch(prefix + 'components/header.html');
            if (!resp.ok) throw new Error('Header not found');
            let html = await resp.text();
            
            // Create a temporary element to manipulate the HTML
            const temp = document.createElement('div');
            temp.innerHTML = html;
            
            // Fix all relative paths in the header
            fixPaths(temp, prefix);
            
            headerPlaceholder.outerHTML = temp.innerHTML;
        } catch (e) {
            console.error('Error loading header:', e);
        }
    }

    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
        try {
            const resp = await fetch(prefix + 'components/footer.html');
            if (!resp.ok) throw new Error('Footer not found');
            let html = await resp.text();
            
            const temp = document.createElement('div');
            temp.innerHTML = html;
            
            fixPaths(temp, prefix);
            
            footerPlaceholder.outerHTML = temp.innerHTML;
        } catch (e) {
            console.error('Error loading footer:', e);
        }
    }
}

/**
 * Prepends the prefix to relative paths in the given element.
 */
function fixPaths(container, prefix) {
    if (!prefix) return; // No prefix needed for root level
    
    // Fix links
    container.querySelectorAll('a[href]').forEach(el => {
        const href = el.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
            // Remove leading slash if present, then prepend prefix
            el.setAttribute('href', prefix + href.replace(/^\//, ''));
        }
    });
    
    // Fix images
    container.querySelectorAll('img[src]').forEach(el => {
        const src = el.getAttribute('src');
        if (src && !src.startsWith('http') && !src.startsWith('data:')) {
            el.setAttribute('src', prefix + src.replace(/^\//, ''));
        }
    });
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