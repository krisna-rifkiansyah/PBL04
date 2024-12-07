import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

API_URL = 'http://localhost:8001/api/cars/'


def index(request):
    query = request.GET.get('q', '')
    if query:
        response = requests.get(f"{API_URL}?search={query}")
    else:
        response = requests.get(API_URL)

    if response.status_code == 200:
        cars = response.json()
    else:
        cars = []
        print("Error:", response.status_code)
    
    return render(request, 'index.html', {'cars': cars, 'query': query})

def add_car(request):
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'brand': request.POST['brand'],
            'model': request.POST['model'],
            'price': request.POST['price']
        }
        requests.post(API_URL, data=data)
        return redirect('index')
    return render(request, 'add_car.html')

def edit_car(request, car_id):
    response = requests.get(f"{API_URL}{car_id}/")
    if response.status_code == 200:
        car = response.json()
    else:
        car = None
        print("Error: Car not found or server error")

    if request.method == 'POST':
        updated_data = {
            'name': request.POST['name'],
            'brand': request.POST['brand'],
            'model': request.POST['model'],
            'price': request.POST['price']
        }
        response = requests.put(f"{API_URL}{car_id}/", json=updated_data)
        if response.status_code == 200:
            return redirect('index')
        else:
            print("Error updating car:", response.status_code)

    return render(request, 'edit_car.html', {'car': car})

def delete_car(request, car_id):
    requests.delete(f"{API_URL}{car_id}/")
    return redirect('index')
