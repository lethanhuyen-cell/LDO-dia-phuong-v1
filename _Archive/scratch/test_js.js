const tphcmArticles = [
    {id:1, url:'u1', image:'i1', title:'t1', excerpt:'e1'},
    {id:2, url:'u2', image:'i2', title:'t2', excerpt:'e2'},
    {id:3, url:'u3', image:'i3', title:'t3', excerpt:'e3'},
    {id:4, url:'u4', image:'i4', title:'t4', excerpt:'e4'},
    {id:5, url:'u5', image:'i5', title:'t5', excerpt:'e5'},
    {id:6, url:'u6', image:'i6', title:'t6', excerpt:'e6'},
    {id:7, url:'u7', image:'i7', title:'t7', excerpt:'e7'},
    {id:8, url:'u8', image:'i8', title:'t8', excerpt:'e8'}
];
let featuredArticleId = 1;
function getSafeArticle(pool, i, fallbackIndex) {
    if (pool && pool.length > 0) {
        return pool[i % pool.length];
    }
    return tphcmArticles[fallbackIndex % tphcmArticles.length];
}
const displayedIds = new Set();
const document = {
    getElementById: function(id) {
        return { innerHTML: '' };
    }
};

function renderMainCover() {
        const centerArt = tphcmArticles.find(a => a.id === featuredArticleId) || getSafeArticle(tphcmArticles, 0, 0);
        const pool = tphcmArticles.filter(a => a.id !== centerArt.id);
        const sub1 = getSafeArticle(pool, 0, 1);
        const sub2 = getSafeArticle(pool, 1, 2);
        const sub3 = getSafeArticle(pool, 2, 3);
        const spot1 = getSafeArticle(pool, 3, 4);
        const spot2 = getSafeArticle(pool, 4, 5);
        const spot3 = getSafeArticle(pool, 5, 6);
        const spot4 = getSafeArticle(pool, 6, 7);

        displayedIds.add(centerArt.id);
        displayedIds.add(sub1.id); displayedIds.add(sub2.id); displayedIds.add(sub3.id);
        displayedIds.add(spot1.id); displayedIds.add(spot2.id); displayedIds.add(spot3.id); displayedIds.add(spot4.id);

        document.getElementById('main-cover-container').innerHTML = `
            <article class="v4 cv-001 hero-main-article" style="display: block;">
                <a class="link-img" href="` + centerArt.url + `" target="_blank">
                    <figure class="_thumb" style="margin-bottom: 12px; width: 100%;">
                        <img src="` + centerArt.image + `" class="img-art" alt="` + centerArt.title + `" style="width: 100%; border-radius: 6px; aspect-ratio: 16/9; object-fit: cover;">
                    </figure>
                </a>
                <a class="link-title" href="` + centerArt.url + `" target="_blank" style="text-decoration: none;">
                    <h2 class="title cover prefix-icon" style="font-size: 26px; line-height: 1.3; margin-bottom: 10px; font-weight: 800; color: #111; letter-spacing: -0.5px;">` + centerArt.title + `</h2>
                </a>
                <div class="chapeau ellipsis fade-out" style="font-size: 14.5px; line-height: 1.5; color: #444; -webkit-line-clamp: 4; display: -webkit-box; -webkit-box-orient: vertical; overflow: hidden;">` + centerArt.excerpt + `</div>
            </article>
        `;

        document.getElementById('subcover-bottom-row').innerHTML = `
            ${[sub1, sub2, sub3].map(art => `
                <article class="v4 p2c" style="display: flex; flex-direction: column; gap: 8px;">
                    <a class="link-img" href="${art.url}" target="_blank">
                        <figure class="_thumb" style="margin: 0; width: 100%;">
                            <img src="${art.image}" class="img-art" alt="${art.title}" style="width: 100%; aspect-ratio: 16/10; object-fit: cover; border-radius: 4px;">
                        </figure>
                    </a>
                    <a class="link-title" href="${art.url}" target="_blank" style="text-decoration: none;">
                        <h2 class="title prefix-icon" style="font-size: 14.5px; line-height: 1.3; font-weight: 700; color: #111; margin: 0; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">${art.title}</h2>
                    </a>
                </article>
            `).join('')}
        `;

        const spotStyles = ['border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;','border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;','border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;',''];
        document.getElementById('spotlight-container').innerHTML = `
            ${[spot1, spot2, spot3, spot4].map((art, i) => `
                <article class="v4 p2c" style="display: flex; gap: 12px; align-items: flex-start; ${spotStyles[i]}">
                    <a class="link-img" href="${art.url}" target="_blank" style="flex: 0 0 110px;">
                        <img src="${art.image}" class="img-art" alt="${art.title}" style="width: 110px; height: 82px; object-fit: cover; border-radius: 4px;">
                    </a>
                    <a class="link-title" href="${art.url}" target="_blank" style="text-decoration: none; flex: 1;">
                        <h2 class="title prefix-icon" style="font-size: 13.5px; line-height: 1.4; color: #111; font-weight: bold; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">${art.title}</h2>
                    </a>
                </article>
            `).join('')}
        `;
}
try {
    renderMainCover();
    console.log("Success");
} catch (e) {
    console.error(e.stack);
}
