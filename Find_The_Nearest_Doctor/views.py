
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
from django.shortcuts import render
Error_validity = {'Error': 'You are not authorized to enter here'}

@csrf_exempt
@csrf_protect
@login_required(login_url='login')
def t(request):
    if request.method == "POST": # NEW
        doctors = []
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        parameters = {
            "location": "30.0778,31.2852",
            "rankby": "distance",
            "type": "doctor",
            "keyword": "طبيب باطنة",
            "key": "AIzaSyCs5_KOaxD6-ZJiaJwA67wBq25zZ08o3QE"
        }
        response = requests.get(url, params=parameters)
        data_dict = response.json()
        # Append the doctors to the list
        for item in data_dict["results"]:
            name = item.get("name", "No name")
            place_id = item.get("place_id", "No place ID")
            vicinity = item.get("vicinity", "No vicinity")
            rating = item.get("rating", "No rating")
            open_now = item.get("opening_hours", {}).get("open_now", "Unknown")

            doctors.append({
                "name": name,
                "place_id": place_id,
                "vicinity": vicinity,
                "rating": rating,
                "open_now": open_now
            })
        print(doctors)
        return JsonResponse(doctors, safe=False)
    return JsonResponse(Error_validity, safe=False) # NEW 
@csrf_exempt
@csrf_protect
@login_required(login_url='login')
def t(request):
    if request.method == "POST":  # NEW
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        doctors = []
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        parameters = {
            "location": f"{latitude},{longitude}",
            "rankby": "distance",
            "type": "doctor",
            "keyword": "طبيب باطنة",
            "key": "AIzaSyCs5_KOaxD6-ZJiaJwA67wBq25zZ08o3QE"
        }
        response = requests.get(url, params=parameters)
        data_dict = response.json()
        # Append the doctors to the list
        for item in data_dict["results"]:
            name = item.get("name", "No name")
            place_id = item.get("place_id", "No place ID")
            vicinity = item.get("vicinity", "No vicinity")
            rating = item.get("rating", "No rating")
            open_now = item.get("opening_hours", {}).get("open_now", "Unknown")

            doctors.append({
                "name": name,
                "place_id": place_id,
                "vicinity": vicinity,
                "rating": rating,
                "open_now": open_now
            })
        print(doctors)
        return JsonResponse(doctors, safe=False)
    return JsonResponse(Error_validity, safe=False)  # NEW



def one(request):
    context={}
    if request.method == 'POST':
        latitude = request.POST.get('latitude') 
        longitude = request.POST.get('longitude')
        context ={'latitude':latitude,'longitude':longitude }

    return render(request, 'Nearst doctor/diseases.html',context)
@login_required(login_url='login')
def two(request):
    doctors = [
    ]
    if request.method == 'POST':
        latitude = request.POST.get('latitude') 
        longitude = request.POST.get('longitude')
        print("ggggggggggggger")
        print(longitude)
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        parameters = {
            "location": f"{latitude},{longitude}",
            "rankby": "distance",
            "type": "doctor",
            "keyword": "طبيب باطنة",
            "key": "AIzaSyCs5_KOaxD6-ZJiaJwA67wBq25zZ08o3QE"
        } 
        response = requests.get(url, params=parameters) 
        data_dict = response.json()
            # Append the doctors to the list
        for item in data_dict["results"]:
         name = item.get("name", "No name")
         place_id = item.get("place_id", "No place ID")
         vicinity = item.get("vicinity", "No vicinity")
         rating = item.get("rating", "No rating")
         open_now = item.get("opening_hours", {}).get("open_now", "Unknown")
         latitude = item.get("geometry", {}).get("location", {}).get("lat", "No latitude")
         longitude = item.get("geometry", {}).get("location", {}).get("lng", "No longitude")

         doctors.append({
            "name": name,
            "place_id": place_id,
            "vicinity": vicinity,
            "rating": rating,
            "open_now": open_now,
            "latitude":latitude,
            "longitude":longitude,
        })
        
    print(doctors)
    context = {"doctors": doctors} 
    # print(context)
    return render(request, 'Nearst doctor/doctorLocation.html', context)
