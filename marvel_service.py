import urllib.request
import urllib.parse
import json
import hashlib


class MarvelService:

    def __init__(self, private_key, public_key, ts):
        self.private_key = private_key
        self.public_key = public_key
        self.ts = ts
        self.hash = hashlib.md5(f'{ts}{private_key}{public_key}'.encode('utf-8')).hexdigest()

    def getCharacters(self, limit=100, offset=0):
        url = f'http://gateway.marvel.com/v1/public/characters?apikey={self.public_key}&ts={self.ts}&hash={self.hash}&limit={limit}&offset={offset}'
        response = urllib.request.urlopen(url)
        parsed_response = json.loads(response.read().decode('utf-8'))
        return parsed_response

    def getAllCharacters(self):
        limit = 100
        offset = 0
        characters_list = []
        while True:
            response = self.getCharacters(limit, offset)
            if response['data']['count'] == 0:
                break
            characters_list = characters_list + response['data']['results']
            offset += limit
        return characters_list
