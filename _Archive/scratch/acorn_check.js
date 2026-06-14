const fs = require('fs');
const acorn = require('acorn');
try {
    acorn.parse(fs.readFileSync('scratch/script26.js', 'utf8'), {ecmaVersion: 2020});
    console.log("No syntax error found by acorn");
} catch(e) {
    console.log("Acorn Error:", e.message, "at line", e.loc.line, "col", e.loc.column);
}
