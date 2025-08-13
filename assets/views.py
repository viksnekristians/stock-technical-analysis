from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from assets.models import DailyAssetInfo, Asset
import json
import requests

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

    records = DailyAssetInfo.objects.filter(asset_id=id).order_by('date')

    for record in records:
        daily_info["dates"].append(record.date.strftime('%Y-%m-%d'))
        daily_info["prices"].append(float(record.close))

    return render(request, 'view_asset.html', {"daily_info": json.dumps(daily_info)})
    
OLLAMA_URL = "http://ollama:11434/api/generate"

def get_ai_summary(request, id):
    payload = {
        "model": "llama3",
        "prompt": "hello, answer shortly and quickly",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return JsonResponse(response.json())
    except requests.RequestException as e:
        return HttpResponse(f"Request failed: {e}", status=500)