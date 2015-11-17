#!/usr/bin/env python
import requests
import os, sys
import django


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import Film, Starship

counter = 1
response = True
while True:
    counter += 1
    counter_as_string = str(counter)
    response = requests.get('http://swapi.co/api/starships/'+counter_as_string)
    print response.json()
    data = response.json()
    print response

    callback = response.status_code
    
    if callback != 404:
        print "awvewvnwoen"

        response_dict = response.json()
       
        new_starship, created = Starship.objects.get_or_create(name=data['name'])

        print data

        new_starship.model = data['model']
        new_starship.manufacturer = data['manufacturer']
        new_starship.cost_in_credits = data['cost_in_credits']
        new_starship.length = data['length']
        new_starship.max_atmosphering_speed = data['max_atmosphering_speed']
        new_starship.crew = data['crew']
        new_starship.passengers = data['passengers']
        new_starship.cargo_capacity = data['cargo_capacity']
        new_starship.consumables = data['consumables']
        new_starship.hyperdrive_rating = data['hyperdrive_rating']
        new_starship.MGLT = data['MGLT']
        new_starship.starship_class = data['starship_class']

        for starstuff in data['pilots']:
            if starstuff != "Chewbacca":
                response = requests.get(starstuff)
                the_stuff = response.json()['name']
                star_obj, created = Starship.objects.get_or_create(name=the_stuff)
                new_starship.pilots.add(star_obj)

        # new_starship.pilots = data['pilots']
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
            new_starship.films.add(film_obj)

        # new_starship.films = data['films']
        new_starship.url = data['url']

        print new_starship

        new_starship.save()

    elif callback == 404:
        
        print "=============================" 
    
       
