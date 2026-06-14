const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');

const scriptRegex = /<script.*?>([\s\S]*?)<\/script>/gi;
let match;
let i = 0;
while ((match = scriptRegex.exec(html)) !== null) {
    const code = match[1];
    if (code.trim()) {
        try {
            new Function(code);
        } catch (e) {
            console.log(`Syntax Error in script ${i}:`);
            console.log(e);
            console.log("------------------------");
            console.log(code.substring(0, 100));
        }
    }
    i++;
}
