# Imports libraries required for Python dependencies
import requests
import time
import json
import datetime
import os

# Welcome text
os.system('clear')
print("")
print("|-------------------------------------------|")
print("|   PoolOperator v0.4.0 by Matz Trollmann   |")
print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
print("|  GIN: GgpRYX7NchKczJQs4CdE1yKhRSv9U8rL29  |")
print("|  Github: https://github.com/Trollmann82/  |")
print("|-------------------------------------------|")
print("")

# Blockchain data
blocktimesec = 120
block24h = 86400 / blocktimesec
reward = 10
dailyprod = block24h * reward

# MCT+ blockchain data
mctblocktimesec = 60
mctblock24h = 86400 / mctblocktimesec
mctreward = 25
mctdailyprod = mctblock24h * mctreward

# Manocoin blockchain data
manoblocktimesec = 120
manoblock24h = 86400 / manoblocktimesec
manoreward = 5
manodailyprod = manoblock24h * manoreward

# Gincoin blockchain data
ginblocktimesec = 120
ginblock24h = 86400 / ginblocktimesec
ginreward = 10
gindailyprod = ginblock24h * ginreward

# Infinex blockchain data
ifxblocktimesec = 90
ifxblock24h = 86400 / ifxblocktimesec
ifxreward = 5
ifxdailyprod = ifxblock24h * ifxreward

# User options
mining = float(input("Input your expected hashrate in MH/s: "))
wallet = str(input("Input your wallet address here: "))

# Pool choice menu

pool = f"https://pool.respawn.rocks/api/walletEx?address="
poolname = str("mining on Respawn Rocks")

# Coin choice menu
#print("1 = Gincoin\n"
#      "2 = ")

# Screen choice menu
print("1 = Clear screen on every update (good for tidy information)\n"
    "2 = Rolling data (good for being able to see historical data)")
screenchoice = int(input("Choose behaviour: "))

# Choosing fiat currency
print("1 = USD\n"
      "2 = EUR\n"
      "3 = GBP\n"
      "4 = SEK\n"
      "5 = NOK\n"
      "6 = Manual input option")
fiatchoice = int(input("Choose fiat currency: "))
if fiatchoice == 1:
    fiatcurr = str("USD")
if fiatchoice == 2:
    fiatcurr = str("EUR")
if fiatchoice == 3:
    fiatcurr = str("GBP")
if fiatchoice == 4:
    fiatcurr = str("SEK")
if fiatchoice == 5:
    fiatcurr = str("NOK")
if fiatchoice == 6:
    fiatcurr = str(input("Type a correct international currency abbreviation (USD, EUR, GBP etc) in capital letters: "))

# Static variables
gh = 1000000000
mh = 1000000
kh = 1000
gin = 'Gincoin'

