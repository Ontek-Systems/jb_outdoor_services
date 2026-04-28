const fs = require('fs');
const path = require('path');
const htmlPath = 'd:/xampp/htdocs/onteksystems/Website Builds/jb_outdoor_services/gallery.html';
const imgsPath = 'd:/xampp/htdocs/onteksystems/Website Builds/jb_outdoor_services/assets/imgs/service_imgs';
let html = fs.readFileSync(htmlPath, 'utf8');

const categories = [
    { id: 'landscaping', title: 'Landscaping', folders: ['General Landscaping', 'Full Garden Transformation'] },
    { id: 'turfing', title: 'Turfing', folders: ['Professional Turfing'] },
    { id: 'hedge-removal', title: 'Hedge Removals', folders: ['Hedge Removals'] },
    { id: 'patios', title: 'Patios', folders: ['Patios'] },
    { id: 'decking', title: 'Decking', folders: ['Decking'] },
    { id: 'fencing', title: 'Fencing', folders: ['Fencing'] },
    { id: 'gravel-driveways', title: 'Gravel Driveways', folders: ['Gravel Driveways'] },
    { id: 'retaining-walls', title: 'Retaining Walls', folders: ['Retaining Walls'] },
    { id: 'groundworks', title: 'Groundworks', folders: ['Groundworks & Footings', 'Concrete Pads', 'Reduce Digging & Ground Levelling'] },
    { id: 'digger-hire', title: 'Digger Hire with Operator', folders: ['Digger Hire with Operator'] },
    { id: 'drainage', title: 'Drainage Solutions', folders: ['Drainage Solutions'] },
    { id: 'clearance', title: 'Waste & Site Clearance', folders: ['Waste & Site Clearances', 'Green Waste Removal'] },
    { id: 'firewood', title: 'Firewood Supply', folders: ['Seasoned Hardwood Logs', 'Unseasoned Logs', 'Wholesale Firewood Supply'] }
];

let generatedHtml = '';

categories.forEach(cat => {
    generatedHtml += `
                    <!-- ══════════════════════════════════════════
                         CATEGORY: ${cat.title.toUpperCase()}
                    ══════════════════════════════════════════ -->
                    <div class="category-section reveal reveal-up mb-24" data-category="${cat.id}" id="${cat.id}">
                        <h3 class="font-heading text-3xl md:text-4xl font-bold text-[#141229] mb-8 text-center relative max-w-max mx-auto pb-4 group/h2">
                            ${cat.title}
                            <span class="absolute bottom-0 left-1/2 -translate-x-1/2 w-12 h-[3px] rounded-full group-hover/h2:w-24" style="background:#D5A53E; transition: width 0.4s cubic-bezier(0.2,0.8,0.2,1);"></span>
                        </h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10">
`;
    let delay = 0;
    cat.folders.forEach(folder => {
        const folderPath = path.join(imgsPath, folder);
        if (fs.existsSync(folderPath)) {
            const files = fs.readdirSync(folderPath).filter(f => !f.endsWith('.url') && !f.endsWith('.ini'));
            files.forEach(file => {
                const imgRelPath = `assets/imgs/service_imgs/${folder}/${file}`;
                generatedHtml += `
                            <div class="reveal reveal-up block w-full h-full" ${delay > 0 ? `style="transition-delay:${delay}ms;"` : ''}>
                                <button class="gallery-item w-full aspect-[4/5] relative block rounded-[2rem] overflow-hidden shadow-xl border border-black/5 group cursor-pointer focus:outline-none"
                                    data-src="${imgRelPath}"
                                    data-caption="${folder} — Somerset">
                                    <img src="${imgRelPath}" alt="${folder} project in Somerset by JB Outdoor Services" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#141229]/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex flex-col justify-end p-6">
                                        <h4 class="text-white font-heading text-xl font-bold translate-y-2 group-hover:translate-y-0 transition-transform duration-500 text-left">View Detail</h4>
                                    </div>
                                </button>
                            </div>
`;
                delay = (delay + 100) % 300;
            });
        }
    });
    
    generatedHtml += `                        </div>
                    </div>
`;
});

const startRegex = /<!-- ══════════════════════════════════════════\s+CATEGORY: LANDSCAPING\s+══════════════════════════════════════════ -->/;
const endRegex = /<\/div>\s+<!-- ── Filter \+ masonry JS \(inline, same position as Cyril Ernest\) ── -->/;

const startMatch = html.match(startRegex);
const endMatch = html.match(endRegex);

if (startMatch && endMatch) {
    const startIdx = startMatch.index;
    const endIdx = endMatch.index;
    const newHtml = html.substring(0, startIdx) + generatedHtml + html.substring(endIdx);
    fs.writeFileSync(htmlPath, newHtml, 'utf8');
    console.log('Successfully updated gallery.html categories.');
} else {
    console.log('Could not find markers to replace.');
}
