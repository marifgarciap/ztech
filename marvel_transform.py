import pandas as pd


class MarvelTransform:

    @staticmethod
    def getCharactersDataframe(characters_dict):
            df = pd.json_normalize(characters_dict)
            df = df[["id", "name", "description", "comics.available", "series.available", "stories.available",
                               "events.available"]]
            df = df.rename(columns={"comics.available": "comics", "series.available": "series", "stories.available": "stories",
                         "events.available": "events"})
            return df


