#!/usr/bin/env python
import requests
import os, sys
import django


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import Film, Vehicles

counter = 0
response = True
while True:
    counter += 1
    counter_as_string = str(counter)
    response = requests.get('http://swapi.co/api/vehicles/'+counter_as_string)
    print response.json()
    data = response.json()

    callback = response.status_code

    if callback != 404:
        cost_in_credits = data['cost_in_credits']
        cargo_capacity = data['cargo_capacity']
        consumables = data['consumables']
        manufacturer = data['manufacturer']
        length = data['length']
        max_atmosphering_speed = data['max_atmosphering_speed']
        passengers = data['passengers']

        response_dict = response.json()
    
        new_vehicles, created = Vehicles.objects.get_or_create(name=data['name'])

        new_vehicles.model = data['model']

        if manufacturer == 'unknown':
            print 'true true true'
            manufacturer = 0

        new_vehicles.manufacturer = manufacturer

        if cost_in_credits == 'unknown':
            print 'true true true'
            cost_in_credits = 0

        new_vehicles.cost_in_credits = cost_in_credits

        if length == 'unknown':
            print 'true true true'
            length = 0      

        new_vehicles.length = data['length']

        if max_atmosphering_speed == 'unknown':
            print 'true true true'
            max_atmosphering_speed = 0

        new_vehicles.max_atmosphering_speed = data['max_atmosphering_speed']
        new_vehicles.crew = data['crew']

        if passengers == 'unknown':
            passengers = 0

        new_vehicles.passengers = passengers

        if cargo_capacity == 'none':
            print 'true true true'
            cargo_capacity = 0        

        if cargo_capacity == 'unknown':
            print 'true true true'
            cargo_capacity = 0

        new_vehicles.cargo_capacity = cargo_capacity

        new_vehicles.consumables = consumables
        new_vehicles.vehicle_class = data['vehicle_class']
        for starstuff in data['pilots']:
            if starstuff != "Chewbacca":
                response = requests.get(starstuff)
                the_stuff = response.json()['name']
                veh_obj, created = Vehicles.objects.get_or_create(name=the_stuff)
                new_vehicles.pilots.add(veh_obj)
        # new_vehicles.pilots = data['pilots']

        for film in data['films']:
            print film
            #each url is a url endpoint for the starwars api, so we need to query it with requests <REQUEST>
            response = requests.get(film)
            #here we are getting the value of the title from the API's response <FILTER>
            the_film = response.json()['title']
            #here we are finding an existing film object that has a title matching the one <LOOK UP>
            #that the API just returned
            film_obj = Film.objects.get(title=the_film)
            #here we are pairing the People object with the Film object retreived on line 46 <PAIR>
            new_vehicles.films.add(film_obj)
        print new_vehicles

        new_vehicles.save()
    
    elif callback == 404:

        print "============================="
               
        