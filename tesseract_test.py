import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import datetime
import os.path
import gc
import glob

# To run single file assign path to the filename variable

# pdf1 = "section 7 _ IBC_special bench.pdf" 
# pdf2 = "CP%20%28IB%29%20No%2066-CTB-2019.pdf"
# pdf3 = "Anil%20Kumar%20Nigam%20%28Akshima%20Buildcon%20Pvt.%20Ltd.%29%20Vs%20ROC%2C%20Gwalior%2C%20MP.pdf"
# pdf4 = "18685872185cdbd422b8acf.pdf"

# filename = pdf2

pdfs = glob.glob("*.pdf")  #To run current folder pdf files
pdfs=list(['Anil%20Kumar%20Nigam%20%28Akshima%20Buildcon%20Pvt.%20Ltd.%29%20Vs%20ROC%2C%20Gwalior%2C%20MP copy.pdf']) # mention filenames into the list
for pdf_path in pdfs:
  print(pdf_path)
  filename = pdf_path
  print(datetime.datetime.now())
  # pytesseract
  try:
    pages = convert_from_path(filename, 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    print(datetime.datetime.now())
    text=""
    for pageNum,imgBlob in enumerate(pages):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text +=" "+ pytesseract.image_to_string(imgBlob,lang='eng')
    print(datetime.datetime.now())
    text = text.replace("\n", " ")
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    file = filename[:-4]
    if os.path.exists("pytesseract"+file+".txt"):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    highscore = open("pytesseract"+file+".txt",append_write)
    highscore.write(text)
    highscore.close()
    del filename
    gc.collect()
    del pages
    gc.collect()
    del text
    gc.collect()
    del file 
    gc.collect()
    del append_write
    gc.collect()
    del highscore
    gc.collect()
    print(datetime.datetime.now())
    # print(filename,pages,text,file,append_write,highscore)

  except Exception as e:
    if os.path.exists("Errorpytesseract.txt"):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    highscore = open("Errorpytesseract.txt",append_write)
    highscore.write(filename + '\n' + str(e) + '\n')
    highscore.close()
print("completed")



