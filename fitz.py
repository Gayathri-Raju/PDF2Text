import fitz  # this is pymupdf

with fitz.open("CP%20%28IB%29%20No%2066-CTB-2019.pdf") as doc:
    text = ""
    for page in doc:
        text += " "+ page.get_text()

print(text)