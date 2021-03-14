#!/usr/bin/env python3
__author__ = 'Michal Pielaszkiewicz (@yautay)'
__date__ = '20210311'
__version__ = '1.0'
__description__ = """Generates dates patterns."""

import itertools
from datetime import date, timedelta


class BirthdayGenerator:
    def __init__(self, first_year: int, last_year: int):
        self.first_year = first_year
        self.last_year = last_year

    def generate_calendar(self):
        delta = timedelta(days=1)
        date_min = date(self.first_year, 1, 1)
        date_max = date(self.last_year, 12, 31)
        element = {}
        while date_min <= date_max:
            _date = self.extract_y_m_d_from_date(date_min.isoformat())
            _dict_minor = self.serialize_d_m_y(_date)
            _dict_major = self.format_dates(_dict_minor)
            combinations = self.combinator(_dict_major)
            combinations = self.clean_list(combinations)
            dates = self.format_to_string(combinations)
            dates = self.clean_list(dates)
            # TODO zapis do strumienia oraz pliku
            print(dates)
            date_min += delta
        return element

    @staticmethod
    def serialize_d_m_y(_date: list):
        element = {}
        year = _date[0]
        month = _date[1]
        day = _date[2]
        element["y"] = year
        element["m"] = month
        element["d"] = day
        return element

    @staticmethod
    def extract_y_m_d_from_date(_date: str):
        array = _date.split("-")
        return array

    @staticmethod
    def format_dates(day: dict):
        y4 = str(day["y"])
        m2 = str(day["m"])
        d2 = str(day["d"])
        y2 = y4[-2:]
        m1 = str(int(m2))
        d1 = str(int(d2))
        element = {
            "y4": y4,
            "y2": y2,
            "m2": m2,
            "m1": m1,
            "d2": d2,
            "d1": d1
        }
        return element

    @staticmethod
    def combinator(_dict_major: dict):
        def permutator(array_of_elements):
            permutations = itertools.permutations(array_of_elements, len(array_of_elements))
            return permutations

        def wariator(array_of_elements):
            variations = []
            for year in array_of_elements[0]:
                for month in array_of_elements[1]:
                    for day in array_of_elements[2]:
                        variations.append([year, month, day])
            return variations
        m1 = _dict_major["m1"]
        y4 = _dict_major["y4"]
        y2 = _dict_major["y2"]
        m2 = _dict_major["m2"]
        d2 = _dict_major["d2"]
        d1 = _dict_major["d1"]
        variations = wariator([[y4, y2], [m2, m1], [d2, d1]])
        permutations = []
        for variation in variations:
            permutations.append(list(permutator(variation)))
        return permutations

    @staticmethod
    def clean_list(array: list):
        cleaned_elements = []
        for variation in array:
            for element in variation:
                cleaned_elements.append(element)
        return cleaned_elements

    @staticmethod
    def format_to_string(array: list):
        out = []
        out_w_delimiter = []
        for element in array:
            day = "{}{}{}".format(element[0], element[1], element[2])
            day_w_delimiter = "{}{}{}{}{}".format(element[0], "-", element[1], "-", element[2])
            out.append(day)
            out_w_delimiter.append(day_w_delimiter)
        result = [out, out_w_delimiter]
        return result


app = BirthdayGenerator(1982, 1983)
app.generate_calendar()
