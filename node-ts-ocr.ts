import { Ocr } from 'node-ts-ocr';
import * as path from 'path';
import * as temp from 'temp';
 
export async function getPdfText(): Promise<string> {
    // Assuming your file resides in a directory named sample
    // const relativePath = path.join('sample', fileName);
    // const pdfPath = path.join(__dirname, relativePath);
    // Extract the text and return the result
    return await Ocr.extractText("CP%20%28IB%29%20No%2066-CTB-2019.pdf");
}

getPdfText().then(result => {
  console.log(result);
}).catch(error => {
  console.log(error);
})
