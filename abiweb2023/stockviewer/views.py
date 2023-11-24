from django.shortcuts import render
from .models import StockPriceHistory
# Create your views here.

def list_stocks(request):
    stocks=StockPriceHistory.objects.using("stocks").all()
    symbols=list(set([stock.symbol for stock in stocks]))
    return render(request, "stockviewer/liststocks.html",{'symbols':symbols})

def stock_detail(request,symbol):
    prices=StockPriceHistory.objects.using("stocks").filter(symbol=symbol).order_by('date')
    dates,closes=[],[]
    for p in prices:
        dates.append(p.date.date())
        closes.append(float(p.close))
    context={
        'closes':closes,
        'dates':dates,
        'symbol':symbol,
        'last_price':prices.reverse()[0]
    }
    return render(request, "stockviewer/stock_detail.html",context)