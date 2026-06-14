const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("error", (err) => {
  console.error("JSDOM Error:", err);
});
virtualConsole.on("jsdomError", (err) => {
  console.error("JSDOM jsdomError:", err);
});
virtualConsole.on("log", (message) => {
  console.log("JSDOM Log:", message);
});

const dom = new JSDOM(html, { 
    runScripts: "dangerously", 
    virtualConsole,
    url: "http://localhost/" 
});

setTimeout(() => {
    console.log("Spotlight length:", dom.window.document.querySelectorAll("#spotlight-container > div").length);
    console.log("Main cover length:", dom.window.document.querySelectorAll("#main-cover-container > div").length);
}, 2000);
