# Author: Michael Morriss
# Date: 1/6/2021
# Description: File that creates Person class objects based on their names and ages,
# includes a basic_stats function that returns a tuple containing the mean, median, and mode of a list containing
# multiple Person objects.

from statistics import mean, median, mode


class Person:
    """
    Class that creates a Person and records both name and age.
    """

    def __init__(self, name, age):
        """
        Creates new Person with name and age.
        """
        self._name = name
        self._age = age

    def get_age(self):
        """
        Returns the age of a specified Person.
        """
        return self._age


def basic_stats(people_list):
    """
    Function that takes an ordered list of Person object ages, and returns a tuple
    containing the mean, median, and mode of this age list, in that order.
    """
    age_list = [person.get_age() for person in people_list]  # iterates through list to get age for each element.
    age_mean = mean(age_list)
    age_median = median(age_list)
    age_mode = mode(age_list)
    result = (age_mean, age_median, age_mode)
    return result
