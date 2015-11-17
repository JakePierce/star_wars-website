#!/usr/bin/env python
import requests
import os, sys
import django


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import People, Film, Species, Vehicles, Planet

callback = 0
counter = 15
response = True 
People.objects.all().delete()
while response or callback == 404:
    counter += 1
    counter_as_string = str(counter)
    response = requests.get('http://swapi.co/api/people/'+counter_as_string)
    # print response.json()
    data = response.json()
    # print data['name']

    response_dict = response.json()
    callback = response.status_code
    if callback != 404:
        new_people, created = People.objects.get_or_create(name=data['name'])

        new_people.height = data['height']
        new_people.mass = data['mass']
        new_people.hair_color = data['hair_color']
        new_people.skin_color = data['skin_color']
        new_people.eye_color = data['eye_color']
        new_people.birth_year = data['birth_year']
        new_people.gender = data['gender']

        response = requests.get(data['homeworld'])
        the_planet = response.json()['name']
        print the_planet
        planet_obj = Planet.objects.get(name=the_planet)
        new_people.homeworld.add(planet_obj)

        # print data['films']
        #data['films'] is a list of urls, so we must loop though them
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
            new_people.films.add(film_obj)

        for skin in data['species']:
            print skin

            response = requests.get(skin)
            the_name = response.json()['name']
            print the_name
            species_obj, created = Species.objects.get_or_create(name=the_name)

            new_people.species.add(species_obj)

        for cars in data['vehicles']:
            print cars

            response = requests.get(cars)
            the_vehicle = response.json()['name']
            print the_vehicle
            vehicle_obj, created = Vehicles.objects.get_or_create(name=the_vehicle)

            new_people.vehicles.add(vehicle_obj)
        # new_people.vehicles = data['vehicles']
        #new_people.starships = Starship.objects.get(name=data['starships'])
        new_people.url = data['url']

        print new_people

        new_people.save()

    elif callback == 404:
        print "This is a 404 Error"
        print "=============================" 
        print response