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

    return render(request, 'view_asset.html', {
        "daily_info": json.dumps(daily_info),
        "asset": asset,
    })
    
OLLAMA_URL = "http://ollama:11434/api/generate"

def get_ai_summary(request, id):
    asset = Asset.objects.get(id=id)

    try:
        asset = Asset.objects.get(id=id)
    except Asset.DoesNotExist:
        return HttpResponse("Asset not found", status=404)

    records = list(DailyAssetInfo.objects.filter(asset_id=id).order_by('-date')[:30][::-1])

    if not records:
        return HttpResponse("No daily info found for this asset", status=404)

    prompt = (
        "You are investment advisor. Please answer very quickly and give just overall summary."
        f"Generate a summary for the asset {asset.symbol} "
        f"with the following daily prices: {', '.join(str(r.close) for r in records)} "
        f"starting at {records[0].date.strftime('%Y-%m-%d')} until {records[-1].date.strftime('%Y-%m-%d')}"
        "If available include key trends and overall sentiment. Be quick."
    )

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return JsonResponse(response.json())
    except requests.RequestException as e:
        return HttpResponse(f"Request failed: {e}", status=500)