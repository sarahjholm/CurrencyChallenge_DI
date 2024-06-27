from django.http import JsonResponse
from django.http import HttpResponseBadRequest

from datetime import timedelta

import datetime
import requests

from .models import *

def get_currency_rate(request, start_date = "", end_date = ""):
    
    start_date_parsed, end_date_parsed = date_parser(start_date, end_date)
    
    if (start_date_parsed > end_date_parsed):
        return HttpResponseBadRequest('Dates are invalid (start_date > end_date)')

    currency_rates, new_dates = get_currencyrates_from_db(start_date_parsed, end_date_parsed)

    print(currency_rates)
    print(new_dates)

    if len(new_dates) != 0:
        for new_date in new_dates:
            new_currency_rate = call_fankfurter_api(new_date, 'USD')
            if new_currency_rate != 0:
                currency_rates.append(new_currency_rate)

    final_rate = 0

    print(currency_rates)
    print(len(currency_rates))

    for currency_rate in currency_rates:
        final_rate = final_rate + currency_rate
    
    print(final_rate)

    if final_rate != 0:      
        final_rate = final_rate / len(currency_rates)

    final_rate_dict = {"Rate (Averaged)": final_rate, "Start Date": start_date, "End Date": end_date}

    return JsonResponse(final_rate_dict)   
    
def date_parser(start_date_str, end_date_str):

    if not start_date_str and not end_date_str:
        start_date = end_date = datetime.datetime.now()
        return start_date, end_date
    
    elif not end_date_str:
        end_date_str = start_date_str

    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
    
    return start_date, end_date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def get_currencyrates_from_db(start_date, end_date):
    
    new_dates = []
    currency_rates = []

    for date in daterange(start_date, end_date):

        currency_rate_info = CurrencyRate.objects.filter(date = date).first()
        
        if not currency_rate_info:
            new_dates.append(date)

        else:
            current_rate = currency_rate_info.value

            if current_rate != 0:
                currency_rates.append(current_rate)

    return currency_rates, new_dates

def call_fankfurter_api(date, currency):

    date_str = date.strftime("%Y-%m-%d")
    frankfurter_api_url = 'https://api.frankfurter.app/' + date_str

    try:

        params = {'to': currency}
        response = requests.get(frankfurter_api_url, params=params)

        currency_rate_complete_json = response.json()

        if date_str != currency_rate_complete_json.get("date"):
            new_currency_rate = CurrencyRate(date = date, value = 0)
            new_currency_rate.save()
            return 0

        currency_rate = save_currency_rates_db(currency_rate_complete_json, currency)

        return currency_rate
    
    except requests.exceptions.RequestException as e:

        print(f"Error: {e}")
        print("Request was not successful")

def save_currency_rates_db(currency_rate_complete_json, currency):
    
    currency_rate_complete = currency_rate_complete_json.get("rates")
    
    if not currency_rate_complete:
        return currency_rate

    currency_rate = currency_rate_complete[currency]
    date = currency_rate_complete_json.get("date")

    new_currency_rate = CurrencyRate(date = date, value = currency_rate)
    new_currency_rate.save()
    
    return currency_rate