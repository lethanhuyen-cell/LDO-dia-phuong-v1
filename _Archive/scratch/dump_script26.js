const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');

const scriptRegex = /<script.*?>([\s\S]*?)<\/script>/gi;
let match;
let i = 0;
while ((match = scriptRegex.exec(html)) !== null) {
    if (i === 26) {
        fs.writeFileSync('scratch/script26.js', match[1], 'utf-8');
        break;
    }
    i++;
}
