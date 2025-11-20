from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        place_type = request.POST.get("type")
        print(f"Name: {name}, Type: {place_type}")
        return HttpResponse("Form submitted!")
    return HttpResponse("Invalid request")
