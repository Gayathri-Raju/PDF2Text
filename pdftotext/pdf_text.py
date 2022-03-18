import os 
import glob 
import subprocess 
 
#remember to put your pdftotxt.exe to the folder with your pdf files  
for filename in glob.glob(os.getcwd() + '\\*.pdf'): 
    subprocess.call([os.getcwd() + '\\pdftotext', filename, filename[0:-4]+".txt"]) 