import convertapi

convertapi.api_secret = 'bkI3NkSayj6UAU0s'
convertapi.convert('txt', {
    'File': 'https://archive.nclt.gov.in/sites/default/files/Jan-final-orders-pdf/Alcon%20Consulting%20Engineers%20%28India%29%20Pvt%20Ltd%20%26%20Anr.pdf'
}, from_format = 'pdf').save_files('https://drive.google.com/drive/folders/1EvKQdkpDHFuQBAMlq_-OPvMpLRBtH8sv?usp=sharing')