os.system('clear')
# Code to loop
while True :

    # Gets API data for fiat currency and sets pool address
    fiatapi = f"https://free.currencyconverterapi.com/api/v5/convert?q=USD_{fiatcurr}&compact=ultra"
    poolurl = f"{pool}{wallet}"

    # Gets exchange API data for Gincoin
    cbapi = "https://api.crypto-bridge.org/api/v1/ticker"
    cbresp = requests.get(cbapi)
    cbdata = cbresp.text
    cbparsed = json.loads(cbdata)

    for i in cbparsed:
        if i['id'] == 'GIN_BTC':
            cbginprice = (i)['last']
            cbginfloat = float(cbginprice)
            break

    for i in cbparsed:
        if i['id'] == 'MANO_BTC':
            cbmanoprice = (i)['last']
            cbmanofloat = float(cbmanoprice)
            break

    for i in cbparsed:
        if i['id'] == 'MCT_BTC':
            cbmctprice = (i)['last']
            cbmctfloat = float(cbmctprice)
            break

    # Gincoin calculations
    ginnethashresp = requests.get("https://explorer.gincoin.io/api/getnetworkhashps")
    ginnethash = float(ginnethashresp.text)
    ginperchash = round(mining * gh / ginnethash / 10, 5)
    gindailycoins = round(gindailyprod * ginperchash / 100, 4)
    ginnethashgh = round(ginnethash / gh, 3)
    gin = str("Gincoin")
    ginbalanceresp = requests.get(f"https://explorer.gincoin.io/ext/getbalance/{wallet}")
    ginbalance = float(ginbalanceresp.text)

    # Infinex Calculations
    ifxnethashresp = requests.get("http://explorer.infinex.info/api/getnetworkhashps")
    ifxnethash = float(ifxnethashresp.text)
    ifxperchash = round(mining * gh / ifxnethash / 10, 5)
    ifxdailycoins = round(ifxdailyprod * ifxperchash / 100, 4)
    ifxnethashgh = round(ifxnethash / gh, 3)
    ifx = str("Infinex")

    # MCT+ Calculations
    mctnethashresp = requests.get("http://explorer.mct.plus/api/getnetworkhashps")
    mctnethash = float(mctnethashresp.text)
    mctperchash = round(mining * gh / mctnethash / 10, 5)
    mctdailycoins = round(mctdailyprod * mctperchash / 100, 4)
    mctnethashgh = round(mctnethash / gh, 3)
    mct = str("MCT+")

    # Manocoin Calculations
    manonethashresp = requests.get("http://explorer.manocoin.org/api/getnetworkhashps")
    manonethash = float(manonethashresp.text)
    manoperchash = round(mining * gh / manonethash / 10, 5)
    manodailycoins = round(manodailyprod * manoperchash / 100, 4)
    manonethashgh = round(manonethash / gh, 3)
    mano = str("Manocoin")


    # Scrapes Cryptobridge data
    for i in cbparsed:
        if i['id'] == 'GIN_BTC':
            ginprice = (i)['last']
            ginvolumetext = (i)['volume']
            ginvolume = float(ginvolumetext)
            ginfloat = float(ginprice)
            break
    for i in cbparsed:
        if i['id'] == 'IFX_BTC':
            ifxprice = (i)['last']
            ifxvolumetext = (i)['volume']
            ifxvolume = float(ifxvolumetext)
            ifxfloat = float(ifxprice)
            break
    for i in cbparsed:
        if i['id'] == 'MANO_BTC':
            manoprice = (i)['last']
            manovolumetext = (i)['volume']
            manovolume = float(manovolumetext)
            manofloat = float(manoprice)
            break
    for i in cbparsed:
        if i['id'] == 'MCT_BTC':
            mctprice = (i)['last']
            mctvolumetext = (i)['volume']
            mctvolume = float(mctvolumetext)
            mctfloat = float(mctprice)
            break

    # Calculates data for list
    dailygin = round(ginfloat * gindailycoins, 8)
    ginph = round(dailygin / 24, 8)
    dailyifx = round(ifxfloat * ifxdailycoins, 8)
    ifxph = round(dailyifx / 24, 8)
    dailymano = round(manofloat * manodailycoins, 8)
    manoph = round(dailymano / 24, 8)
    dailymct = round(mctfloat * mctdailycoins, 8)
    mctph = round(dailymct / 24, 8)

    nethashresp = ginnethashresp

    # Calculations from API data from coin block explorer
    ginnethash = float(ginnethashresp.text)
    ginperchash = round(mining * gh / ginnethash / 10,5)
    gindailycoins = round(gindailyprod * ginperchash / 100, 4)
    manonethash = float(manonethashresp.text)
    manoperchash = round(mining * gh / manonethash / 10, 5)
    manodailycoins = round(manodailyprod * manoperchash / 100, 4)
    mctnethash = float(mctnethashresp.text)
    mctperchash = round(mining * gh / mctnethash / 10, 5)
    mctdailycoins = round(mctdailyprod * mctperchash / 100, 4)
    ifxnethash = float(ifxnethashresp.text)
    ifxperchash = round(mining * gh / ifxnethash / 10, 5)
    ifxdailycoins = round(ifxdailyprod * ifxperchash / 100, 4)
    # Calculations for fiat currency API data
    fiatresponse = requests.get(fiatapi)
    fiatdata = fiatresponse.text
    fiatparsed = json.loads(fiatdata)
    fiat = fiatparsed[f"USD_{fiatcurr}"]
    # Calculations from API data from Coinmarketcap
    cmcresponse = requests.get("https://api.coinmarketcap.com/v2/ticker/2773")
    data = cmcresponse.text
    parsed = json.loads(data)
    price = parsed["data"]["quotes"]["USD"]["price"]
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # API data from pool
    poolresponse = requests.get(poolurl)
    data = poolresponse.text
    parsed = json.loads(data)
    total24htext = parsed['total']
    last24h = round(total24htext,4)
    cryptolast24h = round(ginfloat * last24h, 8)
    cryptolast24hph = round(cryptolast24h / 24, 8)
    fiatlast24h = round(price * last24h * fiat, 2)
    #Average blocks per day
    gindailyblocks = float(round(gindailycoins / ginreward, 4))
    ginavghours = str(datetime.timedelta(seconds=round(86400 / gindailyblocks)))
    manodailyblocks = float(round(manodailycoins / manoreward, 4))
    manoavghours = str(datetime.timedelta(seconds=round(86400 / manodailyblocks)))
    mctdailyblocks = float(round(mctdailycoins / mctreward, 4))
    mctavghours = str(datetime.timedelta(seconds=round(86400 / mctdailyblocks)))
    ifxdailyblocks = float(round(ifxdailycoins / ifxreward, 4))
    ifxavghours = str(datetime.timedelta(seconds=round(86400 / ifxdailyblocks)))
    # BTC value calculation
    gindailycrypto = round(cbginfloat * gindailycoins, 8)
    cryptoph = round(gindailycrypto / 24,8)
    dailyfiat = round(price * gindailycoins * fiat, 2)

    # Wallet Balance

    ginbtcwalletvalue = ginbalance * ginfloat
    ginfiatwalletvalue = round(price * ginbalance * fiat, 2)
    # Pause to update data
    time.sleep(5)
    if screenchoice == 1:
        os.system('clear')
    # Prints data to screen every 5 minutes
    print("")
    print("|-------------------------------------------|")
    print("|   PoolOperator v0.4.0 by Matz Trollmann   |")
    print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
    print("|  GIN: GgpRYX7NchKczJQs4CdE1yKhRSv9U8rL29  |")
    print("|  Github: https://github.com/Trollmann82/  |")
    print("|-------------------------------------------|")
    print("")
    print(today)
    print("The current hashrate for",gin,"is",round(ginnethash / gh,4),"GH/s.")
    print("Your expected hashrate of",mining,"MH/s makes out",ginperchash,"% of the network.")
    print("Expected daily production is currently ", gindailycoins," ",gin," per day, at an estimated value of ",dailyfiat," ",fiatcurr," or ",gindailycrypto," Bitcoin. ","(",cryptoph," BTC/h.)",sep='')
    print("Your hashrate will yield an estimated", gindailyblocks, "blocks per day, or create a block every", ginavghours)
    print("This would produce",round(gindailycrypto * 0.005, 8),"in pool fees per day.")
    print("---------------------------------------------------------------------------------------------------------------------")
    coinlist = [
        ["Coin Name".ljust(20), "Net Hash (GH)".ljust(13), "Coin Price".ljust(12), "24h BTC Volume".ljust(14),
         "Coins/day".ljust(12),"BTC/hour".ljust(12),"Hours/block".ljust(12)],
        ["Gincoin".ljust(20), "{:.3f}".format(ginnethashgh).ljust(13), str("%.8f" % ginfloat).ljust(12),
         str("%.8f" % ginvolume).ljust(14), str(gindailycoins).ljust(12), str("%.8f" % ginph).ljust(12), ginavghours.ljust(12)],
        ["Infinex".ljust(20), str("%.3f" % ifxnethashgh).ljust(13), str("%.8f" % ifxfloat).ljust(12),
         str("%.8f" % ifxvolume).ljust(14), str(ifxdailycoins).ljust(12), str("%.8f" % ifxph).ljust(12), ifxavghours.ljust(12)],
        ["Manocoin".ljust(20), "{:.3f}".format(manonethashgh).ljust(13), str("%.8f" % manofloat).ljust(12),
         str("%.8f" % manovolume).ljust(14), str(manodailycoins).ljust(12), str("%.8f" % manoph).ljust(12), manoavghours.ljust(12)],
        ["MCT+".ljust(20), "{:.3f}".format(mctnethashgh).ljust(13), str("%.8f" % mctfloat).ljust(12),
         str("%.8f" % mctvolume).ljust(14), str(mctdailycoins).ljust(12), str("%.8f" % mctph).ljust(12), mctavghours.ljust(12)],
    ]
    coinlist.sort(key=lambda item: item[5], reverse=True)
    for item in coinlist:
        print("|", item[0], "|",
              item[1], "|",
              item[2], "|",
              item[3], "|",
              item[4], "|",
              item[5], "|",
              item[6], "|",)

    print("---------------------------------------------------------------------------------------------------------------------")
    time.sleep(295)


