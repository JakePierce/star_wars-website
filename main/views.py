from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, JsonResponse
from main.forms import PeopleEditForm, PlanetEditForm, StarshipEditForm, VehicleEditForm, SpeciesEditForm

from main.models import Film, People, Planet, Starship, Species, Vehicles

# from main.models import CustomUser
# from main.forms import UserSignUp, UserLogin

# from django.contrib.auth import authenticate, login, logout
# from django.db import IntegrityError


def json_response(request):
    search_string = request.GET.get('search', '')

    objects = Film.objects.filter(title__icontains=search_string)

    object_list = []

    for obj in objects:
        object_list.append(obj.title)

    return JsonResponse(object_list, safe=False)

#Here are the extra views:
# ----------------------------


def ajax_search(request):
    context = {}

    return render_to_response('ajax_search.html', context, context_instance=RequestContext(request))


def home_view(request):

    context = {}

    return render_to_response('home_view.html', context, context_instance=RequestContext(request))


def universe_view(request):

    context = {}

    return render_to_response('universe_view.html', context, context_instance=RequestContext(request))


def forceawakens_view(request):

    context = {}

    return render_to_response('forceawakens_view.html', context, context_instance=RequestContext(request))


def games_view(request):

    context = {}
    
    return render_to_response('games_view.html', context, context_instance=RequestContext(request))

# Here are all the film views:
# ----------------------------


def film_list(request):

    film = Film.objects.all()

    context = {}

    context['film'] = film

    return render_to_response('film_list.html', context, context_instance=RequestContext(request))


def film_detail(request, pk):

    film = Film.objects.get(pk=pk)

    context = {}

    context['film'] = film

    return render_to_response('film_detail.html', context, context_instance=RequestContext(request))

# Here are the people/character views:
# ----------------------------


def people_list(request):

    people = People.objects.all()

    context = {}

    context['people'] = people

    return render_to_response('people_list.html', context, context_instance=RequestContext(request))


def people_detail(request, pk):

    people = People.objects.get(pk=pk)

    context = {}

    context['people'] = people

    return render_to_response('people_detail.html', context, context_instance=RequestContext(request))


def people_create(request):

    context = {}

    context['request'] = request.method

    context['people'] = People.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        height = request.GET.get('height', None)
        mass = request.GET.get('mass', None)
        hair_color = request.GET.get('hair_color', None)
        skin_color = request.GET.get('skin_color', None)
        eye_color = request.GET.get('eye_color', None)
        birth_year = request.GET.get('birth_year', None)
        gender = request.GET.get('gender', None)
        homeworld = request.GET.get('homeworld', None)
        species = request.GET.get('species', None)

        the_person, created = People.objects.get_or_create(name=name)

        the_person.save()

        context['created'] = created

    elif request.method == 'GET':
            print "It was a GET request"

    return render_to_response('people_create.html', context, context_instance=RequestContext(request))


def people_edit(request, pk):

    context = {}

    people = People.objects.get(pk=pk)

    form = PeopleEditForm(request.POST or None, instance=people)

    context['People'] = people
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/people_list/')

    return render_to_response('people_edit.html', context, context_instance=RequestContext(request))


# Here are the starship views:
# ----------------------------


def starship_list(request):

    starships = Starship.objects.all()

    context = {}

    context['starships'] = starships

    return render_to_response('starship_list.html', context, context_instance=RequestContext(request))


def starship_detail(request, pk):

    starship = Starship.objects.get(pk=pk)

    context = {}

    context['starship'] = starship

    return render_to_response('starship_detail.html', context, context_instance=RequestContext(request))


def starship_create(request):

    context = {}

    context['request'] = request.method

    context['starship'] = Starship.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        model = request.GET.get('model', None)
        manufacturer = request.GET.get('manufacturer', None)
        cost_in_credits = request.GET.get('cost_in_credits', None)
        length = request.GET.get('length', None)
        max_atmosphering_speed = request.GET.get('max_atmosphering_speed', None)
        crew = request.GET.get('crew', None)
        passengers = request.GET.get('passengers', None)
        cargo_capacity = request.GET.get('cargo_capacity', None)
        consumables = request.GET.get('consumables', None)
        hyperdrive_rating = request.GET.get('hyperdrive_rating', None)
        MGLT = request.GET.get('MGLT', None)
        starship_class = request.GET.get('starship_class', None)
        pilots = request.GET.get('pilots', None)

        the_starship, created = Starship.objects.get_or_create(name=name)

        the_starship.save()

        context['created'] = created

    elif request.method == 'GET':
            print "It was a GET request"

    return render_to_response('starship_create.html', context, context_instance=RequestContext(request))


def starship_edit(request, pk):

    context = {}

    starship = Starship.objects.get(pk=pk)

    form = StarshipEditForm(request.POST or None, instance=starship)

    context['Starship'] = starship
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/starship_list/')

    return render_to_response('starship_edit.html', context, context_instance=RequestContext(request))
# Here are the planet views:
# ----------------------------


def planet_list(request):

    planet = Planet.objects.all()

    context = {}

    context['planet'] = planet

    return render_to_response('planet_list.html', context, context_instance=RequestContext(request))


def planet_detail(request, pk):

    planet = Planet.objects.get(pk=pk)

    context = {}

    context['planet'] = planet

    return render_to_response('planet_detail.html', context, context_instance=RequestContext(request))


