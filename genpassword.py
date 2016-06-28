#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  genpassword.py [options] <wordcount> <digitcount>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 24 Jun 2016 / 17:18
where   : Latitude: 51.957128
          longitude: 4.569670
          https://www.google.nl/maps/place/51.957128,4.569670
"""
import sys
import string
import itertools
import random

from arguments import Arguments
from consoleprinter import console

if sys.version_info.major < 3:
    console("Python 3 is required", color="red", plaintext="True")
    exit(1)


def gibberish(wordcount, vowels='aeiou'):
    """
    @type wordcount: int
    @type vowels: str, unicode
    """
    initial_consonants = (set(string.ascii_lowercase) - set('aeiou') - set('qxc') | {'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'str', 'sw', 'tr'})
    final_consonants = (set(string.ascii_lowercase) - set('aeiou') - set('qxcsj') | {'ct', 'ft', 'mp', 'nd', 'ng', 'nk', 'nt', 'pt', 'sk', 'sp', 'ss', 'st'})


    # each syllable is consonant-vowel-consonant "pronounceable"
    syllables = set(map(''.join, itertools.product(initial_consonants, vowels, final_consonants)))

    # you could throw in number_of_paths_to_generate combinations, maybe capitalized versions...
    return random.sample(syllables, wordcount)



def get_pronounceable_password(wordcount=3, digitcount=2):
    """
    @type wordcount: int
    @type digitcount: int
    """
    numbermax = 10 ** digitcount
    password = '-'.join(gibberish(wordcount))

    if digitcount >= 1:
        r = int(random.random() * numbermax)

        password += "-" + str(r)
    passwordl = list(password)
    for x in range(0,3):
        r = int(random.random() * len(password))
        if r < len(password):
            passwordl[r] = password[r].capitalize()
    password = ''.join(passwordl)
    return password


class IArguments(Arguments):
    """
    IArguments
    """

    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.input = ""
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    console(get_pronounceable_password(wordcount=arguments.wordcount, digitcount=arguments.digitcount), plainprint=True)


if __name__ == "__main__":
    main()
