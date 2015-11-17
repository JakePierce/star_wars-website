#!/usr/bin/env python
import requests
import os, sys
import django


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import Film, Planet, People

counter = 0
response = True
while response:
    counter += 1
    counter_as_string = str(counter)
    response = requests.get('http://swapi.co/api/planets/'+counter_as_string)
    print response.json()
    data = response.json()
    print data['name']

    response_dict = response.json()
    
    new_planet, created = Planet.objects.get_or_create(name=data['name'])

    new_planet.rotation_period = data['rotation_period']
    new_planet.orbital_period = data['orbital_period']
    new_planet.diameter = data['diameter']
    new_planet.climate = data['climate']
    new_planet.gravity = data['gravity']
    new_planet.terrain = data['terrain']
    new_planet.surface_water = data['surface_water']
    new_planet.population = data['population']

    for peeps in data['residents']:
        print data['residents']
        print peeps
        print " ------------ "
        response = requests.get(peeps)
        the_peeps = response.json()['name']
        print the_peeps
        peep_obj, created = People.objects.get_or_create(name=the_peeps)
        new_planet.residents.add(peep_obj)
    # new_planet.residents = data['residents']

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
            new_planet.films.add(film_obj)
    # new_planet.films = data['films']
    new_planet.url = data['url']

    print new_planet

    new_planet.save()
