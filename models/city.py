#!/usr/bin/python3
""" Class Place """

from models.base_model import BaseModel


class City(BaseModel):
    """ Public fetures of Place """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
