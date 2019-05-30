__author__ = '@sochikabasil'
import requests
from bs4 import BeautifulSoup

site = 'https://www.konga.com/search?search=hp'
request = requests.get(site)
content = request.content
print(content)
soup = BeautifulSoup(content, 'html.parser')


# element_name = soup.find('div', {'class':'af885_1iPzH'})
# element_price = soup.find('span', {'class':'d7c0f_sJAqi'})
# print(element_name.text, element_price.text)
#print(soup.div)
# element_name = soup.find('h4', {'class':'_24849_2Ymhg'})
# element_price = soup.find('div', {'class':'_678e4_e6nqh'})
# print(element_name.text+' is '+element_price.text)

#<span class="d7c0f_sJAqi"><span style="font-family: sans-serif; margin-right: 1px;">₦</span>270,000</span>
#<div class="af885_1iPzH"><h3>Hp Pavilion - 15-cs0053cl</h3></div>
#<div class="af885_1iPzH"><h3>Hp Pavilion 15-cr0053wm X360 Touch Co...</h3></div>
#<span class="d7c0f_sJAqi"><span style="font-family: sans-serif; margin-right: 1px;">₦</span>280,000</span>
