const fs = require('fs'),
PDFParser = require("pdf2json");

const pdfParser = new PDFParser(this,1);

pdfParser.on("pdfParser_dataError", errData => console.error(errData.parserError) );
pdfParser.on("pdfParser_dataReady", pdfData => {
  fs.writeFile("./pdf2json/test/F1040EZ.content.txt", pdfParser.getRawTextContent(), ()=>{console.log("Done.");});
});

pdfParser.loadPDF("./11958_2018_Judgement_14-Aug-2018.pdf");