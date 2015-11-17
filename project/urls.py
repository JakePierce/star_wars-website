"""starwars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [

    #Json Response
    url(r'^json_response/$', 'main.views.json_response'),
    url(r'^ajax_search/$', 'main.views.ajax_search'),


    #Admin Views
    url(r'^admin/', include(admin.site.urls)),

    # Bonus Views
    url(r'^universe_view/$', 'main.views.universe_view'),
    url(r'^forceawakens_view/$', 'main.views.forceawakens_view'),
    url(r'^games_view/$', 'main.views.games_view'),
    url(r'^home_view/$', 'main.views.home_view'),
    
    # Film Views
    url(r'^film_list/$', 'main.views.film_list'),
    url(r'^film_detail/(?P<pk>\d+)/$', 'main.views.film_detail'),

    # People Views
    url(r'^people_list/$', 'main.views.people_list'),
    url(r'^people_detail/(?P<pk>\d+)/$', 'main.views.people_detail'),
    url(r'^people_create/$', 'main.views.people_create'),
    url(r'^people_edit/(?P<pk>\d+)/$', 'main.views.people_edit'),

    # Starship Views
    url(r'^starship_list/$', 'main.views.starship_list'),
    url(r'^starship_detail/(?P<pk>\d+)/$', 'main.views.starship_detail'),
    url(r'^starship_create/$', 'main.views.starship_create'),
    url(r'^starship_edit/(?P<pk>\d+)/$', 'main.views.starship_edit'),

    # Planet Views
    url(r'^planet_list/$', 'main.views.planet_list'),
    url(r'^planet_detail/(?P<pk>\d+)/$', 'main.views.planet_detail'),
    url(r'^planet_create/$', 'main.views.planet_create'),
    url(r'^planet_edit/(?P<pk>\d+)/$', 'main.views.planet_edit'),

    # Vehicle Views
    url(r'^vehicle_list/$', 'main.views.vehicle_list'),
    url(r'^vehicle_detail/(?P<pk>\d+)/$', 'main.views.vehicle_detail'),
    url(r'^vehicle_create/$', 'main.views.vehicle_create'),
    url(r'^vehicle_edit/(?P<pk>\d+)/$', 'main.views.vehicle_edit'),

    # Species Views
    url(r'^species_list/$', 'main.views.species_list'),
    url(r'^species_detail/(?P<pk>\d+)/$', 'main.views.species_detail'),
    url(r'^species_create/$', 'main.views.species_create'),
    url(r'^species_edit(?P<pk>\d+)/$', 'main.views.species_edit'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


