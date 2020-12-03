#!/bin/python
# Capitalize frequently used short form words

import requests

class CAPITALIZER:
    caches = []

    def __init__(self):
        self.caches = self.__cached_words()

    def __cached_words(self) -> []:
        csv_url = "https://raw.githubusercontent.com/anytizer/capitalizer.php/master/src/anytizer/words.csv"
        csv = requests.get(csv_url)
        words = csv.text.splitlines()
        return words

    def __capitalize(self, w=""):
        capitalized = w.title()
        for entity in self.caches:
            if w.upper() == entity:
                capitalized = entity
        return capitalized

    def capitalize(self, word=""):
        capitalized = " ".join([self.__capitalize(w) for w in word.split("_")])
        return capitalized
