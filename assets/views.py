from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests

# Create your views here.
def test(request):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=P50DH8XQ9SKA2ANB'
    r = requests.get(url)
    data = r.json()

    return JsonResponse(data)

    # return render(request, 'test.html', {
    #     'name': data
    # })