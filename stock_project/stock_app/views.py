# stockviewer/views.py

from django.shortcuts import render
from django.http import JsonResponse
from yahoo_fin import stock_info
from .models import StockData
import json

def get_stock_data(request, symbol):
    data = stock_info.get_quote_table(symbol)
    stock_data = StockData.objects.create(
        symbol=symbol,
        date=data['date'],
        open_price=data['open'],
        high_price=data['day_high'],
        low_price=data['day_low'],
        close_price=data['previous_close'],
        volume=data['volume']
    )
    stock_data.save()

    response_data = {
        'symbol': symbol,
        'date': data['date'],
        'open': data['open'],
        'high': data['day_high'],
        'low': data['day_low'],
        'close': data['previous_close'],
        'volume': data['volume']
    }

    return JsonResponse(response_data)
