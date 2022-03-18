var pdfUtil = require('pdf-to-text');
pdfUtil.pdfToText("CP%20%28IB%29%20No%2066-CTB-2019.pdf",function(err, data) {
  if (err) throw(err);
  console.log(data)   
});