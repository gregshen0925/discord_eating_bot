import googlemaps
import json
import pprint
import time
import os
import random
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('Google_Map_API_Key')


gmaps = googlemaps.Client(key=API_KEY)

my_fields = ['name', 'rating', 'price_level', 'vicinity', 'photo']

places = []


def findRestaurant():
    randNum = random.randint(0, 59)

    if randNum < 20:
        places_results = gmaps.places_nearby(
            location='22.9988944,120.2147295', radius=2500, open_now=True, type='restaurant')
        for place in places_results['results']:
            places.append(place['place_id'])
        chosen_place_hash = places[randNum]
    if 19 < randNum < 40:
        places_results = gmaps.places_nearby(
            location='22.9988944,120.2147295', radius=2500, open_now=True, type='restaurant')
        time.sleep(2)
        places_results = gmaps.places_nearby(
            page_token=places_results['next_page_token'])
        for place in places_results['results']:
            places.append(place['place_id'])
        randNum = randNum-20
        chosen_place_hash = places[randNum]
    if 39 < randNum < 60:
        places_results = gmaps.places_nearby(
            location='22.9988944,120.2147295', radius=2500, open_now=True, type='restaurant')
        time.sleep(2)
        places_results = gmaps.places_nearby(
            page_token=places_results['next_page_token'])
        time.sleep(2)
        places_results = gmaps.places_nearby(
            page_token=places_results['next_page_token'])
        for place in places_results['results']:
            places.append(place['place_id'])
        randNum = randNum-40
        chosen_place_hash = places[randNum]
    else:
        places_results = gmaps.places_nearby(
            location='22.9988944,120.2147295', radius=2500, open_now=True, type='restaurant')
        time.sleep(2)
        places_results = gmaps.places_nearby(
            page_token=places_results['next_page_token'])
        time.sleep(2)
        places_results = gmaps.places_nearby(
            page_token=places_results['next_page_token'])
        time.sleep(2)
        places_results = gmaps.places_nearby(
            page_token=places_results['next_page_token'])
        for place in places_results['results']:
            places.append(place['place_id'])
        randNum = randNum-60
        chosen_place_hash = places[randNum]

    # print(chosen_place)

    place_details = gmaps.place(
        place_id=chosen_place_hash, fields=my_fields, language='zh-TW')

    chosen_detail = place_details['result']

    chosen_price_level = chosen_detail['price_level'] if 'price_level' in chosen_detail else "unknown"

    chosen_rating = chosen_detail['rating'] if 'rating' in chosen_detail else 0

    # photo_reference=chosen_detail['photos'][0]['photo_reference']

    # quote = "昂貴程度：%.1f \n評價：%.1f \n地址：%s" % (chosen_price_level,chosen_rating,chosen_detail['vicinity'])
    # print(a)
    # print(quote)

    URL = "https://www.google.com/maps/search/?api=1&query=Google&query_place_id=%s" % (
        chosen_place_hash)

    # imageURL='https://maps.googleapis.com/maps/api/place/photo?maxwidth=2000&photo_reference=%s'%(photo_reference)
    # print(URL)
    return chosen_detail['name'], chosen_price_level, chosen_rating, chosen_detail['vicinity'], URL
