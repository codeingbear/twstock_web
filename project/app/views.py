from django.shortcuts import render
from django.http import HttpResponse
import twstock
def main(request):
    return render(request,'main.html')
def num(request,stock_num):
    if(stock_num<1000):
        stock_num=f"{stock_num:04d}"
    try:
        twstock.codes(stock_num)
        return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>num</title></head><body>{0}</body></html>'.format(twstock.Stock(stock_num).fetch(2024,5)))
    except:
        return render(request,'baka.html')
def name(request,stock_name):
    for name in list(list(twstock.codes.items())):
        if(stock_name==name[1][2]):
            return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>num</title></head><body>{0}</body></html>'.format(twstock.Stock(name[1][1]).fetch(2024,5)))
    return render(request,'baka.html')