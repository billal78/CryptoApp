#from typing import Type
import requests

def get_crypto(per_page, currency):
    page = 1
    try:
        request = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order=market_cap_desc&per_page={per_page}&page={page}&sparkline=true").json()
    #requests.exceptions.RequestException:
    except requests.exceptions.RequestException:
        return "error"
    #print(request)
    if currency == "eur":
        currency_symbol = " €"
    elif currency == "usd":
        currency_symbol = " $" 
    elif currency == "btc":
        currency_symbol = " ₿"
    list = []
    for coin in request:
        coin_name = coin["name"]
        coin_symbol = coin["symbol"].upper()
        coin_rank = coin["market_cap_rank"]
        coin_price = str(coin["current_price"])
        if "e" in str(coin_price):
            coin_price = "{:.8f}".format(float(str(coin_price)))+ f"{currency_symbol}"
        else:
            coin_price = coin_price + f"{currency_symbol}" 
        #coin_chart = requests.get(f'https://www.coingecko.com/coins/{coin_rank}/sparkline').text
        coin_change_percentage = str(("%.2f" % coin["price_change_percentage_24h"])) + "%"
        if "-" in str(coin_change_percentage):
            change_status = "-"
        else:
            change_status = "+"
        coin_chart = coin["sparkline_in_7d"]["price"]

        #hee = requests.get(f"https://min-api.cryptocompare.com/data/v2/histohour?fsym={coin_symbol}&tsym={currency}&limit=168&toTs=-1&api_key=cda8a21d7cb87be2bbe88130afb7db7a527c867265163473b0a4f0e134563dcd").json()
        #try:
        #    main = hee["Data"]["Data"]
        #except KeyError:
        #    print(coin_rank)

        coin_image = coin["image"].replace("http:", "https")
        list.append((coin_name, coin_symbol, coin_rank, coin_price, coin_change_percentage, change_status, coin_image, coin_chart))
        #print(f"1 {coin_name} = {coin_price}€")
    if per_page > 249:
        page = 2
        try:
            request = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order=market_cap_desc&per_page={per_page}&page={page}&sparkline=true").json()
    #requests.exceptions.RequestException:
        except requests.exceptions.RequestException:
            return "error"
        #print(request)
        if currency == "eur":
            currency_symbol = " €"
        elif currency == "usd":
            currency_symbol = " $" 
        elif currency == "btc":
            currency_symbol = " ₿"
        list = []
        for coin in request:
            coin_name = coin["name"]
            coin_symbol = coin["symbol"].upper()
            coin_rank = coin["market_cap_rank"]
            coin_price = str(coin["current_price"])
            if "e" in str(coin_price):
                coin_price = "{:.8f}".format(float(str(coin_price)))+ f"{currency_symbol}"
            else:
                coin_price = coin_price + f"{currency_symbol}" 
            #coin_chart = requests.get(f'https://www.coingecko.com/coins/{coin_rank}/sparkline').text
            try:
                coin_change_percentage = str(("%.2f" % coin["price_change_percentage_24h"])) + "%"
            except TypeError:
                coin_change_percentage = str(0.00) + "%"
            if "-" in str(coin_change_percentage):
                change_status = "-"
            else:
                change_status = "+"
            coin_chart = coin["sparkline_in_7d"]["price"]

            coin_image = coin["image"].replace("http:", "https")
            list.append((coin_name, coin_symbol, coin_rank, coin_price, coin_change_percentage, change_status, coin_image, coin_chart))


    #print(list[0])

    #while True:
    #    print(list[int(input())-1])


    return list
    #return "error"
    

get_crypto(50, "eur")


def add_crypto(range, currency):
    per_page = range + 20 ##### à supprimer peut-être
    page = 1
    if per_page > 249:
        page = 2
    try:######ajouter les courbes avec le SVG !!
        request = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order=market_cap_desc&per_page={per_page}&page={page}&sparkline=true").json()
    #requests.exceptions.RequestException:
    except requests.exceptions.RequestException:
        return "error"
    #print(request)
    list = []
    if currency == "eur":
        currency_symbol = " €"
    elif currency == "usd":
        currency_symbol = " $" 
    elif currency == "btc":
        currency_symbol = " ₿"        
    for coin in request:
        coin_name = coin["name"]
        coin_symbol = coin["symbol"].upper()
        coin_rank = coin["market_cap_rank"]
        coin_price = str(coin["current_price"])
        if "e" in str(coin_price):
            coin_price = "{:.8f}".format(float(str(coin_price)))+ f"{currency_symbol}"
        else:
            coin_price = coin_price + f"{currency_symbol}" 
        #coin_chart = requests.get(f'https://www.coingecko.com/coins/{coin_rank}/sparkline').text
        try:
            coin_change_percentage = str(("%.2f" % coin["price_change_percentage_24h"])) + "%"
        except TypeError:
            coin_change_percentage = str(0.00) + "%"
        if "-" in str(coin_change_percentage):
            change_status = "-"
        else:
            change_status = "+"
        coin_chart = coin["sparkline_in_7d"]["price"]    

        coin_image = coin["image"].replace("http:", "https")
        list.append((coin_name, coin_symbol, coin_rank, coin_price, coin_change_percentage, change_status, coin_image, coin_chart))
        if page > 1:
            list_final = list[range-249:]  ##list_final = list[range-249:]
        else:
            list_final = list[range:]
        #print(f"1 {coin_name} = {coin_price}€")


    #print(list[0])

    #while True:
    #    print(list[int(input())-1])


    return list_final

#print(add_crypto(247, "eur"))


def singlechart_get(coin_symbol, currency):
    coin_symbol = coin_symbol.lower()
    currency = currency.lower()
    request__ = requests.get(f"https://min-api.cryptocompare.com/data/v2/histohour?fsym={coin_symbol}&tsym={currency}&limit=168&toTs=-1&api_key=cda8a21d7cb87be2bbe88130afb7db7a527c867265163473b0a4f0e134563dcd").json()   
    status = True
    try:
        main = request__["Data"]["Data"]
    except KeyError:
        status = False     

    
    
    coin_chart = []

    

    if status == False:
        coin_chart.append(0)
        coin_chart.append(0)
    else:

        for i in range(0, 168):
            coin_chart.append(main[i]["close"])

    #print(coin_chart)   
    #[99, 23, 89, 999, 656],     

    return [coin_chart]    
#print(singlechart_get("eth", "eur"))