from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from assets.Services.API.Alphavantage.alphavantage_api_client import AlphavantageApiClient
from assets.models import DailyAssetInfo, Asset
from datetime import datetime
import json
from django.core.serializers import serialize
from django.forms.models import model_to_dict

# Create your views here.
def asset_info(request, id):
    try:
        asset = Asset.objects.get(id=id)
    except Asset.DoesNotExist:
        return render(request, '404.html')

    daily_info = {
        "dates": [],
        "prices": []
    }

    #nodefinet periodu opcijas
    records = DailyAssetInfo.objects.filter(asset_id=id).order_by('date')
    
    # priekš moving average varbut vajag iepriekšējos x (x=window size) recordus?
    # vai ari uzreiz dabut un sakt no konkreta records seta indeksa veidojot atgrieztos datus

    for record in records:
        daily_info["dates"].append(record.date.strftime('%Y-%m-%d'))
        daily_info["prices"].append(float(record.close))

    return render(request, 'view_asset.html', {"daily_info": json.dumps(daily_info)})