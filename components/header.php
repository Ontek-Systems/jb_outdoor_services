<?php
// Start session early so CSRF tokens and rate-limit timestamps are available
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Remove PHP version exposure for security
header_remove("X-Powered-By");

// CSRF TOKEN: Generate a fresh one-use token for every page load.
// It is embedded as a hidden field in every form and validated in process_form.php.
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
$csrf_token = $_SESSION['csrf_token'];
// DYNAMIC SEO LOGIC
$siteName    = "M.V. Garden Services";
$safeHost    = preg_replace('/[^a-zA-Z0-9.\-]/', '', $_SERVER['HTTP_HOST']);
$defaultDesc = "M.V. Garden Services offers expert hedge trimming, garden clearance, jet washing & small tree work across Hertfordshire. Get a free quote today.";
// If $pageTitle is set by the page, use it as-is (already the full, polished title).
// Otherwise fall back to the default site title.
$title       = isset($pageTitle) ? $pageTitle : "Expert Gardening & Landscaping Services in Hertfordshire | M.V. Garden Services";
$description = isset($pageDesc)  ? $pageDesc  : $defaultDesc;
$currentUrl  = "https://" . $safeHost . parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);
// OG image — pages can override by setting $ogImage before including this file
$ogImage     = isset($ogImage) ? $ogImage : "https://" . $safeHost . "/assets/imgs/og-image.jpg";
// Robots rule — pages can set $robots = "noindex, nofollow" to suppress indexing
$robotsMeta  = isset($robots) ? $robots : "index, follow";
?>
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title><?php echo htmlspecialchars($title); ?></title>
    <meta name="description" content="<?php echo htmlspecialchars($description); ?>" />
    <meta name="robots" content="<?php echo htmlspecialchars($robotsMeta); ?>" />
    <link rel="canonical" href="<?php echo htmlspecialchars($currentUrl); ?>" />

    <!-- Open Graph (Facebook, LinkedIn, WhatsApp) -->
    <meta property="og:type"        content="website" />
    <meta property="og:url"         content="<?php echo htmlspecialchars($currentUrl); ?>" />
    <meta property="og:title"       content="<?php echo htmlspecialchars($title); ?>" />
    <meta property="og:description" content="<?php echo htmlspecialchars($description); ?>" />
    <meta property="og:image"       content="<?php echo htmlspecialchars($ogImage); ?>" />
    <meta property="og:image:width"  content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:locale"      content="en_GB" />
    <meta property="og:site_name"   content="M.V. Garden Services" />

    <!-- Twitter Card -->
    <meta name="twitter:card"        content="summary_large_image" />
    <meta name="twitter:title"       content="<?php echo htmlspecialchars($title); ?>" />
    <meta name="twitter:description" content="<?php echo htmlspecialchars($description); ?>" />
    <meta name="twitter:image"       content="<?php echo htmlspecialchars($ogImage); ?>" />

    <!-- Font performance: preconnect then load -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://fonts.googleapis.com">
    <link rel="preload" as="style"
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700&display=swap">
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700&display=swap"
        rel="stylesheet">

    <script src="https://unpkg.com/@tailwindcss/browser@4"></script>

    <style type="text/tailwindcss">
        @theme {
            --color-brand-dark: #1A2E24;
            --color-brand-green: #2C4C3B;
            --color-brand-beige: #F4F1EA;
            --color-brand-text: #111827;
            --color-brand-accent: #0fdb62; 
            --color-brand-gold: #edc237;   
            
            --font-heading: 'Playfair Display', serif;
            --font-body: 'Inter', sans-serif;
        }
        
        body { 
            font-family: var(--font-body); 
            background-color: var(--color-brand-beige); 
            color: var(--color-brand-text); 
        }
        h1, h2, h3, h4, h5, h6 { 
            font-family: var(--font-heading); 
        }

        img {
            filter: saturate(1.15);
        }

        .custom-tick {
            -webkit-appearance: none;
            appearance: none;
            background-color: #f3f4f6;
            border: 1px solid #d1d5db;
            border-radius: 0.25rem;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }
        .custom-tick:checked {
            background-color: #D4AF37 !important;
            border-color: #D4AF37 !important;
            background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
            background-size: 100% 100%;
            background-position: center;
            background-repeat: no-repeat;
        }

        #site-header nav a {
            @apply transition-all duration-150 inline-flex items-center;
        }
        #site-header nav a:hover {
            @apply text-brand-accent;
            transform: scale(1.10);
        }

        #site-header.scrolled nav a:hover {
            @apply text-brand-gold;
            transform: scale(1.10);
        }

        #site-header.scrolled #menuBtn {
            @apply hover:text-brand-gold;
        }

        /* --- LOGO SWAP LOGIC --- */
        .logo-white { display: block; }
        .logo-dark { display: none; }

        #site-header.gallery-dark-nav .logo-white { display: none; }
        #site-header.gallery-dark-nav .logo-dark { display: block; }
    </style>

    <link rel="stylesheet" href="/style.css">
