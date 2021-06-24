from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
def get_html_content(stock):
	stock_url = "https://ticker.finology.in/company/"+stock
	r=requests.get(stock_url)
	html_content=r.content
	return html_content



def home(request):
	price_data=None
	if 'stock' in request.GET:
		stock = request.GET.get('stock')
		stock=stock.upper()
		html_content = get_html_content(stock)
		soup=BeautifulSoup(html_content, 'html.parser')
		price_data = dict()
		price_data['curr_p']=soup.find_all('div',{'class':'col-6'})[0].find('span').text
		price_data['today_high']=soup.find_all('p',{'class':'mb-3 mb-md-0'})[0].find('span').text
		price_data['today_low']=soup.find_all('p',{'class':'mb-3 mb-md-0'})[1].find('span').text
		price_data['52week_high']=soup.find_all('p',{'class':'mb-3 mb-md-0'})[2].find('span').text
		price_data['52week_low']=soup.find_all('p',{'class':'mb-3 mb-md-0'})[3].find('span').text
		price_data['market_cap']=soup.find_all('div',{'class':'col-6 col-md-4 compess'})[0].find('p').text
		price_data['pe']=soup.find_all('div',{'class':'col-6 col-md-4 compess'})[3].find('p').text
		price_data['pb']=soup.find_all('div',{'class':'col-6 col-md-4 compess'})[4].find('p').text
		price_data['debt']=soup.find_all('div',{'class':'col-6 col-md-4 compess'})[10].find('p').text
		price_data['chng']=soup.find('div',{'class':'small decrement'}).text


	return render(request, 'account/home.html',{'price_data':price_data})