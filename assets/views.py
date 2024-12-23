from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from assets.Services.API.Alphavantage.alphavantage_api_client import AlphavantageApiClient
from assets.models import DailyAssetInfo
from datetime import datetime

# Create your views here.
def test(request):
    return HttpResponse('test')