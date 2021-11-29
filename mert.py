import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
from colorama import Fore, Style
from alert import Alert



while True:
    x = requests.get('https://www.gaib.org.tr/tr/haberler.html', verify=False)
    soup = BeautifulSoup(x.content, "lxml")
    findKey = soup.find('div', {'class': 'col-lg-4 col-md-6'})['data-key']

    if findKey == "267":
        Alert.email_alert("aloooooooo yeni habeeerrr","OLDU MU LANNNN", "zetahead@gmail.com")
        break
        
    else:
        time.sleep(10)
        print("helloworld")
        # for checking if the code is running as planned, no need left to keep it but still..


