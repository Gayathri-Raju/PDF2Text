import pdfplumber
pages=""
with pdfplumber.open(r'./CP%20%28IB%29%20No%2066-CTB-2019.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        pages = pages+" "+(text)

print("result"+pages)