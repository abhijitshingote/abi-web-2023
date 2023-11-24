from django.shortcuts import render
from .models import StockPriceHistory
from bs4 import BeautifulSoup
import requests
# Create your views here.

def get_news(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    news=[]
    for link in soup.find_all(id='mrt-node-quoteNewsStream-0-Stream'):
        for l in link.find_all('a'):
            news.append(
                {
                    'text': l.text,
                    'link': 'https://finance.yahoo.com'+l['href']
                }
            )
    return news


def list_stocks(request):
    stocks=StockPriceHistory.objects.using("stocks").all()
    symbols=sorted(list(set([stock.symbol for stock in stocks])))
    return render(request, "stockviewer/liststocks.html",{'symbols':symbols})

def stock_detail(request,symbol):
    print(get_news(symbol))
    prices=StockPriceHistory.objects.using("stocks").filter(symbol=symbol).order_by('date')
    dates,closes=[],[]
    for p in prices:
        dates.append(p.date.date())
        closes.append(float(p.close))
    context={
        'closes':closes,
        'dates':dates,
        'symbol':symbol,
        'last_price':prices.reverse()[0],
        'news':get_news(symbol)
    }
    return render(request, "stockviewer/stock_detail.html",context)