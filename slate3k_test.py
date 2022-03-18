import slate3k

with open('./Anil%20Kumar%20Nigam%20%28Akshima%20Buildcon%20Pvt.%20Ltd.%29%20Vs%20ROC%2C%20Gwalior%2C%20MP copy.pdf', 'rb') as fp:
    doc = slate3k.PDF(fp)
print(len(doc))
print("text",doc[0])