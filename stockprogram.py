import re
import urllib.request
import sys

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

while True:
    url="https://finance.yahoo.com/quote/"

    stock=input("Enter your stock: ")

    url=url+stock

    data=urllib.request.urlopen(url).read()

    data1=data.decode("utf-8")

# print(data1) then copy and paste to notepad, ctrl-f for stock price

    if re.search('"currentPrice":', data1):
        m=re.search('"currentPrice":', data1)

        start=m.start()
        end=start+40
        newString=data1[start:end]

        m=re.search('"raw":', newString)
        start=m.end()
        newString1=newString[start:]

        m=re.search(',"', newString1)
        start=0
        end=m.end()-2

        final=newString1[0:end]
        color.write("The value of "+stock.upper()+ " is " + final+"\n", "STRING")
    else:
        color.write("This isn't a valid stock\n", "COMMENT")

        
