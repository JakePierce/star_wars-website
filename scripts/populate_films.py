#!/usr/bin/env python
import requests
import os, sys
import django


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import Film, Planet

counter = 0
response = True
while response:
    counter += 1
    counter_as_string = str(counter)
    response = requests.get('http://swapi.co/api/films/'+counter_as_string)
    print response.json()
    data = response.json()
    print data['title']

    response_dict = response.json()
    
    new_film, created = Film.objects.get_or_create(title=data['title'])

    new_film.episode_id = data['episode_id']
    new_film.opening_crawl = data['opening_crawl']
    new_film.director = data['director']
    new_film.producer = data['producer']
    new_film.release_date = data['release_date']

    #The change from urls to actual names in the database.
    #WE WANT THIS CODE NOT <<new_film.characters_url = data['characters']>>
    # response = requests.get('characters')
    # the_char = response.json().get(['name'])
    # print the_char
    # char_obj = Film.objects.get(name=the_char)
    # new_film.characters_url.add(char_obj)


    new_film.characters_url = data['characters']
    # print data['characters']

    # for planet in data['planets']:
    #     print planet
    #     response = rjequests.get(planet)
    #     print response.json()['name']
    #     print "-------------------"
    #     the_planet = response.json()['name']
    #     new_film.planets_url.add(the_planet)
    new_film.planets_url = data['planets']

    new_film.starships_url = data['starships']
    new_film.vehicles_url = data['vehicles']
    # new_film.species_url = data['species']

    print new_film

    new_film.save()
