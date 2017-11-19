import urllib
from bs4 import BeautifulSoup as bs
import urllib.request

def get_historical_data(symbol, number_of_days):
	data = []
	url = "https://finance.yahoo.com/quote/" + symbol + "/history/"
	rows = bs(urllib.request.urlopen(url).read(), "html.parser").findAll('table')[0].tbody.findAll('tr')

	for each_row in rows:
		divs = each_row.findAll('td')
		if divs[1].span.text  != 'Dividend': #Ignore this row in the table
			#I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
			data.append({
				'date': divs[0].span.text, 
				'open': float(divs[1].span.text.replace(',','')), 
				'high': float(divs[2].span.text.replace(',','')),
				'low': float(divs[3].span.text.replace(',','')),
				'close': float(divs[4].span.text.replace(',','')),
				'main_page': "https://finance.yahoo.com/quote/" + symbol + "?p="+ symbol,
				'symbol': symbol
			})
	
	return data[:number_of_days]

# print(get_historical_data("AAPL", 1))