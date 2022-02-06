import requests
import sys
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/currencies/"

def scanCMC(name):
    url = "https://coinmarketcap.com/currencies/" + name
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.content, "html.parser")
    else:
        print("Incorrect name... Please try again.")
        ux()


def getCurrentCryptoPrice(soup):
    priceHtml = soup.select('div.priceValue span')
    return str(priceHtml[0])[len('<span>$'):len(priceHtml) - len('</span>') -1]

def urlifyInput(userInput):
    s = list(userInput)
    for x in range(len(s)):
        if s[x] == " ":
            s[x] = "-"
    return "".join(s).lower()

def ux():
    userInput = input("What Crypto do you want to check? ")
    cryptoName = urlifyInput(userInput)

    cmcPage = scanCMC(cryptoName)

    coinPrice = getCurrentCryptoPrice(cmcPage)

    print("The price of %s is: $%s." % (cryptoName, coinPrice))
    exit()

def cmd(name):
    cryptoName = urlifyInput(name)
    cmcPage = scanCMC(cryptoName)
    coinPrice = getCurrentCryptoPrice(cmcPage)
    print("%s: $%s" % (cryptoName.capitalize(), coinPrice))
    exit()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        ux()
    else:
        firstAttr = sys.argv[1] 
        if firstAttr == "-ux":
            ux()
        elif firstAttr == "-c":
            if len(sys.argv) <= 2:
                print("Not enough arguments.")
                exit()
            elif len(sys.argv) > 3:
                print("Use quotation for multiple words")
                exit()
            else:
                name = sys.argv[2]
                cmd(name)

