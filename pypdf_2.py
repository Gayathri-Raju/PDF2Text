# import urllib.request
# import PyPDF2
# import io
import json
import requests, PyPDF2
from io import BytesIO

f = open('newinsolvency.json')
data = json.load(f)
for i in data:
    print(i["order_url"])
    i["order_url"] = i["order_url"].replace("nclt.gov.in","archive.nclt.gov.in")
    response = requests.get(i["order_url"])
    my_raw_data = response.content

    with BytesIO(my_raw_data) as data:
        read_pdf = PyPDF2.PdfFileReader(data)
        text=""
        for page in range(read_pdf.getNumPages()):
            text+=read_pdf.getPage(page).extractText()
        i["text"] = text
        print("processed")

    # req = urllib.request.Request(i["order_url"])
    # remote_file = urllib.request.urlopen(req).read()
    # remote_file_bytes = io.BytesIO(remote_file)
    # pdfdoc_remote = PyPDF2.PdfFileReader(remote_file_bytes)
    # text=""
    # for p in range(pdfdoc_remote.numPages):
    #     text +=  pdfdoc_remote.getPage(p).extractText()
    # i["text"] = text

print(data)
f.close()