def planet_create(request):

    context = {}

    context['request'] = request.method

    context['planet'] = Planet.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        rotation_period = request.GET.get('rotation_period', None)
        orbital_period = request.GET.get('orbital_period', None)
        diameter = request.GET.get('diameter', None)
        climate = request.GET.get('climate', None)
        gravity = request.GET.get('gravity', None)
        terrain = request.GET.get('terrain', None)
        surface_water = request.GET.get('surface_water', None)
        population = request.GET.get('population', None)

        the_planet, created = Planet.objects.get_or_create(name=name)

        the_planet.save()

        context['created'] = created

    elif request.method == 'GET':
            print "It was a GET request"

    return render_to_response('planet_create.html', context, context_instance=RequestContext(request))


def planet_edit(request, pk):

    context = {}

    planet = Planet.objects.get(pk=pk)

    form = PlanetEditForm(request.POST or None, instance=planet)

    context['Planet'] = planet
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/planet_list/')

    return render_to_response('planet_edit.html', context, context_instance=RequestContext(request))

# Here are the vehicle views:
# ----------------------------


def vehicle_list(request):

    vehicles = Vehicles.objects.all()

    context = {}

    context['vehicles'] = vehicles

    return render_to_response('vehicle_list.html', context, context_instance=RequestContext(request))


def vehicle_detail(request, pk):

    vehicle = Vehicles.objects.get(pk=pk)

    context = {}

    context['vehicle'] = vehicle

    return render_to_response('vehicle_detail.html', context, context_instance=RequestContext(request))


def vehicle_create(request):

    context = {}

    context['request'] = request.method

    context['vehicle'] = Vehicles.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        model = request.GET.get('model', None)
        manufacturer = request.GET.get('manufacturer', None)
        cost_in_credits = request.GET.get('cost_in_credits', None)
        length = request.GET.get('length', None)
        max_atmosphering_speed = request.GET.get('max_atmosphering_speed', None)
        crew = request.GET.get('crew', None)
        passengers = request.GET.get('passengers', None)
        cargo_capacity = request.GET.get('cargo_capacity', None)
        consumables = request.GET.get('consumables', None)
        vehicle_class = request.GET.get('vehicle_class', None)
        pilots = request.GET.get('pilots', None)

        the_vehicle, created = Vehicles.objects.get_or_create(name=name)

        the_vehicle.save()

        context['created'] = created

    elif request.method == 'GET':
            print "It was a GET request"

    return render_to_response('vehicle_create.html', context, context_instance=RequestContext(request))


def vehicle_edit(request, pk):

    context = {}

    vehicle = Vehicles.objects.get(pk=pk)

    form = VehicleEditForm(request.POST or None, instance=vehicle)

    context['Vehicle'] = vehicle
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/vehicle_list/')

    return render_to_response('vehicle_edit.html', context, context_instance=RequestContext(request))


# Here are the species views:
# ----------------------------


def species_list(request):

    species = Species.objects.all()

    context = {}

    context['species'] = species

    return render_to_response('species_list.html', context, context_instance=RequestContext(request))


def species_detail(request, pk):

    species = Species.objects.get(pk=pk)

    context = {}

    context['species'] = species

    return render_to_response('species_detail.html', context, context_instance=RequestContext(request))


def species_create(request):

    context = {}

    context['request'] = request.method

    context['species'] = Species.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        classification = request.GET.get('classification', None)
        designation = request.GET.get('designation', None)
        average_height = request.GET.get('average_height', None)
        skin_colors = request.GET.get('skin_colors', None)
        hair_colors = request.GET.get('hair_colors', None)
        eye_colors = request.GET.get('eye_colors', None)
        average_lifespan = request.GET.get('average_lifespan', None)
        homeworld = request.GET.get('homeworld', None)
        language = request.GET.get('language', None)

        the_species, created = Species.objects.get_or_create(name=name)

        the_species.save()

        context['created'] = created

    elif request.method == 'GET':
            print "It was a GET request"

    return render_to_response('species_create.html', context, context_instance=RequestContext(request))


def species_edit(request, pk):

    context = {}

    species = Species.objects.get(pk=pk)

    form = SpeciesEditForm(request.POST or None, instance=species)

    context['Species'] = species
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/species_list/')

    return render_to_response('species_edit.html', context, context_instance=RequestContext(request))

# Here are the extra signup views:
# ----------------------------


# def signup(request):

    # context = {}

    # form = UserSignUp()

    # context['form'] = form

    # if request.method == 'POST':

    #     form = UserSignUp(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']

    #         try:
    #             new_user = CustomUser.objects.create_user(email, password)

    #             auth_user = authenticate(email=email, password=password)

    #             login(request, auth_user)

    #             return HttpResponseRedirect('/')

    #         except IntegrityError, e:
    #             context['valid'] = "A User With That Name Already Exists"

    #     else:
    #         context['valid'] = form.errors

    # return render_to_response('signup.html', context, context_instance=RequestContext(request))

# Here are the compressed login and logout views:
# ----------------------------


# def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/')


# def login_view(request):

    # context = {}

    # context['form'] = form

    # if request.method == 'POST':
    #     form = UserLogin(request.POST)
    #     if form.is_valid():
    #         print "form is valid"

    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']

    #         auth_user = authenticate(email=email, password=password)

    #         if auth_user is not None:
    #             login(request, auth_user)

    #             print "auth_user is not None"

    #             return HttpResponseRedirect('/')
    #         else:
    #             context['valid'] = "Invalid User"

    #     else:
    #         context['valid'] = "Please enter a User Name"

    # return render_to_response('login.html', context, context_instance=RequestContext(request))
  







