from django.shortcuts import render

# Create your views here.
# APİ KEY =
#! xv9l+rH5KzlcLe0d/UnEpQ==NUWHR6xa53qRLkpV
# Fonksiyonu oluştur


def home(request):
    import requests
    import json

    if request.method == "POST":
        query = request.POST["query"]
        api_url = "https://api.api-ninjas.com/v1/nutrition?query="
        api_request = requests.get(
            api_url + query,
            headers={"X-Api-Key": "xv9l+rH5KzlcLe0d/UnEpQ==NUWHR6xa53qRLkpV"},
        )
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops, something went wrong ERROR"
            print(e)
        return render(request, "home.html", {"api": api})
    else:
        return render(request, "home.html", {"query": "Enter a valid Query"})
