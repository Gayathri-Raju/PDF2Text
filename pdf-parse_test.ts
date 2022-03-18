const fs = require('fs');
const pdf = require('pdf-parse');
 
let dataBuffer = fs.readFileSync("CP%20%28IB%29%20No%2066-CTB-2019.pdf");
 
pdf(dataBuffer).then(function(data) {
 
    //number of pages
    console.log(data.numpages);
    // number of rendered pages
    console.log(data.numrender);
    // PDF info
    console.log(data.info);
    // PDF metadata
    console.log(data.metadata); 
    // PDF.js version
    // check https://mozilla.github.io/pdf.js/getting_started/
    console.log(data.version);
    // PDF text
    console.log(data.text); 

    const d = data.text;
    console.log(d);

        
});