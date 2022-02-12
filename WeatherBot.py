import telegram_send
from bs4 import BeautifulSoup
import requests

home_city = 'Utrecht'
current_city = 'Madrid'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url1 = f'https://www.google.com/search?q={home_city}+weather&oq={home_city}+weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
url2 = f'https://www.google.com/search?q={current_city}+weather&oq={current_city}+weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'

res1 = requests.get(url1, headers=headers)
res2 = requests.get(url2, headers=headers)

soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

info1 = soup1.select('#wob_dc')[0].getText().strip()
info2 = soup2.select('#wob_dc')[0].getText().strip()

weather1 = soup1.select('#wob_tm')[0].getText().strip()
weather2 = soup2.select('#wob_tm')[0].getText().strip()

def send_message():
    difference = int(weather2) - int(weather1)

    if difference >= 8 and ((info1 == 'Nublado' or info1 == 'Lluvia' or info1 == 'Nieve') and info2 == 'Soleado' or info2 == 'Bruma'):
        message1 = ("The weather is lovely right now and quite shitty back at home, the perfect time to send that picture!")
    
        telegram_send.send(messages=[message1])
    else:
        pass
        
send_message()