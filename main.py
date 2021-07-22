from marvel_transform import MarvelTransform
from marvel_service import MarvelService
import json


config = json.load(open('./marvel_keys.config.json'))
ms = MarvelService(config["api_request"]["private_key"], config["api_request"]["public_key"], config["api_request"]["ts"])
characters = ms.getAllCharacters()
df = MarvelTransform.getCharactersDataframe(characters)
print(df.head(10))
print(len(df.index))