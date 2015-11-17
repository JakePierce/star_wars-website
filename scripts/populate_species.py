#!/usr/bin/env python
import requests
import os, sys
import django

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import Film, Species

counter = 2
response = True
while True:
    counter += 1
    counter_as_string = str(counter)
    response = requests.get('http://swapi.co/api/species/'+counter_as_string)
    print response.json()
    data = response.json()
    print data['name']

    language = data['language']
    skin_colors = data['skin_colors']
    hair_colors = data['hair_colors']
    eye_colors = data['eye_colors']
    average_height = data['average_height']
    average_lifespan = data['average_lifespan']

    callback = response.status_code

    if callback != 404:

        response_dict = response.json()

        new_species, created = Species.objects.get_or_create(name=data['name'])

        new_species.classification = data['classification']
        new_species.designation = data['designation']

        #The statement to run over the Value Errors

        print average_height
        if average_height == 'n/a':
            print 'true true true'
            average_height = 0
            print average_height

        new_species.average_height = data['average_height']
        #These are the color statements to run over the Value Errors

        print skin_colors
        if skin_colors == 'n/a':
            print 'true true true'
            skin_colors = 'unavailable'
            print skin_colors
        
        new_species.skin_colors = skin_colors

        print hair_colors
        if hair_colors == 'n/a':
            print 'true true true'
            hair_colors = 'unavailable'
            print hair_colors

        new_species.hair_colors = hair_colors

        print eye_colors
        if eye_colors == 'n/a':
            print 'true true true'
            eye_colors = 'unavailable'
            print eye_colors

        new_species.eye_colors = eye_colors

        print average_lifespan
        if average_lifespan == 'n/a':
            print 'average life span -- true true true'
            average_lifespan = 'unavailable'
            print average_lifespan
        new_species.average_lifespan = data['average_lifespan']

        new_species.homeworld = data['homeworld']

        print language
        if language == 'n/a':
            print 'language true true true'
            language = 'unavailable'
            print language

        new_species.language = data['language']

        for peeps in data['people']:
            print "------"
            print data['people']
            print "------"
            response = requests.get(peeps)
            the_peeps = response.json()['name']
            print the_peeps
            spec_obj, created = Species.objects.get_or_create(name=the_peeps)
            new_species.people.add(spec_obj)
        # new_species.people = data['people']
        # new_species.films = data['films']
        new_species.url = data['url']

        print new_species
        new_species.save()

    elif callback == 404:
        print "This is a 404 Error"
        print "=============================" 
