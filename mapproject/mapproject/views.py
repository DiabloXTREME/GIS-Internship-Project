from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        place_type = request.POST.get("type")
        lat = request.POST.get("latitude")
        lon = request.POST.get("longitude")
        print(f"Name: {name}, Type: {place_type}")
        # return HttpResponse(f"{name}, {place_type}, {lat}, {lon}")
    else:
        return render(request, 'index.html')