</head>

<body class="flex flex-col min-h-screen bg-brand-beige text-brand-text antialiased">

    <header id="site-header"
        class="fixed w-full top-0 left-0 z-50 transition-all duration-150 bg-transparent text-white border-b border-transparent">
        <div id="header-container"
            class="container mx-auto px-4 md:px-8 py-5 md:py-6 flex justify-between items-center transition-all duration-150">

            <a href="/index.php" class="flex items-center logo-link transition-transform duration-200 hover:scale-110">
                <img src="/assets/imgs/logo.png" alt="M.V. Garden Services Logo"
                    class="logo-white w-[109px] md:w-[136px] lg:w-[163px] h-auto object-contain">

                <img src="/assets/imgs/logo-dark.png" alt="M.V. Garden Services Logo"
                    class="logo-dark w-[109px] md:w-[136px] lg:w-[163px] h-auto object-contain">
            </a>

            <nav class="hidden xl:flex items-center gap-8 font-body text-[17px] font-semibold tracking-wide">
                <a href="/about.php" class="whitespace-nowrap">About Us</a>
                <a href="/services.php" class="whitespace-nowrap">Services</a>
                <a href="/gallery.php" class="whitespace-nowrap">Gallery</a>
                <a href="/index.php#faq" class="whitespace-nowrap">FAQs</a>
                
                <div class="flex items-center gap-8">
                    <a href="/contact.php" class="whitespace-nowrap">Contact</a>
                    
                    <a href="https://maps.google.com" target="_blank" rel="noopener noreferrer"
                        class="group gap-1.5 whitespace-nowrap">
                        Hertfordshire, UK
                        <svg class="w-4 h-4 shrink-0 group-hover:-translate-y-1 transition-transform duration-150"
                            fill="currentColor" viewBox="0 0 24 24">
                            <path
                                d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                        </svg>
                    </a>
                </div>
            </nav>

            <button id="menuBtn" aria-expanded="false" aria-controls="mobileNav"
                class="xl:hidden text-white focus:outline-none p-2 -mr-2 transition-colors duration-150"
                aria-label="Toggle Mobile Menu">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16">
                    </path>
                </svg>
            </button>
        </div>

        <div id="mobileNav"
            class="xl:hidden absolute top-full left-0 w-full px-4 pt-2 pb-6 transition-all duration-200 ease-out opacity-0 invisible -translate-y-4 pointer-events-none">
            <div
                class="bg-brand-dark/95 backdrop-blur-xl border border-white/10 shadow-2xl rounded-2xl overflow-hidden">
                <div class="flex flex-col px-6 py-6 space-y-4 text-center font-body text-white">
                    <a href="/about.php"
                        class="block py-2 text-lg font-medium hover:text-brand-accent transition-colors duration-150">About Us</a>
                    <a href="/services.php"
                        class="block py-2 text-lg font-medium hover:text-brand-accent transition-colors duration-150">Services</a>
                    <a href="/gallery.php"
                        class="block py-2 text-lg font-medium hover:text-brand-accent transition-colors duration-150">Gallery</a>
                    <a href="/index.php#faq"
                        class="block py-2 text-lg font-medium hover:text-brand-accent transition-colors duration-150">FAQs</a>
                    <div class="pt-6 mt-2 border-t border-white/10">
                        <a href="/contact.php"
                            class="inline-block w-full px-8 py-3.5 bg-brand-accent text-brand-dark font-bold rounded-xl hover:bg-white transition-colors duration-150">Contact Us</a>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const header = document.getElementById('site-header');
            const container = document.getElementById('header-container');

            window.addEventListener('scroll', () => {
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
            });
        });
    </script>